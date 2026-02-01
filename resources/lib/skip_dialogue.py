import xbmcgui, xbmc, xbmcaddon
import time
from xbmcgui import ACTION_NAV_BACK, ACTION_PREVIOUS_MENU, ACTION_STOP

import helper.utils as utils
from helper import LazyLogger

OK_BUTTON = 2101

INSTRUCTION_LABEL = 203
AUTHCODE_LABEL = 204
WARNING_LABEL = 205
CENTER_Y = 6
CENTER_X = 2

MIN_REMAINING_SECONDS = 5
MAX_DISPLAY_SECONDS = 6  # Maximum time to show the skip button before auto-hide
LOG = LazyLogger(__name__)

class SkipSegmentDialogue(xbmcgui.WindowXMLDialog):

    def __init__(self, xmlFile, resourcePath, seek_time_seconds, segment_type, is_initial_play=False, play_start_time=0):
        self.seek_time_seconds = seek_time_seconds
        self.segment_type = segment_type
        self.player = xbmc.Player()
        self.is_initial_play = is_initial_play
        self.play_start_time = play_start_time

    def onInit(self):
        # Read setting here (not at module level) so changes take effect without restart
        autoskip = xbmcaddon.Addon('service.jellyskip').getSettingBool('autoskip')
        if autoskip:
            # Close dialog immediately to prevent visual artifacts
            self.close()
            # Delay 5 seconds on initial play to let TV sync/blank settle
            # Only apply delay if we're within 15 seconds of pressing play in Kodi UI
            if self.is_initial_play and (time.time() - self.play_start_time) < 15:
                xbmc.sleep(5000)
            xbmc.executebuiltin('Notification(Jellyskip, Skipped %s, 3000)' % self.segment_type)
            # Do the seek directly instead of going through onClick
            if self.player.isPlaying():
                current_time = self.player.getTime()
                total_time = self.player.getTotalTime()
                # Only seek if target is ahead of current position and total_time is valid
                if total_time > 0 and self.seek_time_seconds > current_time:
                    # Set flag to prevent debounce re-tracking from triggering another skip
                    # Import here to avoid circular import
                    from dialogue_handler import dialogue_handler
                    dialogue_handler.autoskip_pending = True
                    remaining_seconds = total_time - self.seek_time_seconds
                    if remaining_seconds < MIN_REMAINING_SECONDS:
                        self.player.seekTime(total_time - MIN_REMAINING_SECONDS)
                    else:
                        self.player.seekTime(self.seek_time_seconds)
            return
        skip_label = 'Skip ' + str(self.segment_type)
        skip_button = self.getControl(OK_BUTTON)
        skip_button.setLabel(skip_label)
        self.schedule_close_action()

    def get_seconds_till_segment_end(self):
        return self.seek_time_seconds - self.player.getTime()

    def schedule_close_action(self):
        """
        Schedule the dialog to close after MAX_DISPLAY_SECONDS or when segment ends, whichever is sooner.
        :return: None
        """

        seconds_till_segment_end = self.get_seconds_till_segment_end()
        display_time = min(seconds_till_segment_end, MAX_DISPLAY_SECONDS)

        if display_time > 0:
            utils.run_threaded(self.on_automatic_close, delay=display_time, kwargs={})

    def on_automatic_close(self):
        """
        Close the dialog automatically. This is called by the scheduled thread.
        :return: None
        """
        self.close()
        xbmc.executebuiltin("NotifyAll(%s, %s, %s)" % ("service.jellyskip", "Jellyskip.DialogueClosed", {}))

    def onAction(self, action):
        if action in (ACTION_NAV_BACK, ACTION_PREVIOUS_MENU, ACTION_STOP):
            self.close()

    def onControl(self, control):
        pass

    def onFocus(self, control):
        pass

    def onClick(self, control):
        if not self.player.isPlaying():
            self.close()
            return

        if control == OK_BUTTON:
            remaining_seconds = self.player.getTotalTime() - self.seek_time_seconds

            # We don't want to skip to the end of the video (give other addons time to play, like nextup service)
            if remaining_seconds < MIN_REMAINING_SECONDS:
                self.player.seekTime(self.player.getTotalTime() - MIN_REMAINING_SECONDS)
                self.close()
            else:
                self.player.seekTime(self.seek_time_seconds)

        self.close()

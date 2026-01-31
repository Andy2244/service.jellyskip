# Jellyskip

Skip Jellyfin media segments (intros/outros) in Kodi with a button prompt or automatically.

## Features

- **Skip Button** - Shows a "Skip Intro" / "Skip Outro" button when entering a segment
- **Auto Skip** - Automatically skip segments without interaction (with brief notification)
- **Seek-back Detection** - Re-shows skip prompt when seeking back into a segment

## Requirements

- **Kodi 21 (Omega) or newer**
- **Jellyfin for Kodi addon** - installed and configured
- **Jellyfin server 10.9+** with [Intro Skipper plugin](https://github.com/intro-skipper/intro-skipper)

## Installation

### Option 1: Install via Repository (Recommended)

This method enables automatic updates.

1. Download the repository: [repository.andy2244.zip](https://github.com/Andy2244/kodi-repo/raw/main/zips/repository.andy2244/repository.andy2244-1.0.0.zip)
2. In Kodi: **Settings** → **Add-ons** → **Install from zip file**
3. Select the downloaded `repository.andy2244-1.0.0.zip`
4. Go to **Install from repository** → **Andy2244's Repository** → **Services** → **Jellyskip**
5. Click **Install**

### Option 2: Manual Install from ZIP

1. Download the latest release: [service.jellyskip.zip](https://github.com/Andy2244/kodi-repo/raw/main/zips/service.jellyskip/service.jellyskip-1.1.0.zip)
2. In Kodi: **Settings** → **Add-ons** → **Install from zip file**
3. Select the downloaded zip

> **CoreELEC/LibreELEC:** If installation fails, go to **Power** → **Restart Kodi** and try again.

## Settings

Access via: **Settings** → **Add-ons** → **My add-ons** → **Services** → **Jellyskip** → **Configure**

| Setting | Description |
|---------|-------------|
| **Auto Skip** | Automatically skip segments without showing a button. Shows a brief notification instead. On initial playback, there's a 5-second delay to allow your TV to sync. |

## Troubleshooting

### Skip button doesn't appear
- Ensure [Intro Skipper plugin](https://github.com/intro-skipper/intro-skipper) is installed on your Jellyfin server
- Check that media has detected segments (visible in Jellyfin web UI)
- Verify Jellyfin for Kodi addon is configured and synced

### Auto Skip not working after changing settings
- Settings take effect immediately, no restart needed
- If issues persist, restart Kodi

## Credits

Based on [SgtJalau/service.jellyskip](https://github.com/SgtJalau/service.jellyskip) with community improvements.

## License

GNU General Public License, v2

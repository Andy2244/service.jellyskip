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

### Option 1: Add Repository Source (Recommended)

No download required - add the repo URL directly in Kodi:

1. In Kodi: **Settings** → **File Manager** → **Add source**
2. Click `<None>` and enter: `https://raw.githubusercontent.com/Andy2244/kodi-repo/main/zips/`
3. Name it `Andy2244` and click **OK**
4. Go to **Settings** → **Add-ons** → **Install from zip file**
5. Select `Andy2244` → `repository.andy2244` → install the repository zip
6. Go to **Install from repository** → **Andy2244's Repository** → **Services** → **Jellyskip**
7. Click **Install**

### Option 2: Manual ZIP Download

1. Download: [repository.andy2244.zip](https://github.com/Andy2244/kodi-repo/raw/main/zips/repository.andy2244/repository.andy2244-1.0.1.zip)
2. In Kodi: **Settings** → **Add-ons** → **Install from zip file**
3. Select the downloaded zip
4. Then install Jellyskip from the repository

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

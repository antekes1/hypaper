# Hypaper
Extremely basic wallpaper swapping utility for Hyprland.

# Usage
- `list` lists your local wallpapers 
- `get_path` gets the currently set path of wallpapers folder
- `set_path [path]` sets new path of wallpapers folder
- `next_wallpaper` sets your wallpaper to next wallpaper form your wallpapers folder
- `set_random [source]` (source - online or local) - sets your wallpaper to random form your wallpapers folder (local) or internet (online)
- `save` - save your current online wallpaper to your wallpapers folder

# Installation
### Arch Linux
Install it with yay
```sh
yay -S hypaper
```
or paru
```sh
paru -S hypaper
```

## Other Distros
### Dependencies
Before installing, make sure you have python3 and swww installed.
### Build process
Execute the following to automatically clone, compile and move the file to your bin directory:
```sh
git https://github.com/antekes1/hypaper && cd hypaper && sudo chmod +x ./install.sh & sudo ./install.sh
```

# Configuring
Set path to your wallpapers folder with set_path (default path is ~/Pictures/Wallpapers), 
if you want keep the default path create folder in Pictures called Wallpapers

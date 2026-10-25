
To load all of this configurations just run 
```console
$ stow .
```

## Automatic Keyboard Remaps On Keyboard Layout Change
### `.config/keyboard-layout-watcher` and `.config/systemd/user/keyboard_watcher.service`
- IMPORTANT: This assumes that you have a system wide python at `/usr/bin/python3`
- This is used for sourcing of `.zshrc` on keyboard layout change
    - `.zshrc` is sourced because we want the keyboard remappings to be reapplied to the new layout
- This utalizes `systemd` to create a startup service which runs a Python script
-  

## Font

* The preferred fontface to use is `Iosevka SS02 Term`
```console
$ ./install-font.sh
```
* source: https://github.com/be5invis/Iosevka/releases

## Terminal
* For the terminal install `Alacritty`
* My favourite terminal (for now)
* settings: `.config/alacritty/`
* source: https://alacritty.org/

## Window manager
* For the window manager we use the `i3` window manager
* NOTE: For laptop brightness controll install `brightnessctl`
* settings: `.config/i3/`
* source: https://i3wm.org/

## Editor - NeoVim
* Can you call yourself a real programmer if you don't use Vim?
* settings: `.config/nvim`
* source: https://github.com/neovim/neovim

## Additional programs

* **GF2**
This is a *GNU Debugger* frontend.
Essentially a debugger for C, CPP and alike.
- settings: `.config/gf2_config.ini`
- source: https://github.com/nakst/gf

* **RipGrep (rg)**
* line-oriented search tool that recursively searches the current directory for a regex pattern
* source: https://github.com/BurntSushi/ripgrep
* install:
```console
$ sudo apt-get install ripgrep
```

---

## References

- `stow` - https://www.gnu.org/software/stow/
- `Alacritty` - https://alacritty.org/
- `i3wm` - https://i3wm.org/
- `neovim` - https://github.com/neovim/neovim
- `gf2` - https://github.com/nakst/gf
- `Iosevka fonts` - https://github.com/be5invis/Iosevka/releases
- `brightnessctl` - https://github.com/Hummer12007/brightnessctl 
- `GDBFrontend` - https://github.com/rohanrhu/gdb-frontend
- `systemd` - https://en.wikipedia.org/wiki/Systemd
- `Python` - https://www.python.org/

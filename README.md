ob-pipe-menus
=============

Some pipe menus for openbox

show_ob_keybindings.py : menu of keybindings defined in the openbox rc.xml config file  
clipboard_manager/ob_clipboard_pipe_menu.py : menu of clippings from parcellite or clipit clipboard manager
clipboard_manager/ob_clipboard_manager.py : support file for ob_clipboard_pipe_menu.py  
clipboard_manager/ob_paste_clip.py : support file for ob_clipboard_pipe_menu.py  

These files should be placed in your openbox config directory (on Ubuntu its ~/.config/openbox).  
Then for each pipe menu add a line like this to your menu.xml file:  

<menu execute="~/.config/openbox/<PIPE_MENU_FILE>" id="clipboard" label="Clipboard"/>  

For more details read the comments at the beginning of each file.

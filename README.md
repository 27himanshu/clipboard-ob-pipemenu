ob-pipe-menus
=============

Some pipe menus for openbox

show_ob_keybindings.py : menu of keybindings defined in the openbox rc.xml config file  
clipboard_manager/ob_clipboard_pipe_menu.py : menu of clippings from parcellite or clipit clipboard manager
clipboard_manager/ob_clipboard_manager.py : support file for ob_clipboard_pipe_menu.py  
clipboard_manager/ob_paste_clip.py : support file for ob_clipboard_pipe_menu.py  

These files should be placed in your openbox config directory (on Ubuntu its ~/.config/openbox).  
Dependencies:   
[xsel](http://www.vergenet.net/~conrad/software/xsel/)  
To use xvkbd instead of xsel install [xvkbd](http://homepage3.nifty.com/tsato/xvkbd/) and edit file ob_paste_clip.py at the end. Comment out xsel and uncomment xvkbd.  
For more details and installation instructions read the comments at the beginning of each file.

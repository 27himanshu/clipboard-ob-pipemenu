#!/usr/bin/env python2
# OpenBox pipe menu clipboard manager. Show parcellite clipboard, and inserts selected clip.
#
# Copyright 2013 Joe Bloggs (vapniks@yahoo.com)
#
# These scripts: ob_clipboard_manager.py, ob_clipboard_pipe_menu.py & ob_paste_clip.py
# create a pipe menu for openbox which will display the history of clippings stored by parcellite
# or clipit, and allow you to paste one of them by selecting it.
# Obviously either parcellite or clipit needs to be installed for this to work, and they should not
# be run in daemon mode.
# parcellite should be available from the usual repositories, and clipit can be
# obtained from here: http://clipit.rspwn.com/
# If clipit is used then any static clippings will also be displayed in the pipe menu.
# You may need to alter some of the following variables in ob_clipboard_manager.py:
# clipit_history_file, parcellite_history_file, max_displayed_items 

# Installation: copy ob_clipboard_manager.py, ob_clipboard_pipe_menu.py & ob_paste_clip.py to your openbox 
# config directory (on Ubuntu its ~/.config/openbox), then add an item to your openbox menu.xml file
# (also in the config dir) in the form:
#
#   <menu execute="~/.config/openbox/ob_clipboard_pipe_menu.py" id="clipboard" label="Clipboard"/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from ob_clipboard_manager import ob_cb_manager
import pygtk
import gtk
import os
import subprocess
import sys

# get the correct clipping
index = int(sys.argv[1])
manager = ob_cb_manager()
clip = manager.clippings[index]
# paste the clipping 
#x = subprocess.Popen(['xvkbd','-xsendevent','-file','-'],stdin=subprocess.PIPE,stderr=open(os.devnull)).communicate(clip)
p = subprocess.Popen(['xsel', '-b', '-i'], stdin=subprocess.PIPE, close_fds=True)
p.communicate(input=clip.encode('utf-8'))

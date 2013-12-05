#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2011~2013 Deepin, Inc.
#               2011~2013 Kaisheng Ye
#
# Author:     Kaisheng Ye <kaisheng.ye@gmail.com>
# Maintainer: Kaisheng Ye <kaisheng.ye@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import threading
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtGui import QGuiApplication

from controlpanel import ControlPanel
from unique_service import UniqueService
from constants import APP_DBUS_NAME, APP_OBJECT_PATH

def main():
    app = QGuiApplication(sys.argv)
    uniqueService = UniqueService(APP_DBUS_NAME, APP_OBJECT_PATH)
    uniqueService.uniqueTrigger.connect(unique_trigger)

    panel = ControlPanel()
    panel.engine().quit.connect(app.quit)
    panel.show()

    if len(sys.argv) == 2:
        if sys.argv[1] in panel.modulesId._l18n_names.keys():
            panel.view_object.showModule(sys.argv[1])
        else:
            print "Error module id:", sys.argv[1]
    
    thread = threading.Thread(target=panel.record_event.filter_event)
    thread.setDaemon(True)
    thread.start()

    sys.exit(app.exec_())

def unique_trigger():
    print "dss is running"

if __name__ == "__main__":
    main()

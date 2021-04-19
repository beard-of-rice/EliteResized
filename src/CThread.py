# Elite Resized - Elite Dangerous Screenshot Resizer
# Copyright (C) 2021  Nick Walsh (anomie6@yahoo.com)
# Github: beard-of-rice

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PyQt5.QtCore import QThread, pyqtSignal
import time, math, Settings

class CThread(QThread):
    valueChanged = pyqtSignal([int])
    def __init__(self,value):
        super().__init__()
        self.stop_fill = False
        Settings.completed = value


    def run(self):
        if Settings.completed < 100:
            time.sleep(0.1)
            Settings.completed += Settings.percentPerItem
            self.valueChanged.emit(int(math.ceil(Settings.completed)))

#!/usr/bin/python
# Copyright (c) 2014 Cedric Bellegarde <gnumdk@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# Many code inspiration from gnome-music at the GNOME project

class DatabaseUpgrade:

	"""
		Init object
	"""
	def __init__(self, sql, version):
		self._sql = sql
		self._version = version
		self._UPGRADES = { 1: self._db_add_modification_time }

	"""
		Return upgrade count
	"""
	def count(self):
		return len(self._UPGRADES)

	"""
		Upgrade database based on version
		Return new version
	"""	
	def do_db_upgrade(self):
		for i in range(self._version.get_int32()+1, len(self._UPGRADES)+1):
			try:
				self._UPGRADES[i]()
			except Exception as e:
				print("Database upgrade failed: ", e)
		return len(self._UPGRADES)

	"""
		Add modification time to track table
	"""
	def _db_add_modification_time(self):
 		self._sql.execute("ALTER TABLE tracks ADD COLUMN mtime INT")

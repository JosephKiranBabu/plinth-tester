#
# This file is part of Plinth-tester.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

@apps @syncthing
Feature: File Synchronization
  Run Syncthing File Synchronization server.

Background:
  Given I'm a logged in user
  Given the syncthing application is installed

Scenario: Enable syncthing application
  Given the syncthing application is disabled
  When I enable the syncthing application
  Then the syncthing service should be running

Scenario: Disable syncthing application
  Given the syncthing application is enabled
  When I disable the syncthing application
  Then the syncthing service should not be running

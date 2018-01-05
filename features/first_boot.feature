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

@first-boot @setup
Feature: First Boot
  Setup a new FreedomBox installation and create an admin user.

Scenario: Start Setup
  Given I am on the firstboot welcome page
  When I click on start setup
  Then I should be taken to the firstboot page

Scenario: Create Administrator Account
  Given I am on the firstboot page
  When I create an administrator account
  Then I should be taken to the firstboot complete page
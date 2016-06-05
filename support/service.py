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

from support import interface


# unlisted services just use the service_name as module name
service_module = {
    'ntp': 'datetime',
}


def get_service_module(service_name):
    module = service_name
    if service_name in service_module:
        module = service_module[service_name]
    return module


def is_running(browser, service_name):
    interface.nav_to_module(browser, get_service_module(service_name))
    return browser.is_text_present('is running')

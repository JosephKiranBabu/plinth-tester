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

from pytest_bdd import parsers, when, then

from support import system


language_codes = {
    'Danish': 'da',
    'German': 'de',
    'Spanish': 'es',
    'French': 'fr',
    'Norwegian Bokmål': 'nb',
    'Dutch': 'nl',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Russian': 'ru',
    'Swedish': 'sv',
    'Telugu': 'te',
    'Turkish': 'tr',
    'Simplified Chinese': 'zh-hans',
}


@when(parsers.parse('I change the hostname to {hostname:w}'))
def change_hostname_to(browser, hostname):
    system.set_hostname(browser, hostname)


@when(parsers.parse('I change the domain name to {domain:w}'))
def change_domain_name_to(browser, domain):
    system.set_domain_name(browser, domain)


@when('I change the language to <language>')
def change_language(browser, language):
    system.set_language(browser, language_codes[language])


@then(parsers.parse('the hostname should be {hostname:w}'))
def hostname_should_be(browser, hostname):
    assert(system.get_hostname(browser) == hostname)


@then(parsers.parse('the domain name should be {domain:w}'))
def domain_name_should_be(browser, domain):
    assert(system.get_domain_name(browser) == domain)


@then('Plinth language should be <language>')
def plinth_language_should_be(browser, language):
    assert(system.check_language(browser, language_codes[language]) == True)

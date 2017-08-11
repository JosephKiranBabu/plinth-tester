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

from pytest_bdd import parsers, given, when, then

from support import config, interface


@given("I'm a logged in user")
def logged_in_user(browser):
    interface.login(browser, config['DEFAULT']['url'],
                    config['DEFAULT']['username'],
                    config['DEFAULT']['password'])


@given("I'm a logged out user")
def logged_out_user(browser):
    browser.visit(config['DEFAULT']['url'] + '/plinth/accounts/logout/')


@then(parsers.parse('I should be prompted for login'))
def prompted_for_login(browser):
    assert interface.is_login_prompt(browser)


@given(parsers.parse("the user {name:w} doesn't exist"))
def new_user_does_not_exist(browser, name):
    interface.nav_to_module(browser, 'users')
    delete_link = browser.find_link_by_href('/plinth/sys/users/' + name +
                                            '/delete/')
    if delete_link:
        delete_link.first.click()
        browser.find_by_value('Delete ' + name).click()


@given(parsers.parse('the user {name:w} exists'))
def test_user_exists(browser, name):
    interface.nav_to_module(browser, 'users')
    user_link = browser.find_link_by_href('/plinth/sys/users/' + name +
                                          '/edit/')
    if not user_link:
        create_user(browser, name, 'secret')


@when(
    parsers.parse('I create a user named {name:w} with password {password:w}'))
def create_user(browser, name, password):
    interface.create_user(browser, name, password)


@when(parsers.parse('I rename the user {old_name:w} to {new_name:w}'))
def rename_user(browser, old_name, new_name):
    interface.rename_user(browser, old_name, new_name)


@when(parsers.parse('I delete the user {name:w}'))
def delete_user(browser, name):
    interface.delete_user(browser, name)


@then(parsers.parse('{name:w} should be listed as a user'))
def new_user_is_listed(browser, name):
    assert interface.is_user(browser, name)


@then(parsers.parse('{name:w} should not be listed as a user'))
def new_user_is_not_listed(browser, name):
    assert not interface.is_user(browser, name)

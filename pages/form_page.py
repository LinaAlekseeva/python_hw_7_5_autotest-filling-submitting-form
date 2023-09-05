from poetry.console.commands import self
from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FromPageLocators as Locators


class FormPage(BasePage):
    first_name = 'Lina'
    last_name = 'Alekseeva'
    email = 'hello@world.com'
    self.remove_footer()
    self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
    self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
    self.element_is_visible(Locators.EMAIL).send_keys(email)
    self.element_is_visible(Locators.GENDER).click
    self.element_is_visible(Locators.MOBILE).send_keys('1234454678')
    subject = self.element_is_visible(Locators.SUBJECT)
    subject.send_keys('English')
    subject.send_keys(Keys.RETURN)
    self.element_is_visible(Locators.HOBBIES).click
    self.element_is_visible(Locators.FILE_INPUT).send_keys('tests/test.txt')
    self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys("City, 12356, USA")
    self.element_is_visible(Locators.SUBMIT).click

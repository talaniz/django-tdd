from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def test_user_can_register_and_login(self):
        # Edith goes to the awesome superlists site and notices a new login
        # screen.
        self.browser.get(self.server_url)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(header_text, 'Login')

        # She doesn't have an account, so she clicks the register link
        self.browser.find_element_by_id('register').click()

        # She is redirected to a registration page where she is prompted to 
        # enter an email address, name and password twice (once to confirm).
        registration_header = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(registration_header, 'Register')

        # She enters her information in the appropriate fields and clicks
        # submit
        email_field = self.browser.find_element_by_id('id_email')
        email_field.send_keys('edith@edith.com')

        name_field = self.browser.find_element_by_id('id_name')
        name_field.send_keys('Edith Jones')

        password1 = self.browser.find_element_by_id('id_password1')
        password1.send_keys('secret')

        password2 = self.browser.find_element_by_id('id_password2')
        password2.send_keys('secret')

        self.browser.find_element_by_id('submit').click()

        # She is then redirected back to the login page to enter her 
        # credentials
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(header_text, 'Login')

        email_field = self.browser.find_element_by_id('id_username')
        email_field.send_keys('edith@edith.com')

        password_field = self.browser.find_element_by_id('id_password')
        password_field.send_keys('secret')
 
        self.browser.find_element_by_id('submit').click()

        # She is redirected back to To-Do lists page to begin a new list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

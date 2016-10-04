from django.test import TestCase

class LoginTestCase(TestCase):

    def test_login_view_uses_correct_template(self):
        response = self.client.get('/login')

        self.assertTemplateUsed(response, 'login.html')

    def test_user_can_login(self):
        response = self.client.post('/login', {'name': 'Edith Jones', 
                                               'email':'edit@exaple.com', 
                                               'password': 'password'})

        self.assertEqual(response.status_code, 200)

    def test_user_cannot_login_without_credentials(self):
        response = self.client.post('/login')

        self.assertContains(response, 'errorlist')

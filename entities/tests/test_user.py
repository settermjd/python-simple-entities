from unittest import TestCase
from entities.user import User


class UserTest(TestCase):
    def setUp(self):
        # Initialise an empty User instance
        self.user = User()

    def test_can_retrieve_name(self):
        self.assertEqual(self.user.getName(), None,
                         'Name should not be set')

    def test_can_set_name(self):
        self.user.setName('Matthew')
        self.assertEqual(self.user.getName(), 'Matthew',
                         'Name should have been set to "Matthew"')

if __name__ == '__main__':
    unittest.main()

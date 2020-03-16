import unittest


class SignupTest(unittest.TestCase):

    def test_Signbyemail(self):
        print("Sign by email pass")
        self.assertTrue(True)

    def test_Signbyfacebook(self):
        print("Sign by facebook pass")
        self.assertTrue(True)

    def test_Signnbytwitter(self):
        print("Sign by twitter pass")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()

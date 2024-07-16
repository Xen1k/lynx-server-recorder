from compare_faces import compare_faces
import unittest

class TestFacesComparison(unittest.TestCase):
    def test_faces(self):
        self.assertTrue(compare_faces('./tests/hans1.jpg', './tests/hans2.jpg'))
        self.assertFalse(compare_faces('./tests/hans1.jpg', './tests/girl1.jpg'))

if __name__ == '__main__':
    unittest.main()

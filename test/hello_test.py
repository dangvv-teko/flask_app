import unittest
import sys
sys.path.append('./')
from flask_app.hello import hello
import json


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual("Hello Dang", hello(name="Dang"))
        self.assertEqual("Hello World", hello())

if __name__ == "__main__":
    unittest.main()
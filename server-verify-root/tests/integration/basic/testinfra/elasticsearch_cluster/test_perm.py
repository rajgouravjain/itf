import unittest
import testinfra
import pytest
from parameterized import parameterized, param

class TestPerm(unittest.TestCase):

    def setUp(self):
        self.host = testinfra.get_host("local://")

    @parameterized.expand([
      ( "boto3",  "1.16.40"), \
      ( "pip", "21.1.1")
    ])
    def test_package(self,pkg,ver):
      p = self.host.pip(pkg)
      assert p.is_installed
      assert p.version == ver


if __name__ == "__main__":
    unittest.main()

import unittest
import time
from getpass import getpass
from .test_accounts import AccountTests

class TestCommon(unittest.TestCase):
  def __init__(self):
    self._sid = getpass("Enter SID: ")
    self._auth_token = getpass("Enter Auth Token: ")

  def tearDown(self):
    time.sleep(1)    

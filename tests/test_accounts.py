from ziron import Account
from .__init__ import TestCommon

class AccountTests(TestCommon):
  """Test ziron commands
  """

  def test_getAccount(self):
    self.assertTrue(self.z.getAccount().has_key('sid'))

  def test_updateAccount(self):
    last_name = self.z.getAccount("last_name")
    self.z.updateAccount({"last_name": "test"})
    self.assertTrue(self.z.getAccount('last_name') == "test")
    self.z.updateAccount({"last_name": last_name})
    self.assertTrue(self.z.getAccount()['last_name'] == last_name)


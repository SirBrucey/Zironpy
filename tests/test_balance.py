
class BalanceTests(TestCommon):
  def test_getBalance(self):
    self.assertTrue(self.z.getBalance().has_key('balance'))


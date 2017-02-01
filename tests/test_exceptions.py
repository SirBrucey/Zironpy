
class ExceptionTests(TestCommon):
  """Asserts API errors raise the correct exception
  """
  def testAPIError(self):
    self.assertRaises(ziron.APIError)
  def testValueError(self):
    self.assertRaises(ziron.ValueError)


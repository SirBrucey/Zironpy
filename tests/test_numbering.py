
class NumberingTests(TestCommon):
  """Check commands for Numbering API work
  """
  def test_getCountries(self):
    countries = self.z.getCountries()
    self.assertTrue(isinstance(countries, list))
    self.assertTrue(countries[0].has_key("country_iso"))

  def test_getStates(self):
    states = self.z.getStates("GB")
    self.assertTrue(isinstance(states, list))
    self.assertTrue(states[0].has_key("prefix"))

  def test_getAreas(self):
    area = self.z.getAreas("US", "AL")
    self.assertTrue(isinstance(area, list))
    self.assertTrue(area[0].has_key("prefix"))
    
  def test_getRestrictions(self):
    restrictions = self.z.getRestrictions("AR")
    self.assertTrue(isinstance(restrictions, list))
    self.assertTrue(restrictions[0].has_key("restriction_type"))

  def listAvailableNumbers(self):
    return
  def purchaseNumbers(self):
    return
  def getNumbers(self):

    return
  def getIndividualNumber(self):
    return
  def updateIndividualNumber(self):
    return
  def attachEndpoint(self):
    return
  def detachEndpoint(self):
    return
  def getNumberEndpoints(self):
    return

  def deleteIndividualNumber(self):
    """Not sure How to test this yet
    """
    return


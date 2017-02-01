from .ziron import Ziron

class Numbering(Ziron):
  # Numbering
  # https://zironuk.atlassian.net/wiki/display/docs/Numbering+API

  def getCountries(self):
    return self.__request(self._base_url + "/Numbers/Available", "GET")

  def getStates(self, country_iso):
    self._check_code(country_iso)
    return self.__request(self._base_url + "/Numbers/Available/" + country_iso,
                          "GET")

  def getAreas(self, country_iso, state=None):
    self._check_code(country_iso)
    if state:
      self._check_code(country_iso)
      return self.__request(self._base_url + "/Numbers/Available/" +
                            country_iso + "/" + state, "GET")
    else:
      return self.__request(self._base_url + "/Numbers/Available/" +
                            country_iso, "GET")

  def getRestrictions(self, country_iso, number_type=None):
    """Add number_type variable
    """
    self._check_code(country_iso)
    return self.__request(self._base_url + "/Numbers/Restrictions/" +
                          country_iso, "GET")

  def listAvailableNumbers(self):
    return
  def purchaseNumbers(self):
    return

  def getNumbers(self, search=None, unattached=None):
    """Return deatails about numbers
    Args:
      search      - search for match within number, description, country_iso, 
                    state_abbr or area field.
      unattached  - set to '1' to show numbers that are not attached to an 
                    endpoint.
    Returns:
      A paginated list of numbers on our account. Each element in the list is
      a dictionary with all the details for said number.
    """
    url = self._base_url + "/Numbers/Assigned?search="
    if search: url += search
    if unattached:
      if unattached == 1:
        url += "&unattached=1"
      else:
        raise ValueError("Unattatched must be set to 1; or not called at all")

    return self.__request(url, "GET")

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
  def deleteIndividualNumber(self, number_sid):
    """Delete a number from your account.
    Args:
      number_sid - ID of individual number. Can be found using getNumbers.
    """
    return self.__request(self._base_url + "/Numbers/Assigned/" + number_sid,
                          "DELETE")


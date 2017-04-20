from .ziron import Ziron

class NumberRangeLookups(Ziron):
  # Number range lookups
  # https://zironuk.atlassian.net/wiki/display/docs/Lookups+API
  def HLRLookup(self, lookup_type, number):
    """The HLR Lookup service allows you to query the mobile network for a range of 
    subscriber information, and can be used for mobile number validation, porting  
    check, and roaming status.

    Args:
      lookup_type - Type of lookup to perform. 
                    Valid values: get_country, hashed_imsi, home_network.
      number      - The number to lookup. E164 format.
    """

    data = {}

    if lookup_type not in ['get_country', 'hashed_imsi', 'home_network']:
      raise ValueError("Invalid Lookup Type, see documentation")
    else:
      data['lookup_type'] = lookup_type

    if self._check_e164(number): data['number'] = number

    return self._request(self._base_url + "/Lookups/HLR", "POST", data)

  def numberPortabilityLookup(self, number):
    """Performs a Number Portability lookup on a number. 
    https://zironuk.atlassian.net/wiki/display/docs/Number+Portability+Lookup

    Args:
      number - The number to lookup. E164 format.
    Method: POST
    """
    
    data = {}

    if self._check_e164(number): data['number'] = number

    return self._request(self._base_url+"/Lookups/NP", "POST", data)

  def getLookups(self):
    # Not implementing at present, will implement once pagination is reworked.
    return

  def getIndividualLookup(self, lookup_sid, key=None):
    """Returns information on a single lookup
    
    Args: 
      lookup_sid - Individual sid for the endpoint you with to retrieve information on.
      key        - Retunrn specific value based on given key.
    """
    self._check_sid(lookup_sid)
    if not key:
      return self._request(self._base_url+"/Lookups/"+lookup_sid, "GET")
    else:
      return self._request(self._base_url+"/Lookups/"+lookup_sid, "GET")[key]



from .ziron import Ziron

class Porting(Ziron):
  # Porting
  # https://zironuk.atlassian.net/wiki/display/docs/Porting+API
  def getIndividualPortingCountry(self, country_iso):
    """Retrieve details of an individual country where numbers can be ported
    """
    self._check_code(country_iso)
    return self._request(self._base_url + "/Porting/Countries/" + country_iso,
                         "GET")

  def getPortingCountries(self):
    """Retrieve a list of countries where numbers can be ported
    """
    return self._request(self._base_url + "/Porting/Countries", "GET")

  def getPortingOperators(self, country_iso, number_type=None):
    """Returns a list of operators that numbers can be ported from.
    """
    self._check_code(country_iso)
    url =  self._base_url + "/Porting/Countries/" + country_iso + "/Operators"

    if number_type:
      if number_type not in ['local', 'national', 'tollfree', 'mobile']:
        raise ValueError("Invalid number type. Please check documentation")
      else: 
        url = url + "?number_type=" + number_type

    return self._request(url, "GET")

  def createPortingRequest(self):
    return

  def getIndividualPortingRequest(self, porting_sid):
    """Returns an individual porting request
    """
    self._check_sid(porting_sid)
    return self._request(self._base_url + "/Porting/Requests/" + porting_sid,
                         "GET")

  def getPortingRequestEvents(self, porting_sid):
    """Returns an unpaginated list of porting request events. 
    """
    self._check_sid(porting_sid)
    return self._request(self._base_url + "/Porting/Requests/" + porting_sid +
                         "/Events", "GET")

  def getPortingRequests(self, limit=None, start=None, end=None):
    """Returns a paginated list of porting requests

    Args:
      limit  - Number of results to be returned. Default = 100. If Limit = all
               get all results
      start  - Datetime to signify the start of the daterange you wish to return.
      end    - Datetime to signify the end of the daterange you wish to return.
    """
    url = self._base_url + "/Porting/Requests"
    method = "GET"
    
    # Default return 100 records
    if (not limit) and (not start) and (not end):
      return self._request(url, "GET")['result']

    if not isinstance(limit, int):
      # Get all records
      if (limit == "all"):
        return self._pagination_limit(url, method, "all")

      # Get records within date range
      elif start or end:
        if start and end:
          return self._pagination_range(url, method, start=start, end=end)
        elif start:
          return self._pagination_range(url, method, start=start)
        elif end:
          return self._pagination_range(url, method, end=end)
        else:
          raise ValueError("Unknown time constraints")

      else:
        raise ValueError("Unknown request, please check documentation")

    else:
      if limit <= 100 and limit > 0:
        return self._request(url+"?limit="+str(limit), "GET")['result']
      elif limit > 100:
        return self._pagination_limit(url, method, limit)['result']
      else:
        raise ValueError("Limit Must be an integer greater than 0")


  def submitPortingRequest(self):
    return

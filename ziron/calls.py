from .ziron import Ziron

class Calls(Ziron):
  # Calls
  # https://zironuk.atlassian.net/wiki/display/docs/Calls+API
  def getCalls(self, limit=None, start=None, end=None):
    """Get call information. CDRs are paginatated into pages of 100 recrords.

    Args:
      limit  - Number of results to be returned. Default = 100. If Limit = all
               get all CDRs
      start  - 
      end    -

    Todo:
      Add ability to get all call data within a Datetime
    """
    url = self._base_url+"/Calls"
    method = "GET"

    # Default return 100 records
    if (not limit) and (not start) and (not end):
      return self._request(url, "GET")

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
        raise ValueError("Unknown CDR request, please check documentation")

    else:
      if limit <= 100 and limit > 0:
        return self._request(url+"?limit="+str(limit), "GET")['result']
      elif limit > 100:
        return self._pagination_limit(url, method, limit)
      else:
        raise ValueError("Limit Must be an integer greater than 0")

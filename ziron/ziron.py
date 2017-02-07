import requests
import json
import time
import re


class Ziron(object):
  """Python Lib to talk to Ziron's API.
  Documentation can be found:
  https://zironuk.atlassian.net/wiki/display/docs/Developer+API
  """

  def __init__(self, sid, auth_token):
    """Initalise session
    """
    self._sid = sid
    self._auth_token = auth_token
    self._base_url = "https://api.ziron.net/v1/Accounts/" + sid
    self.session = requests.session()
    self.session.headers['User-Agent'] = "Andrews and Arnold Ziron Client"
    self.session.headers['Host'] = "api.ziron.net"
    self.session.headers['Accept'] = "application/json"

  def _request(self, url, method, data=None):
    """Send different types of HTTP request to Ziron.    
    """
    if method == "GET":
      resp = self.session.get(url, auth=(self._sid, self._auth_token))
    elif method == "PUT":
      resp = self.session.put(url, data=data,
                              auth=(self._sid, self._auth_token))
    elif method == "POST":
      resp = self.session.post(url, data, auth=(self._sid, self._auth_token))
    elif method == "DELETE":
      resp = self.session.delete(url, auth=(self._sid, self._auth_token))
    else:
      raise APIError("Unknown HTTP request type: " + method)

    if resp.status_code != requests.codes.ok:
      resp.raise_for_status()

    # When deleting a number, you get 204 back with no data. 
    if (not resp.status_code == 204) and (not method=="DELETE"):
      resp = resp.json()

    if "error" in resp:
      raise APIError(resp['error'])

    return resp

  def _pagination_limit(self, url, method, limit=None):
    """Function to return a certain number of records, where the response is a
    paginated list and the desired limit is greater than 100.

    Args:
      url    - Full API url, eg: _base_url+"/Calls"
      method - HTTP method, eg "GET"
      limit  - Can be "all" or an int

    Returns:
      A list of records in disctionary format
    """
    results = []
    _page = self._request(url, method)
    _page_number = 1
    _total_pages = _page['meta']['last_page']

    results = _page['result']

    while _page_number < _total_pages:
      _page = self._request(url + "?offset=" + str(_page_number*100), method)
      _page_number += 1

      if limit:
        if (_page_number * 100) >= limit:
          _count = 100 - ((_page_number * 100) - limit)
          for record in _page['result']:
            while count > 0:
              results.append(record)
              _count -= 1

          return results

        # Add a whole page to list
        else:
          results += _page['result']

      else:
        raise ValueError("Invalid selection, Limit or dates range must be set")

    return results

  def _pagination_range(self, url, method, start=None, end=None):
    """Returns records form a paginated list in a given date time range.

    Args:
      start - Oldest datetime to return, eg: start="2017-01-01 00:00:00"
      end   - Newest datetime to return, eg: end="2017-01-31 23:59:59"

    Returns:
      If both start and end supplied, it will give a list of CDRs between the 
      given datetimes.
      If only start is given, it will return all records from after the 
      datetime.
      If only end is given, it will return all records from before the datetime.
    """
    if (not start) or (not end):
      raise ValueError("Start and End must be supplied")

    # Check datetime supplied in correct format
    if start: time.strptime(start, "%Y-%m-%d %H:%M:%S")
    if end: time.strptime(end, "%Y-%m-%d %H:%M:%S")

    results = []
    _page = self._request(url, method)
    _page_number = 1
    _total_pages = _page['meta']['last_page']

    while _page_number < _total_pages:
      for record in _page['result']:
        _count = 0
        for key in record:
          if key.startswith("ts"):    # Ts fields are not labeled consitently
            ts = record[key].replace("T", " ").replace("Z","")

            if (ts >= start) and (ts <= end):
              results.append(record)
              _count += 1

      # If no results on page break out of loop         
      if _count == 0:
        break

      # Move on to next page in loop
      _page = self._request(url + "?offset=" + str(_page_number*100), method)
      _page_number += 1

    return results

  def _check_code(self, code):
    if not re.match(r'^[A-Z]{2}$', code):
      error = "Invalid code. Code should be 2 alpha characters. eg: 'GB' / 'CA'"
      raise ValueError(error)
    return


from .ziron import Ziron

class Account(Ziron):
  # Accounts
  # https://zironuk.atlassian.net/wiki/display/docs/Accounts+API
  def getAccount(self, key=None):
    """Get your account information.

    Args:
      key=None  - Return all account details.
      key=Value - Return Specific Value.
    """
    if not key:
      return self._request(self._base_url, "GET")
    else:
      return self._request(self._base_url, "GET")[key]

  def updateAccount(self, data):
    """Update account information. 

    Args:
      data - Dictionary of fields you wish to change and the new values.
    """
    return self.__request(self._base_url, "PUT", data)


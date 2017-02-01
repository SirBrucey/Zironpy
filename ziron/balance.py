from .ziron import Ziron

class Balance(Ziron):
  # Balance
  # https://zironuk.atlassian.net/wiki/display/docs/Balance+API
  def getBalance(self):
    """Return your current balance
    """
    return self._request(self._base_url+"/Balance", "GET")

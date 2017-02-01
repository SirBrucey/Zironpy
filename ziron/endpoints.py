from .ziron import Ziron 

class EndPoints(Ziron):
  # Endpoints
  # https://zironuk.atlassian.net/wiki/display/docs/Endpoints+API
  def createEndpoints(self):
    return
  def deleteEndpoints(self):
    return

  def getEndpoints(self):
    """Get information on current end points. Results are paginated.
    """
    return self.__request(self._base_url+"/Endpoints", "GET")

  def getEndpointTypes(self):
    return
  def getIndividualEndpoint(self):
    return
  def updateIndividualEndpoint(self):
    return


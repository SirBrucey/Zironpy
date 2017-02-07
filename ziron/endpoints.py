from .ziron import Ziron 

class Endpoints(Ziron):
  # Endpoints
  # https://zironuk.atlassian.net/wiki/display/docs/Endpoints+API
  def createEndpoint(self, endpointType, uri, description=None, default=None):
    """Create a new endpoint

    Args:
      endpointType - Type of endpoint. Eg: voice, mms, fax, sms
      uri          - URI for the endpoint
      description  - User defined description for this endpoint. (Optional)
      default      - If defined will make this end point the default for new numbers.
    """
    if (default) and (default != 0): 
      default = 1
    else:
      default = 0

    allow = 0
    for allowed in self._request(self._base_url+"/Endpoints/Types", "GET"):
      if endpointType in allowed['type']:
        allow += 1
      
    if allow == 0:
      raise ValueError("Invalid Endpoint type. See getEndpointTypes for valid values")

    data = {'type': endpointType, 'uri': uri, 'description': description, 
            'is_default': default}

    return self._request(self._base_url+"/Endpoints", "POST", data)

  def deleteEndpoint(self, endpoint_sid):
    """Delete a given endpoint
    
    Args:
      endpoint_sid - Unique sid for the endpoint you wish to delete
    """
    return self._request(self._base_url+"/Endpoints/"+endpoint_sid, "DELETE")

  def getEndpoints(self, limit=None, start=None, end=None):
    """Get information on current end points. Results are paginated.

    Args: 
      limit   - Number of results to be returned. Default = 10. If limit = all get all
                endpoints
      start   - Datetime to signify the start of the daterange you wish to return.
      end     - Datetime to signify the end of the daterange you wish to return.
    """

    url = self._base_url+"/Endpoints"
    method = "GET"

    # Default return the last 100 results
    if (not limit) and (not start) and (not end):
      return self._request(self._base_url+"/Endpoints", "GET")['result']

    if not isinstance(limit, int):
      # Return all endpoints
      if (limit == "all"):
        return self._pagination_limit(url, method, "all")

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
        raise ValueError("Invalid Request")

    else:
      if limit <= 100 and limit > 0:
        return self._request(url+"?limit="+str(limit), "GET")['result']
      elif limit > 100:
        return self._pagination_limit(url, method, limit)
      else:
        raise ValueError("Limit Must be an integer greater than 0")


  def getEndpointTypes(self):
    """Returns a list of valid Endpoint types
    """
    return self._request(self._base_url+"/Endpoints/Types", "GET")

  def getIndividualEndpoint(self, endpoint_sid, key=None):
    """Returns information on a single endpoint
    
    Args: 
      endpoint_sid - Individual sid for the endpoint you with to retrieve information on.
      key          - Retunr specific value based on given key.
    """
    if not key:
      return self._request(self._base_url+"/Endpoints/"+endpoint_sid, "GET")
    else:
      return self._request(self._base_url+"/Endpoints/"+endpoint_sid, "GET")[key]
      
  def updateIndividualEndpoint(self, sid, endpointType=None, uri=None, 
                               description=None, default=None):
    """Update field or fields for an endpoint defined by sid.

    Args:
      sid           - ID of endpoint you are updating
      endpointType  - Type of endpoint your want to update your endpoint to.
      uri           - URI you want to update your endpoint to.
      description   - Updated description for endpointType.
      default       - Update whether or not this should be the default endpoint for new
                      numbers.
    """

    data = {}
    if (default) and (default != 0):
      data['default'] = 1
    else:
      data['default'] = 0

    if endpointType:   
      allow = 0
      for allowed in self._request(self._base_url+"/Endpoints/Types", "GET"):
        if endpointType in allowed['type']:
          allow += 1

      if allow == 0:
        raise ValueError("Invalid Endpoint type. See getEndpointTypes for valid values")
      data['type'] = endpointType

    if uri: data['uri'] = uri
    if description: data['description'] = description
   
    return self._request(self._base_url+"/Endpoints/"+sid, "PUT", data)


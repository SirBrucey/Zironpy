from .ziron import Ziron

class Messages(Ziron):
  # Messages
  # https://zironuk.atlassian.net/wiki/display/docs/Messages+API
  def sendMessage(self, src, dest, data, message_type="sms", mclass=None, mwi=None, 
                   callback_url=None):
    """Send a message to one or more recipients. 
    Returns an unpaginated list of message details.

    Args:
      src           - Source number or name in E164 format
      dest          - Destination numbers in E164 format
      data          - Message body
      message_type  - Type of message to send. Default SMS
      mclass        - Message class in the DCS field (SMS only)
                      0 (flash SMS), 1 (mobile), 2 (SIM), 3 (SIM toolkit)
      mwi           - Activate/deactivate the message waiting indicator (SMS only)
                      0 (activate voicemail), 1 (activate fax), 2 (activate email), 
                      3 (activate other), 4 (deactivate voicemail), 5 (deactivate fax),
                      6 (deactivate email), 7 (deactivate other)
      callback_url  - URL to receive message status callbacks
    """

    post = {}

    # Validate Source and Destination numbers
    try:
      if self._check_e164(src): 
        post['src'] = src
    except: 
      try:
        if self._check_alphanumeric(src, 11): 
          post['src'] = src
      except Exception, e:
        raise ValueError("Invalid source, please see documentation")
      
    if self._check_e164(dest): post['dst'] = dest

    post['data'] = data
    post['message_type'] = message_type

    # If message type sms, check mclass and mwi
    if message_type == "sms":
      if mclass:
        if mclass not in [0,1,2,3]:
          raise ValueError("Invalid option for mclass, please see documentation.")
        post['mclass'] = mclass
      if mwi:
        if mwi not in [0,1,2,3,4,5,6,7]:
          raise ValueError("Invalid option for mwi, please see documentation.")
        post['mwi'] = mwi

    if callback_url: post['callback_url'] = callback_url       

    return self._request(self._base_url+"/Messages", "POST", post)

  def getMessages(self):
    # Needs doing once pagination has been rewritten
    return

  def getIndividualMessage(self, message_sid, key=None):
    """Returns information on a single messgae
    
    Args: 
      message_sid - Individual sid for the message you with to retrieve information on.
      key         - Retunrn specific value based on given key.
    """
    if not key:
      return self._request(self._base_url+"/Messages/"+message_sid, "GET")
    else:
      return self._request(self._base_url+"/Messages/"+message_sid, "GET")[key]
 
  def getMessageHistory(self, message_sid):
    """Return a list of message statuses for a given message. SMS only.

    Args:
      message_sid - Unique ID for the message you wish to retrieve the message history 
                    for.
    """

    return self._request(self._base_url+"/Messages/"+message_sid+"/History", "GET")

  def messageDeliveryStats(self):
    return


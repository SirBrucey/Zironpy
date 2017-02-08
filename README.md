# Zironpy

# Contents

* [Todo](#todo)
* [Setup](#setup)
  * [Installation](#installation)
  * [Testing](#testing)
* [Commands](#commands)
  * [Accounts](#accounts)
    * [getAccount](#getAccount)
    * [updateAccount](#updateAccount)
  * [Balance](#balance)
    * [getBalance](#getBalance)
  * [Calls](#calls)
    * [getCalls](#getCalls)
  * [End Points](#endpoints)
    * [createEndpoint](#createEndpoint)
    * [deleteEndpoint](#deleteEndpoint)
    * [getEndpoints](#getEndpoints)
    * [getEndpointTypes](#getEndpointTypes)
    * [getIndividualEndpoint](#getIndividualEndpoint)
    * [updateIndividualEndpoint](#updateIndividualEndpoint)
  * [Messages](#messages)
    * [sendMessage](#sendMessage)
    * [getMessages](#getMessages)
    * [getIndividualMessage](#getIndividualMessage)
    * [getMessageHistory](#getMessageHistory)
    * [messageDeliveryStatistics](#messageDeliveryStatistics)
  * [Number Range Lookups](#nrl)
    * [HLRLookup](#HLRLookup)
    * [numberPortabilityLookup](#numberPortabilityLookup)
    * [getlookups](#getLookups)
    * [getIndividualLookup](#getIndividualLookup)
  * [Numbering](#numbering)
  * [Payments](#payments)
  * [Pricing](#pricing)
  * [Resources](#resources)
  * [Transactions](#transactions)
  * [Trunks](#trunks)

<a name="todo"/>
# TODO
* Rewrite Pagination

  Places currentluing pagination or will be later:
    * [getCalls](#getCalls)
    * [getEndpoints](#getEndpoints)
    * [getMessages](#getMessages)
    * [getlookups](#getLookups)

<a name="setup"/>
# Setup

<a name="installtion"/>
## Installation

<a name="testing"/>
## Testing

<a name="commands"/>
# Commands

The Ziron developer API is split into multiple sub APIs for different operational
aspects.

Each sub API can be imported seperatly; or you can import all of them at once:

```python
import ziron
```
---
<a name="accounts"/>
## Accounts

The accounts API allows you to manage your individual Ziron account.
> https://zironuk.atlassian.net/wiki/display/docs/Accounts+API

**Import:**
```python
>>> from ziron import Accounts
>>> accounts = Accounts(sid, auth_token)
```
<a name="getAccount"/>
### getAccount(*key*)

The getAccount command returns currently set details about your account.
> https://zironuk.atlassian.net/wiki/display/docs/Get+Account

**Arguments:**

* Required: None

* Optional:
  * key - Return corresponding value from dictionary

  If key is not specified then all results are returned as a dictionary.

**Examples:**
```python
>>> print accounts.getAccount()
{u'last_name': u'xxxxx', u'notification_daily': u'0', u'auth_token': u'xxxxx', u'vat_number': u'', 
 u'postpay_billing_cycle': u'm', u'currency': u'GBP', u'postpay_payment_days': u'14', u'address_state': u'xxxxx', 
 u'timezone': u'Europe/London', u'account_name': u'Andrews & Arnold Ltd', u'rates_email': None, 
 u'address_line2': u'xxxxxx', u'first_name': u'xxxxx', u'address_line1': u'xxxxx', u'detailed_lookup': u'1', 
 u'store_content': u'1', u'notification_low_balance': u'1', u'postpay_credit_limit': u'2000.00000', 
 u'sid': u'xxxxx', u'invoice_email': None, u'postpay_invoice_type': u'e', u'email': u'xxxxx', 
 u'default_prefix': u'44', u'show_financials': u'1', u'vat_code': u'gb', u'invoice_account_email': u'1', 
 u'notification_low_balance_level': u'0.00', u'balance_threshold': u'10', u'address_zip': u'xxxxx', 
 u'address_city': u'xxxxx', u'account_ref': u'xxxxx', u'country': u'GB', u'restricted_lookup': u'1', 
 u'default_sender': u'', u'rates_account_email': u'0', u'postpay_enabled': u'1', u'balance': u'1000.00000'}

>>> print accounts.getAccount('currency')
GBP
```
<a name="updateAccount"/>
### updateAccount(*data*)

The update command take a dictionary of the account values you wish to update.
> https://zironuk.atlassian.net/wiki/display/docs/Update+Account

**Arguments:**

* Required:
  * data - Dicionary of values you wish to update

* Optional: None

**Examples:**

```python
>>> account.updateAccount({'first_name': 'Foo', 'last_name': 'Bar'})
```

---
<a name"balance"/>
## Balance

The balance API allows you to your current account balance.
> https://zironuk.atlassian.net/wiki/display/docs/Balance+API

**Import:**
```python
>>> from ziron import Balance
>>> balance = Balance(sid, auth_token)
```

<a name="getBalance"/>
### getBalance()

The getBalance command returns your accounts current balance and the ISO 4217 currency code.
> https://zironuk.atlassian.net/wiki/display/docs/Get+Balance

**Arguments:**

* Required: None
* Optional: None

**Examples:**

```python
>>> print balance.getBalance()
{u'currency': u'GBP', u'balance': u'100.00000'}
```
---
<a name="calls"/>
## Calls

The calls API allows you to retrieve CDRs
> https://zironuk.atlassian.net/wiki/display/docs/Calls+API 

**Import:**

```python 
>>> from ziron import Calls
>>> calls = Calls(sid, auth_token)
```

<a name="getCalls"/>
### getCalls(*limit*, *start*, *end*)

The getCalls command allows you to return a list of CDRs for a given number of CDRs or within a given date range.
> https://zironuk.atlassian.net/wiki/display/docs/Get+Calls

**Arguments:**
* Required: None
* Optional:
  * limit - Either 1-100 or "all", limit the number number of results returned, if all return all CDRs ever.
  * start - Datetime in the form YYYY-MM-DD HH-MM-SS to signify the start of the daterange you wish to return.
  * end - Datetime in the form YYYY-MM-DD HH-MM-SS to signify the end of the daterange you wish to return.

**Examples**

```python
>>> print calls.getCalls(limit=1)
[{u'src': u'44xxxxxxxxxx', u'billed_duration': u'0.2333333', u'call_duration': u'0.2333333', 
  u'ts': u'2017-02-07T12:10:57Z', u'sid': u'xxxxxxx', u'type': u'call-in', u'dst': u'44xxxxxxxxxx'}]
>>> calls.getCalls(start="2017-02-07 11:00:00", end="2017-02-07 13:00:00")
[{u'src': u'44xxxxxxxxxx', u'billed_duration': u'0.2333333', u'call_duration': u'0.2333333', 
  u'ts': u'2017-02-07T12:10:57Z', u'sid': u'xxxxxxx', u'type': u'call-in', u'dst': u'44xxxxxxxxxx'}, 
  {u'src': u'44xxxxxxxxx', u'billed_duration': u'20.4000000', u'call_duration': u'20.5333333', 
  u'ts': u'2017-02-07T11:43:04Z', u'sid': u'xxxxxxx', u'type': u'call-in', u'dst': u'44xxxxxxxxxx'}, 
  {u'src': u'44xxxxxxxxx', u'billed_duration': u'0.0000000', u'call_duration': u'0.4000000', 
  u'ts': u'2017-02-07T11:38:30Z', u'sid': u'xxxxxxx', u'type': u'call-in', u'dst': u'44xxxxxxxxxx'}, 
  {u'src': u'44xxxxxxxxx', u'billed_duration': u'0.0000000', u'call_duration': u'0.4833333', 
  u'ts': u'2017-02-07T11:34:29Z', u'sid': u'xxxxxxx', u'type': u'call-in', u'dst': u'44xxxxxxxxxx'}]

```

---
<a name="endpoints"/>
## End Points

The end points API allows you to create and manage end points for your account.
> https://zironuk.atlassian.net/wiki/display/docs/Endpoints+API

**Import:**
```python
>>> from ziron import EndPoints
>>> endPoints = EndPoints(sid, auth_token)
```

<a name="createEndpoint"/>
### createEndpoint(*type*, *uri*, *description*, *default*)

Create an endpoint.
> https://zironuk.atlassian.net/wiki/display/docs/Create+Endpoint

**Arguments:**
* Required:
  * type - Type of endpoint, valid options are returned from [Get Endpoint Types](#getEndpointTypes)
  * uri - URI for this endpoint
* Optional:
  * description - A user defined description for this endpoint
  * default - Make this endpoint the default for all new numbers

**Examples:**

```python
>>> endPoints.createEndpoint('sms','test','testing',0)
{u'description': u'testing', u'created': u'2017-02-07 16:13:10', u'uri': u'test', 
 u'modified': u'0000-00-00 00:00:00', u'is_default': u'0', u'sid': u'EPd585a551e7239c3a5fbc293b4a0fe900', 
 u'type': u'sms'}
```

<a name="deleteEndpoint"/>
### deleteEndpoint(*sid*)

The deleteEndpoint command deletes an endpoint from your account.
> https://zironuk.atlassian.net/wiki/display/docs/Delete+Endpoint

**Arguments**
* Required:
  * sid - sid of the created endpoint, use getEndpoints to find the sid.
* Optional: None

**Examples**

```python

>>> endPoints.getIndividualEnpoints('EPd585a551e7239c3a5fbc293b4a0fe900')
{u'description': u'testing', u'created': u'2017-02-07 16:13:10', u'uri': u'test', 
u'modified': u'0000-00-00 00:00:00', u'is_default': u'0', u'sid': u'EPd585a551e7239c3a5fbc293b4a0fe900', 
u'type': u'sms'}

>>> endPoints.deleteEndpoint('EPd585a551e7239c3a5fbc293b4a0fe900')
<response 204>

>>> endPoints.getIndividualEnpoints('EPd585a551e7239c3a5fbc293b4a0fe900')
<Response 404>
```

<a name="getEndpoints"/>
### getEndpoints(*limit*, *start*, *end*)

The getEnpoints commande retrieves a list of created endpoints.
> https://zironuk.atlassian.net/wiki/display/docs/Get+Endpoints

**Arguments**
* Required: None
* Optional: 
  * limit - Either 1 -100 or "all", limits the number of endpoints returned.
  * start - Datetime in the form YYYY-MM-DD HH-MM-SS to signify the start of the daterange you wish to return.
  * end - Datetime in the form YYYY-MM-DD HH-MM-SS to signify the end of the daterange you wish to return.

**Examples**

```python
>>> endPoints.getEndpoints()
[{u'description': u'VOICE', u'created': u'2016-07-27 10:15:13', u'uri': u'xxxxxxx', 
  u'modified': u'2016-07-27 18:40:01', u'is_default': u'1', u'sid': u'xxxxxxx', u'type': u'voice'}, 
  {u'description': u'SMS', u'created': u'2016-07-27 10:16:12', u'uri': u'xxxxxxx', 
  u'modified': u'2016-07-27 11:01:01', u'is_default': u'1', u'sid': u'xxxxxxxxx', u'type': u'sms'}]

>>> print endPoints.getEndpoints(start="2016-07-27 10:00:00", end="2016-07-27 11:00:00
[{u'description': u'VOICE', u'created': u'2016-07-27 10:15:13', u'uri': u'xxxxxxx', 
  u'modified': u'2016-07-27 18:40:01', u'is_default': u'1', u'sid': u'xxxxxxx', u'type': u'voice'}]
```

<a name="getEndpointTypes"/>
### getEnpointTypes()

The getEndpointTypes command returns a list of valid endpoints.
> https://zironuk.atlassian.net/wiki/display/docs/Get+Endpoint+Types

**Arguments**
* Required: None
* Optional: None

**Examples:**
```python
>>> endPoints.getEndpointTypes()
[{u'type': u'voice', u'description': u'Voice'}, {u'type': u'sms', u'description': u'SMS'}, 
 {u'type': u'mms', u'description': u'MMS'}, {u'type': u'fax', u'description': u'Fax'}]
```

<a name="getIndividualEndpoint"/>
### getIndividualEndpoints(*sid*)

The getIndividualEndpoint command returns information on a single endpoint.
> https://zironuk.atlassian.net/wiki/display/docs/Get+Individual+Endpoint

**Arguments:**
* Required: 
  * sid - The unique sid for the endpoint you wish to retrieve information for.
* Optional:
  * key - Individual value from dictionary.

**Examples:**

```python
>>> endPoints.getIndividualEnpoints('EPd585a551e7239c3a5fbc293b4a0fe900')
{u'description': u'testing', u'created': u'2017-02-07 16:13:10', u'uri': u'test',
u'modified': u'0000-00-00 00:00:00', u'is_default': u'0', u'sid': u'EPd585a551e7239c3a5fbc293b4a0fe900',
u'type': u'sms'}

>>> endPoints..getIndividualEndpoint('EPd585a551e7239c3a5fbc293b4a0fe900', 'description')
u'testing'
```

<a name="updateIndividualEndpoint"/>
### updateIndividualEndpoint(*sid*, *type*, *uri*, *description*, *default*)

The updateIndividualEndpoint command lets you update individual fields for an endpoint.
> https://zironuk.atlassian.net/wiki/display/docs/Update+Individual+Endpoint

**Arguments:**
* Required:
  * sid - The unique sid for the endpoint you wish to edit.
* Optional:
  * type - Change Endpoint type
  * uri - Change URI of endpoint
  * description - Change description of endpoint
  * default - Change whether the endpoint is the default

**Examples:**

```python
>>> endPoints.getIndividualEnpoints('EPd585a551e7239c3a5fbc293b4a0fe900')
{u'description': u'testing', u'created': u'2017-02-07 16:13:10', u'uri': u'test',
u'modified': u'0000-00-00 00:00:00', u'is_default': u'0', u'sid': u'EPd585a551e7239c3a5fbc293b4a0fe900',
u'type': u'sms'}

>>> endPoints.updateIndividualEndpoints('EPd585a551e7239c3a5fbc293b4a0fe900', description="A different description")
{u'description': u'A different description', u'created': u'2017-02-07 16:13:10', u'uri': u'test', 
u'modified': u'2017-02-07 17:03:30', u'is_default': u'0', u'sid': u'EPd585a551e7239c3a5fbc293b4a0fe900', 
u'type': u'sms'}
```

---
<a name="messages"/>
## Messages

The Messages API allows you to send messages and retrieve details of existing messages, 
including delivery reports.
> https://zironuk.atlassian.net/wiki/display/docs/Messages+API

**Import:**
```python
>>> from ziron import Messages
>>> messages = Messages(sid, auth_token)
```
<a name="sendMessage"/>
### sendMessage(*src*, *dest*, *data*, *message_type*, *mclass*, *mwi*, *callback_url*)

Send a message to one or more recipients. Returns an unpaginated list of message details.
> https://zironuk.atlassian.net/wiki/display/docs/Send+a+Message

**Arguments:**
* Required:
  * src - Source number or name.
  * dest - Destination number.
  * data - Message body.
* Optional:
  * message_type - Type of message, defaults to 'sms'
  * mclass - Sets the message class in the DCS field (SMS only), 0-3, 
    i.e. 0 (flash SMS), 1 (mobile), 2 (SIM), 3 (SIM toolkit).
  * mwi - Activate/deactivate the message waiting indicator (SMS only), 0-7, 
    i.e. 0 (activate voicemail), 1 (activate fax), 2 (activate email), 
    3 (activate other), 4 (deactivate voicemail), 5 (deactivate fax), 
    6 (deactivate email), 7 (deactivate other).
  * callback_url - URL to receive message status callbacks.

**Examples:**

```python
>>> messages.sendMessage("44xxxxxxxxxx", "44xxxxxxxxxx", "Testing")
[{u'status': u'queued', u'src': u'44xxxxxxxxxx', u'data': u'Testing', 
  u'dst': u'44xxxxxxxxxx', u'charset': None, u'ts': u'2017-02-08T10:50:32Z', 
  u'parts': u'1', u'sid': u'SMb2887b44ddda90ebdfb51e6331435abf', u'type': u'sms-out'}]
```
  
<a name="getMessages"/>
### getMessages(*limit*, *start*, *end*)

#### Needs redoing

The getMessages command returns a list of messages.
> https://zironuk.atlassian.net/wiki/display/docs/Get+Messages

**Arguments:**
* Required: None
* Optional: 
  * limit - Either 1-100 or "all", limit the number number of results returned, 
            if all return all CDRs ever.
  * start - Datetime in the form YYYY-MM-DD HH-MM-SS to signify the start of 
            the daterange you wish to return.
  * end - Datetime in the form YYYY-MM-DD HH-MM-SS to signify the end of the daterange 
          you wish to return.

**Examples:**

```python

```

<a name="getIndividualMessage"/>
### getIndividualMessage(*sid*, *key*)

Return information on an individual message.
> https://zironuk.atlassian.net/wiki/display/docs/Get+an+Individual+Message

**Arguments:**

* Required: 
  * sid - Unique ID for the message you wish to retrieve the information on.
* Optional:
  * key - Return an individual value from the dictionary.

**Examples:**

```python
>>> messages.getIndividualMessage("SMb2887b44ddda90ebdfb51e6331435abf")
{u'status': u'delivered', u'src': u'447599440428', u'data': u'Testing', u'dst': u'447599440428', u'charset': None, u'ts': u'2017-02-08T10:50:32Z', u'parts': u'1', u'sid': u'SMb2887b44ddda90ebdfb51e6331435abf', u'type': u'sms-out'}

>>> messages.getIndividualMessage("SMb2887b44ddda90ebdfb51e6331435abf", "data")
u'Testing'
```

<a name="getMessageHistory"/>
### getMessageHistory(*sid*)

Return a list of message statuses. SMS only.
> https://zironuk.atlassian.net/wiki/display/docs/Get+Message+History

**Arguments:** 

* Required:
  * sid - Unique ID for the message you wish to retrieve the message history for.
* Optional: None

**Examples:**

```python
>>> messages.getMessageHistory("SMb2887b44ddda90ebdfb51e6331435abf")
[{u'status': u'submitted', u'ts': u'2017-02-08T10:50:32Z'}, {u'status': u'delivered', u'ts': u'2017-02-08T10:50:33Z'}]
```

<a name="messageDeliveryStats"/>
### messageDeliveryStats()

Get a list of message statistics for the last 24 hours.
> https://zironuk.atlassian.net/wiki/display/docs/Message+Delivery+Statistics

**Arguments:**

* Required: None
* Optional: None

**Examples:**

```python
>>> messages.messageDeliveryStats()
[{u'status': u'delivered', u'count': u'6', u'percent': u'6.8182'}]
```

---
<a name="nrl"/>
## Number Range Lookups

The Lookups API allows you to use a range of Number Lookup services.
> https://zironuk.atlassian.net/wiki/display/docs/Lookups+API

**Import**:

```python 
>>> from ziron import NumberRangeLookups
>>> nrl = NumberRangeLookups(sid, auth_token)
```

<a name="HLRLookup"/>
### HLRLookup(*lookup_type*, *number*)

The HLR Lookup service allows you to query the mobile network for a range of subscriber  
information, and can be used for mobile number validation, porting  check, and  
roaming status.

> https://zironuk.atlassian.net/wiki/display/docs/HLR+Lookup

**Arguments:**

* Required:
  * lookup_type - Type of lookup to perform.  
    Valid values: get_country, hashed_imsi, home_network.
  * number - The number to lookup. E164 format.
* Optional: None

#### Note: *get_country and hashed_imsi are restricted by default*

**Examples:**

```python
>>> nlr.HLRLookup('home_network','44xxxxxxxxxx')
{u'status': u'success', u'network': u'Foo 3G', 
 u'sid': u'NLeaf71cd334b586f9cbc2d769165402e6', u'mcc': u'234', 
 u'number': u'44xxxxxxxxxx', u'mccmnc': u'234xx', u'country_iso': u'gb', u'mnc': u'xx'}
```

---
<a name="numbering"/>
## Numbering
---
<a name="payments"/>
## Payments
---
<a name="pricing"/>
## Pricing
---
<a name="resources"/>
## Resources
---
<a name="transactions"/>
## Transactions
---
<a name="trunks"/>
## Trunks
---

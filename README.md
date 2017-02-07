# Zironpy

# Contents

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
  * [Messages](#messages)
  * [Number Range Lookups](#nrl)
  * [Numbering](#numbering)
  * [Payments](#payments)
  * [Pricing](#pricing)
  * [Resources](#resources)
  * [Transactions](#transactions)
  * [Trunks](#trunks)

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
  * limit - Either 1-100 or all, limit the number number of results returned, if all return all CDRs ever.
  * start - Datetime in the form YYYY-MM-DD HH-MM-SS to signify the start of the daterange you wish to return.
  * end - Datetime in the form YYYY-MM-DD HH-MM-SS to signify the end of the daterange you wish to return.

**Examples**

```python
>>> print calls.getCalls(limit=1)
[{u'src': u'44xxxxxxxxxx', u'billed_duration': u'0.2333333', u'call_duration': u'0.2333333', 
  u'ts': u'2017-02-07T12:10:57Z', u'sid': u'xxxxxxx', u'type': u'call-in', u'dst': u'44xxxxxxxxxx'}]
>>> calls.getCalls(start="2017-02-07 12:00:00", end="2017-02-07 13:00:00")
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
---
<a name="messages"/>
## Messages
---
<a name="nrl"/>
## Number Range Lookups
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

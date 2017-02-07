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

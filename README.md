# LJWE Database

![Status](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Ffloating-headland-47828.herokuapp.com%2Fljwe%2F)
![Release](https://img.shields.io/github/v/release/leowotzak/ljwe-db)
![Repo Size](https://img.shields.io/github/repo-size/leowotzak/ljwe-db)
![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

**LJWE** website backend built with **Python** & **Django** and supports users as well as a financial assets **REST API**[^1].

The _**Securities Master**_ database comes with a collection of scripts that insert and update new data into the database. They utilize **Django**'s built-in ORM and migration system to track revisions to database schema and **pandas** to extract, transform, & load data.

[^1]: Data sourced from [Alpha Vantage](https://www.alphavantage.co/)

## REST API Endpoints

---

<!-- cSpell: disable -->
### Symbols

*Stores visitor information and sends an email to myself notifying me of a new message*

* **URL**

  /symbol

* **Method(s)**

  * `GET`

* **Params**
  * `symbol_id=[integer]`
  * `freq=[string]`

* **Success Response:**

  * **Code:** 202 ACCEPTED \
    **Content:** `{ body : "Message sent!" }`

* **Error Response:**

  * **Code:** 400 BAD REQUEST \
    **Content:**
    `{ firstname : "Firstname Invalid", lastname: "Lastname Invalid", email: "Email Invalid", message: "Message Invalid" }`

* **Sample Call:**
```bash
  curl --location --request POST 'http://127.0.0.1:5000/contact' \
--form 'firstname="Jim"' \
--form 'lastname="Miller"' \
--form 'email="Jim.Miller@fakeemail.com"' \
--form 'message="Hi!"'
```

<!-- cSpell: enable -->

## Database

---

![database_schema](https://github.com/leowotzak/ljwe-db/blob/ccf29fb48593bba276bc69d258fe4e8f65ad9391/docs/ljwedb.png)

| Symbol Data | Interday Data | Intraday Data |
|----|----|----|
| symbol | daily | one minute |
|| weekly | five minute |
|| monthly | fifteen minute |
||| thirty minute |
||| sixty minute |

**retrieve.py:** Namespace of functions that retrieve and format data from alpha vantage

**update.py:** Namespace of functions that update the Database

# Cordless Challenge

This is my submission for the [Cordless Challenge](https://www.notion.so/Cordless-IVR-challenge-7a654adac6be465ca2b5689abb3af914).

## Tech Stack

- Python
- Flask
- Pipenv (for dependency management)

## Installation

To get started, create a duplicate `.env.example` and name it `.env`. Once you're done, follow the instructions below:

* Ensure you have [python 3.8+](https://www.python.org/) and [pipenv](https://pypi.org/project/pipenv/) installed

* Create a virtual environment with the command `pipenv shell --python=python3`

* Install the dependencies with the command `pipenv install`

* Start the application wit hhe command `make start`

### Endpoints

*/ivr*
This is the endpoint that connects to the Interactive Voice Response engine of the bank.

```http
  GET /ivr
```

| Parameter           | Type     | Description                                                    |
| :------------------ | :------- | :------------------------------------------------------------- |
| `phone_number_from` | `string` | **Required**. Customer's phone number                          |
| `digit`             | `number` | **Required**. number relating to command user wants to perform |
| `recording_url`     | `string` | **Optional**. Recording of customer's voicemail                |

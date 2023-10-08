# Newspaper Agency

This is a newspaper agency website which allows you to interact (read, add, edit, delete)
with news, redactors and topics.

## Check it out!

[Newspaper Agency deployed to Render.com](https://newspaper-agency-xel6.onrender.com/)

### Use this user to test the website
* **login**: superadminuser
* **password**: thehardestpasswordever

## Demo of home page
![img.png](img.png)

## Installing / Getting started

A quick introduction of the minimal setup you need to run it.
(Python should be already installed)

```shell
git clone https://github.com/MarianKovalyshyn/newspaper-agency.git
cd newspaper-agency/
python3 -m venv venv
source venv/bin/activate (MacOS)
venv\Scripts\activate (Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Features

* **Unauthorized** users can only read: list of news, redactors and topics
and their detail pages
* **Authorized** users can add, edit and delete news, redactors and topics

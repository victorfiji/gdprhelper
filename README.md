# Welcome to gdprhelper. :white_check_mark:
## gdprhelper sends GDPR data erasure- and access requests for you to an email of your choice.
### Now supporting 2 languages & loads of company contact mail presets.

How to use
---

* Make sure Python 3.8.2 is installed (get it from (python.org)[https://www.python.org/])
* Create a folder on your computer/laptop
* Put all the contents in the folder
* Open config.json and change the fields required (see below)
* cd into the folder (in cmd line: cd /dir/)
* Now run the python scrypt using python gdpr.py

_Didn't work? Have more questions? Contact me here:_

Discord: victorlean#4935

Session: 05cdeb365538a1d31b1c559f18eda821bb1d079c918acb3f0d63bcb4b755062d7b (getsession.org)[https://getsession.org/]

These are the variables you can/need to change inside the config file.
---

* `sender_email` - The email that will be used to send the email
* `sender_password` - The password to the email that will be used ot send the email
* `user_name` - Your full name or the name you used to sign up with at the site.
* `user_phone` - Your phone number or the number you used to sign up with at the site
* `user_email` - Your email address you used to sign up with at the site OR the one that identifys you.
* `language` - The language that your email will be sent in (refer below for all support languages)

Supported languages (set this in config.json) :u5272:
---
* english (default)
* nederlands
Want to see the emails that will be sent out? Refer to this [github resource](https://github.com/good-lly/gdpr-documents/tree/master/docs)


Support mail providers (set this in config.json) :computer:
---
### If you want to add your own mail provider, simply make a new json entry.

* gmail (default)
* aol
* apple
* inbox.com
* laposte
* mail.com
* ntlworld
* orangefr
* outlook
* t-online
* talktalk
* yahoo
* yandex
* zoho

About development
---

This is my first real Python (and any language for that matter) project. There probably will be bugs in the code and/or other issues, if there are be sure to contact me on Github or one of the contact options above. Any ideas or updates on how to make the code better are welcome and I am grateful for them.

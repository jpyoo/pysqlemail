# pysqlemail

This will allow you to run sql query and save data as csv files using python.
The csv files will be attached to your email report.

# Result:
Your data will be saved under Data folder.

and email will be sent attaching the data.
![Capture](https://user-images.githubusercontent.com/58375171/148623450-4ff05332-9661-475b-88ca-0ef62bb6f411.JPG)


# How to use:
use intall_requirements.bat to install required libraries.
your database credentials go in db.key

![image](https://user-images.githubusercontent.com/58375171/148623467-fdeef692-58d0-45fb-88d1-eaec17e77315.png)

your email info and attachment info should be in email_data.json
![image](https://user-images.githubusercontent.com/58375171/148623489-32887156-1a36-4e27-a704-1e6a07c7dd36.png)

Your Database name and query goes in modules/renew_report.py
![image](https://user-images.githubusercontent.com/58375171/148623535-6e719d39-db80-4fe0-a48b-ccf084c9132c.png)

Use jobs/email_report.bat to send email

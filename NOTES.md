
curl -X POST 'https://api.twilio.com/2010-04-01/Accounts/AC5404118426bc9d8f62ab9fdf2289d124/Messages.json' \
-u AC5404118426bc9d8f62ab9fdf2289d124:[AuthToken]

Test
AccountSID: AC8b23b04f7c23cf1428281356bcc2c8a9
AuthToken: e341271d87198c55fa6cc397d96fdf1a

Full
AccountSID: AC5404118426bc9d8f62ab9fdf2289d124
AuthToken:  64ac10aabd55d1002a9dec6b5df455ff

https://api.twilio.com/2010-04-01/Accounts/AC8b23b04f7c23cf1428281356bcc2c8a9/Messages
auth: 
    {
    user: "AC8b23b04f7c23cf1428281356bcc2c8a9",
    pass: "e341271d87198c55fa6cc397d96fdf1a"
    },         
form: 
    {
    From: "9517327866",             
    To: "9517327866",             
    Body: "test"         
    }


auth: 
    {
    user: AC5404118426bc9d8f62ab9fdf2289d124",
    pass: 64ac10aabd55d1002a9dec6b5df455ff"
    },         
form: 
    {
    From: "9517327866",             
    To: "9517327866",             
    Body: "test"         
    }


Dash Mac :  74:75:48:8a:4f:f0

https://api.twitter.com/1.1/statuses/update.json

tx
https://apps.twitter.com/app/6875827/show

Consumer Key (API Key) IxTqT2yeqKoE7FlDWQ4V6w1Mn
Consumer Secret (API Secret) cfVeZkHCIbdv0SRVPK2WzoPVRq3X2QsRkWbnZl2I90hvxLCW6u
Owner ID	274696817

Access Token	274696817-Rp8Ulbhi4Fsd8UYxNRfN0xNCEvoAql3sSDz9BTwS
Access Token Secret	jiUW61uCg2tZE63jZhQDqtsp5rUrssZgUDqKd209ipOAD
Access Level	Read-only
Owner	xmlking
Owner ID	274696817

---
sudo easy_install pip
sudo pip install requests
----

-----
Node-Dash-Button-Webtasks
===================

Simple demo showcasing IoT and Auto0's Webtask integration. 


```bash 
npm install wt-cli -g

wt create send_text.js --name send_text --secret TWILIO_ACCOUNT_SID=AC8b23b04f7c23cf1428281356bcc2c8a9 --secret TWILIO_AUTH_TOKEN=e341271d87198c55fa6cc397d96fdf1a --secret TWILIO_NUMBER:+15005550006



wt create send_text.js --name send_text -TWILIO_ACCOUNT_SID=AC8b23b04f7c23cf1428281356bcc2c8a9 -TWILIO_AUTH_TOKEN=e341271d87198c55fa6cc397d96fdf1a -TNUMBER=+15005550006

wt create send_text.js --name send_text --secret TWILIO_ACCOUNT_SID=AC8b23b04f7c23cf1428281356bcc2c8a9 -s TWILIO_AUTH_TOKEN=e341271d87198c55fa6cc397d96fdf1a -s TWILIO_NUMBER=+15005550006


wt create send_text.js --name send_text -s —TWILIO_ACCOUNT_SID=AC8b23b04f7c23cf1428281356bcc2c8a9 —TWILIO_AUTH_TOKEN=e341271d87198c55fa6cc397d96fdf1a -TWILIO_NUMBER=+15005550006


curl https://webtask.it.auth0.com/api/run/wt-xmlking+github-gmail_com-0/send_text?webtask_no_cache=1&TWILIO_ACCOUNT_SID=AC8b23b04f7c23cf1428281356bcc2c8a9&TWILIO_AUTH_TOKEN=e341271d87198c55fa6cc397d96fdf1a&TWILIO_NUMBER=+15005550006
 
sudo python run.py
```
-----
Node-Dash-Button-Webtasks
===================

Simple demo showcasing IoT and **webtask** integration. 

[Amazon Dash Button](www.amazon.com/oc/dash-button) triggers [webtask](https://webtask.io/) to send text message when button is pressed.

```bash 
npm install wt-cli -g

wt create send_text.js --name send_text -s TWILIO_ACCOUNT_SID=AC8b23b04f7c23cf1428281356bcc2c8a9 -s TWILIO_AUTH_TOKEN=e341271d87198c55fa6cc397d96fdf1a -s TWILIO_NUMBER=+15005550006
 
sudo python run.py
```
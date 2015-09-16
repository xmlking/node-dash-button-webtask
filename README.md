Node-Dash-Button-Webtasks
===================

Simple demo showcasing IoT and **webtask** integration. 

[Amazon Dash Button](www.amazon.com/oc/dash-button) triggers [webtask](https://webtask.io/) to send text message when button is pressed.

```bash 
npm install wt-cli -g

wt create send_text.js --name send_text -s TWILIO_ACCOUNT_SID=aaa -s TWILIO_AUTH_TOKEN=aaa -s TWILIO_NUMBER=+15005550006
 
sudo python run.py
```


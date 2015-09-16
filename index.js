// Twilio Credentials
var accountSid = 'AC8b23b04f7c23cf1428281356bcc2c8a9';
var authToken = 'e341271d87198c55fa6cc397d96fdf1a';

//require the Twilio module and create a REST client
var client = require('twilio')(accountSid, authToken);

client.messages.create({
    to: "+19513677933",
    from: "+15005550006",
    body: "test123"
}, function(error, message) {
    if (!error) {
        console.log('Success! The SID for this SMS message is:');
        console.log(message.sid);

        console.log('Message sent on:');
        console.log(message.dateCreated);
    } else {
        console.log('Oops! There was an error.',error);
    }
});
const Alexa = require('alexa-sdk');

exports.handler = function(event, context, callback){
    const alexa = Alexa.handler(event, context, callback);
    alexa.appId = 'd1ad2752-b418-4fa8-811f-f86ebaf41f08';
    alexa.registerHandlers(handlers);
    alexa.execute();
}

const handlers = {
    'HelloWorldIntent' : function() {
        //emit response directly
        this.emit(':tell', 'Hello World!');
    }
};
var Twitter = require('twitter'); //twitter package
var config = require('./config.js');

var T = new Twitter(config);

var params = {
    q: //handle,
    count: 200,
    //result_type: 'recent',
    lang: 'en'
}

T.get('statuses/user_timeline', params, function(err, data, response) {
    if(!err) {
        return data;
        }
    } else {
        return err;
    }
});
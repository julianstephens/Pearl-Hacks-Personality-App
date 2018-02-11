var Twitter = require('twitter'); //twitter package
var config = require('./config.js');

var tweetData = {};
var key = 'contentItems';
tweetData[key] = [];

var T = new Twitter(config);

var params = {
    screen_name: 'realDonaldTrump',
    count: 3200,
    lang: 'en'
}


for (var i = 1; i <= 16; i++) {
    params.page = i;
    T.get ('statuses/user_timeline', params, function(err, data, response) {
        if(!err) {
           // console.log(data);


            data.forEach(function (tweet) {
                var tempData = {
                "contenttype": "text/plain",
                "language": "en"
                };

                if (typeof tweet.retweeted_status === 'undefined') {
                    //if original tweet
                    tempData.content = tweet.text;
                    //tempData.id = tweet.id;
                } else {
                    //if retweet
                    tempData.content = tweet.retweeted_status.text;
                    //tempData.id = tweet.retweeted_status.id;
                }
                tweetData[key].push(tempData);
            });
        } else {
            return err;
        }

        //console.log(tweetData);

    }); //get
}  //for loop






// var PersonalityInsightsV3 = require('watson-developer-cloud/personality-insights/v3');

// var personalityInsights = new PersonalityInsightsV3({
//   username: 'a1e78119-98e6-4c30-a6f2-8529024c5e72',
//   password: 'cdX0Oz3yUD3C',
//   version_date: '2018-2-10',
//   url: 'https://gateway.watsonplatform.net/personality-insights/api'
// });

// personalityInsights.profile(
//   {
//     content: data,
//     content_type: 'text/plain',
//     consumption_preferences: true
//   },
//   function(err, response) {
//     if (err) {
//       console.log('error:', err);
//     } else {
//       return JSON.stringify(response, null, 2);
//     }
//   }
// );
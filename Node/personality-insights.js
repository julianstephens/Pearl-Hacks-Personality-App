

function getHandle(handle){

}









var PersonalityInsightsV3 = require('watson-developer-cloud/personality-insights/v3');

var personalityInsights = new PersonalityInsightsV3({
  username: 'a1e78119-98e6-4c30-a6f2-8529024c5e72',
  password: 'cdX0Oz3yUD3C',
  version_date: '2018-2-10',
  url: 'https://gateway.watsonplatform.net/personality-insights/api'
});

personalityInsights.profile(
  {
    content: 'Enter more than 100 unique words here...',
    content_type: 'text/plain',
    consumption_preferences: true
  },
  function(err, response) {
    if (err) {
      console.log('error:', err);
    } else {
      console.log(JSON.stringify(response, null, 2));
    }
  }
);

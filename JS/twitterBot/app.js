const secret = require('./secret_keys.js');
/*Array containing:
* consumer key, consumer secret,
* access token key, and access token secret.
* All are given by twitter and must be acquired at:
* apps.twitter.com*/
const TwitterPackage = require('twitter');

let Twitter = new TwitterPackage(secret);

let query = "alot";

Twitter.get('search/tweets', {q: query, count: 5, lang:"en"}, function(error, tweets) {
   let tweet_list = tweets['statuses'];
   console.log(tweet_list.length);

       for (let i = 0; i < tweet_list.length; i++) {
           function forLoop() {
               setTimeout(function(){
               let screen_name = tweet_list[i].user.screen_name;
               let message = "@" + screen_name + " Alot confused, a lot not understand feelings";
               let tweet_id = tweet_list[i].id_str;

               try {
                   Twitter.post('statuses/update', {
                       "status": message,
                       "in_reply_to_status_id": tweet_id
                   }, function () {
                       console.log("Tweet posted successfully!")
                   });
               }

               catch (err) {
                   console.log(err);
               }
               }, 3000*i);
           }
           forLoop();
       }

});


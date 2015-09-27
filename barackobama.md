**Request**: `http://otter.topsy.com/authorinfo.txt?url=http%3A%2F%2Ftwitter.com%2Fbarackobama&apikey=<your_apikey>`

**Response**: The TXT response is shown below. Other [response formats](ResponseFormats.md) are also available.

```
### FOR DEBUG ONLY ###
$VAR1 = {
          'request' => {
                         'resource' => 'authorinfo',
                         'response_type' => 'txt',
                         'parameters' => {
                                           'url' => 'http://twitter.com/barackobama'
                                         },
                         'url' => 'http://otter.topsy.com/authorinfo.txt?url=http%3A%2F%2Ftwitter.com%2Fbarackobama'
                       },
          'response' => {
                          'name' => 'Barack Obama',
                          'nick' => 'barackobama',
                          'description' => 'This account is run by #Obama2012 campaign staff. Tweets from the President are signed -bo.',
                          'influence_level' => 10,
                          'url' => 'http://twitter.com/barackobama',
                          'image_url' => 'http://a0.twimg.com/profile_images/2824616796/2d3383532bbc7bcc28f7a07e69cfe25e_normal.png',
                          'type' => 'twitter',
                          'topsy_author_url' => 'http://topsy.com/twitter/barackobama'
                        }
        };
```
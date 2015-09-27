## /top ##

**Description:** A feed of Top 100, 1K, 5K and 20K links, photos, tweets & videos posted on the social web everyday.

**URL Format:** `http://otter.topsy.com/top.json?query=parameters`

### Parameters: ###

| **Name**   | **Required** | **Description** |
|:-----------|:-------------|:----------------|
| thresh     | required     | top100, top1k, top5k, top20k |
| type       | optional     | defaults to everything. Other values: image, video, tweet |
| allow\_lang | optional     | defaults to all.  Other values:  en, ja, kr, de, pt, es, th, fr |

Accepts [List Parameters](ResListParameters.md)

This method returns a feed of Top 100, or 1K (1000), 5K (5000), 20K (20,000) items posted on Twitter everyday.  The list is computed using a predictive algorithm, which dynamically adjusts ranking criteria to determine the threshold number of items everyday.  You can select a particular threshold with the `thresh` parameter.

When `type` is not specified, the list includes all types of items.  There are independent lists for type image, video and tweet, that can be accessed with the `type` parameter.

Several langauges are supported by /top, described in the table above.

### Example: ###

Fetch the Top 100 tweets in English.

```
$ curl -i "http://otter.topsy.com/top.json?thresh=top100&type=tweet&allow_lang=en"

HTTP/1.1 200 OK
Cache-Control: max-age=5
Content-Type: application/json; charset=utf-8
Expires: Wed, 23 Mar 2011 01:51:17 GMT
Last-Modified: Wed, 23 Mar 2011 01:51:12 GMT
Server: lighttpd/1.4.26
Content-Length: 8440
Date: Wed, 23 Mar 2011 01:51:13 GMT
X-Varnish: 1488685665
Age: 0
Via: 1.1 varnish
X-Served-By: ps391
X-Cache: MISS
Connection: close

{
   "request" : {
      "resource" : "top",
      "response_type" : "json",
      "parameters" : {
         "allow_lang" : "en",
         "type" : "tweet",
         "thresh" : "top100"
      },
      "url" : "http://otter.topsy.com/top.json?allow_lang=en&thresh=top100&type=tweet"
   },
   "response" : {
      "page" : 1,
      "total" : 500,
      "perpage" : 10,
      "last_offset" : 14,
      "hidden" : 1,
      "thresh" : "top100",
      "list" : [
         {
            "author_url" : "http://twitter.com/idothat2",
            "date" : 1300844963,
            "author_img" : "http://a1.twimg.com/profile_images/1246614074/idothattoo_normal.png",
            "content" : "RT @IDoThat2: Make a fist with your left hand, squeeze your left thumb, then put your right index finger down your throat. NO GAG REFLEX.",
            "date_alpha" : "41 seconds ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/idothat2/status/50368320272220160?utm_source=otter",
               "url" : "http://twitter.com/idothat2/status/50368320272220160",
               "mytype" : "tweet",
               "title" : "Make a fist with your left hand, squeeze your left thumb, then put your right index finger down your throat. NO GAG REFLEX.",
               "trackback_total" : 445
            },
            "author_nick" : "idothat2",
            "firstpost_date" : 1300843743,
            "topsy_author_url" : "http://topsy.com/twitter/idothat2?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/quixotic",
            "date" : 1300844892,
            "author_img" : "http://a0.twimg.com/profile_images/14300972/pic_mgmt_rhoffman_100x100_normal.gif",
            "content" : "RT @quixotic: Here&#39;s the 10 rules of massive entrepreneurship that I covered at SXSW.  http://lnkd.in/BfdBkT",
            "date_alpha" : "2 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/quixotic/status/50369753562357761?utm_source=otter",
               "url" : "http://twitter.com/quixotic/status/50369753562357761",
               "mytype" : "tweet",
               "title" : "Here&#39;s the 10 rules of massive entrepreneurship that I covered at SXSW.  http://lnkd.in/BfdBkT",
               "trackback_total" : 17
            },
            "author_nick" : "quixotic",
            "firstpost_date" : 1300844076,
            "topsy_author_url" : "http://topsy.com/twitter/quixotic?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/niw",
            "date" : 1300844714,
            "author_img" : "http://a0.twimg.com/profile_images/1255264346/discover_normal.jpg",
            "content" : "RT @niw: Mac OS Xでどうぞ→ $ say &quot;tahno see nurcomer gah popopo-poooon\\!&quot;",
            "date_alpha" : "5 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/niw/status/50293712605036544?utm_source=otter",
               "url" : "http://twitter.com/niw/status/50293712605036544",
               "mytype" : "tweet",
               "title" : "Mac OS Xでどうぞ→ $ say &quot;tahno see nurcomer gah popopo-poooon\\!&quot;",
               "trackback_total" : 21
            },
            "author_nick" : "niw",
            "firstpost_date" : 1300826225,
            "topsy_author_url" : "http://topsy.com/twitter/niw?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/herbcaen",
            "date" : 1300844451,
            "author_img" : "http://a3.twimg.com/profile_images/843522902/herb1_normal.jpg",
            "content" : "RT @HerbCaen: Caress each Spanish syllable. Don&#39;t say &quot;Frisco.&quot; Don&#39;t say &quot;San-Fran-Cis-Co.&quot; That&#39;s how tourists pronounce it. It&#39;s &quot;SanfrnSISco.&quot;",
            "date_alpha" : "9 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/herbcaen/status/50302206058053632?utm_source=otter",
               "url" : "http://twitter.com/herbcaen/status/50302206058053632",
               "mytype" : "tweet",
               "title" : "Caress each Spanish syllable. Don&#39;t say &quot;Frisco.&quot; Don&#39;t say &quot;San-Fran-Cis-Co.&quot; That&#39;s how tourists pronounce it. It&#39;s &quot;SanfrnSISco.&quot;",
               "trackback_total" : 23
            },
            "author_nick" : "herbcaen",
            "firstpost_date" : 1300827990,
            "topsy_author_url" : "http://topsy.com/twitter/herbcaen?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/ajelive",
            "date" : 1300844327,
            "author_img" : "http://a3.twimg.com/profile_images/955686894/AJE_TWITTER_ICON_normal.jpg",
            "content" : "RT @AJELive: Reports of at least 4 people killed in the #Syrian city of #Daraa, where residents say electricity has been cut off: http://aje.me/hBUe4g",
            "date_alpha" : "11 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/ajelive/status/50368232003084288?utm_source=otter",
               "url" : "http://twitter.com/ajelive/status/50368232003084288",
               "mytype" : "tweet",
               "title" : "Reports of at least 4 people killed in the #Syrian city of #Daraa, where residents say electricity has been cut off: http://aje.me/hBUe4g",
               "trackback_total" : 36
            },
            "author_nick" : "ajelive",
            "firstpost_date" : 1300843708,
            "topsy_author_url" : "http://topsy.com/twitter/ajelive?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/thinkprogress",
            "date" : 1300844316,
            "author_img" : "http://a1.twimg.com/profile_images/1256047404/TP_normal.gif",
            "content" : "RT @thinkprogress: NEW POLL: Just 7% of Americans view the federal deficit as the most important problem facing U.S. today http://thkpr.gs/ecU4DU",
            "date_alpha" : "11 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/thinkprogress/status/50362164892008449?utm_source=otter",
               "url" : "http://twitter.com/thinkprogress/status/50362164892008449",
               "mytype" : "tweet",
               "title" : "NEW POLL: Just 7% of Americans view the federal deficit as the most important problem facing U.S. today http://thkpr.gs/ecU4DU",
               "trackback_total" : 43
            },
            "author_nick" : "thinkprogress",
            "firstpost_date" : 1300842264,
            "topsy_author_url" : "http://topsy.com/twitter/thinkprogress?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/mohammad_syria",
            "date" : 1300844280,
            "author_img" : "http://a2.twimg.com/profile_images/1133769021/RWR_normal.png",
            "content" : "RT @Mohammad_Syria: Confirmed: Eyewitnesses: 6 dead bodies inside #Omari mosque right now as army committed a massacre in #Daraa #Syria #mar15",
            "date_alpha" : "12 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/mohammad_syria/status/50359652470362112?utm_source=otter",
               "url" : "http://twitter.com/mohammad_syria/status/50359652470362112",
               "mytype" : "tweet",
               "title" : "Confirmed: Eyewitnesses: 6 dead bodies inside #Omari mosque right now as army committed a massacre in #Daraa #Syria #mar15",
               "trackback_total" : 25
            },
            "author_nick" : "mohammad_syria",
            "firstpost_date" : 1300841681,
            "topsy_author_url" : "http://topsy.com/twitter/mohammad_syria?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/inhabitat",
            "date" : 1300844109,
            "author_img" : "http://a3.twimg.com/profile_images/51865670/OwliMcOwl_normal.jpg",
            "content" : "RT @inhabitat: California just launched a new energy upgrade program that can qualify residents for thousands of dollars in rebates! http://bit.ly/hGsnHc",
            "date_alpha" : "15 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/inhabitat/status/50318962348654592?utm_source=otter",
               "url" : "http://twitter.com/inhabitat/status/50318962348654592",
               "mytype" : "tweet",
               "title" : "California just launched a new energy upgrade program that can qualify residents for thousands of dollars in rebates! http://bit.ly/hGsnHc",
               "trackback_total" : 10
            },
            "author_nick" : "inhabitat",
            "firstpost_date" : 1300832116,
            "topsy_author_url" : "http://topsy.com/twitter/inhabitat?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/webseriestoday",
            "date" : 1300843994,
            "author_img" : "http://a1.twimg.com/profile_images/789016827/wst_100_normal.gif",
            "content" : "RT @webseriestoday: A First: Interactive Film with Augmented Reality: ..It’s then their job to track down the victim, fin... http://bit.ly/fbpmOS #webseries",
            "date_alpha" : "17 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/webseriestoday/status/50327403851022336?utm_source=otter",
               "url" : "http://twitter.com/webseriestoday/status/50327403851022336",
               "mytype" : "tweet",
               "title" : "A First: Interactive Film with Augmented Reality: ..It’s then their job to track down the victim, fin... http://bit.ly/fbpmOS #webseries",
               "trackback_total" : 17
            },
            "author_nick" : "webseriestoday",
            "firstpost_date" : 1300835145,
            "topsy_author_url" : "http://topsy.com/twitter/webseriestoday?utm_source=otter"
         },
         {
            "author_url" : "http://twitter.com/impolitical",
            "date" : 1300843992,
            "author_img" : "http://a0.twimg.com/profile_images/653297476/Twitter_avatar_grn_normal.jpg",
            "content" : "RT @impolitical: Hebert: Budget &quot;was not designed to restore peace in the 40th Parliament.&quot; http://ow.ly/4kcb2 #cdnpoli",
            "date_alpha" : "17 minutes ago",
            "target" : {
               "topsy_trackback_url" : "http://topsy.com/twitter.com/impolitical/status/50330927347404802?utm_source=otter",
               "url" : "http://twitter.com/impolitical/status/50330927347404802",
               "mytype" : "tweet",
               "title" : "Hebert: Budget &quot;was not designed to restore peace in the 40th Parliament.&quot; http://ow.ly/4kcb2 #cdnpoli",
               "trackback_total" : 6
            },
            "author_nick" : "impolitical",
            "firstpost_date" : 1300834843,
            "topsy_author_url" : "http://topsy.com/twitter/impolitical?utm_source=otter"
         }
      ],
      "offset" : 0
   }
}

```

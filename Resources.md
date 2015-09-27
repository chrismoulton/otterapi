

# The Otter URI #

The api is accessible via the uri: http://otter.topsy.com/

# Request Syntax #

All requests are implemented via HTTP GET calls. The url of the request
can be broken down into three parts: [Resources (described below)](Resources.md),
[response format](ResponseFormats.md), and query parameters. A malformed
request will return a response with HTTP 400 status.

> `GET /`[resource](Resources.md)`.`[response-format](ResponseFormats.md)`?keys=values HTTP/1.1`<br>
<blockquote><code>Host: otter.topsy.com</code></blockquote>

<h2>apikey</h2>

All requests accept the API key via the <code>apikey</code> parameter.<br>
<br>
<blockquote><code>GET /</code><a href='Resources.md'>resource</a><code>.</code><a href='ResponseFormats.md'>response-format</a><code>?apikey=KEY&amp;keys=values HTTP/1.1</code><br></blockquote>

<h1>Resources</h1>

<h2>/authorinfo</h2>

<b>Description:</b> Profile information for an author (a twitter profile<br>
indexed by Topsy). The response contains the name, description (biography) and<br>
the influence level of the author.<br>
<br>
<b>Explanation of Influence:</b> <a href='http://code.google.com/p/otterapi/wiki/Glossary'>TopsyGlossary</a>

<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>   </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> url           </td><td> required        </td><td> URL string for the author. </td></tr></tbody></table>

<h3>Example:</h3>

Fetch information about Barack Obama's Twitter profile.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/authorinfo.json?url=http://twitter.com/barackobama"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 03:57:16 GMT<br>
Content-Length: 587<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:02:16 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2468<br>
X-RateLimit-Reset: 1251345600<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "url" : "http://twitter.com/barackobama"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "authorinfo",<br>
      "url" : "http://otter.topsy.com/authorinfo.json?url=http%3A%2F%2Ftwitter.com%2Fbarackobama"<br>
   },<br>
   "response" : {<br>
      "name" : "Barack Obama",<br>
      "url" : "http://twitter.com/barackobama",<br>
      "type" : "twitter",<br>
      "nick" : "barackobama",<br>
      "description" : "44th President of the United States",<br>
      "topsy_author_url" : "http://topsy.com/twitter/barackobama",<br>
      "influence_level" : "5"<br>
   }<br>
}<br>
</code></pre>

<hr />

<h2>/experts</h2>

<b>Description:</b> List of authors that talk about the query. The list is<br>
sorted by frequency of posts and the influence of authors.<br>
(Note: for backwards compatibility, the /authorsearch api method is an alias to /experts.)<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>  </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> q            </td><td> required        </td><td> Search query string. (<a href='QuerySyntax.md'>query syntax</a>) </td></tr>
<tr><td> config_NoFilters </td><td> optional        </td><td> Setting this to 1, would turn off all other filters. Default value is 0. </td></tr></tbody></table>

Accepts <a href='ResListParameters.md'>List Parameters</a>

<h3>Example:</h3>

Fetch search results in json format for authors who talk about "nosql" the most.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/experts.json?q=nosql"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 04:13:46 GMT<br>
Content-Length: 7473<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:18:45 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2494<br>
X-RateLimit-Reset: 1251349200<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "q" : "nosql"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "experts",<br>
      "url" : "http://otter.topsy.com/experts.json?q=nosql"<br>
   },<br>
   "response" : {<br>
      "page" : 1,<br>
      "total" : "1139",<br>
      "perpage" : 15,<br>
      "list" : [<br>
         {<br>
            "name" : "nosql topsy 5",<br>
            "nick" : "nosql_topsy_5",<br>
            "photo_url" : "",<br>
            "description" : "",<br>
            "influence_level" : "1",<br>
            "hits" : 72,<br>
            "trackback_total" : 104,<br>
            "url" : "http://twitter.com/nosql_topsy_5",<br>
            "topsy_author_url" : "http://topsy.com/twitter/nosql_topsy_5"<br>
         },<br>
         ...<br>
      ]<br>
   }<br>
}<br>
</code></pre>

<hr />

<h2>/linkposts</h2>

<b>Description:</b> List of urls posted by an author.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>   </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> url           </td><td> required        </td><td> URL string for the author. </td></tr>
<tr><td> contains      </td><td> optional        </td><td> Query string to filter results. </td></tr>
<tr><td> tracktype     </td><td> optional        </td><td> Type of posts. Options include: <code>image</code>, <code>tweet__various</code> (tweets and retweets) and <code>self__tweet</code> (tweets by user). </td></tr>
<tr><td> sort_method   </td><td> optional        </td><td> the order in which to return results. Options are: date (default), -date, score. </td></tr></tbody></table>

Accepts <a href='ResListParameters.md'>List Parameters</a>

<h3>Example:</h3>

Fetch links in json format posted by Barack Obama.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/linkposts.json?url=http://twitter.com/barackobama"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 04:16:29 GMT<br>
Content-Length: 6247<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:21:29 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2492<br>
X-RateLimit-Reset: 1251349200<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "url" : "http://twitter.com/barackobama"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "linkposts",<br>
      "url" : "http://otter.topsy.com/linkposts.json?url=http%3A%2F%2Ftwitter.com%2Fbarackobama"<br>
   },<br>
   "response" : {<br>
      "page" : 1,<br>
      "total" : "288",<br>
      "perpage" : 10,<br>
      "list" : [<br>
         {<br>
            "permalink_url" : "http://twitter.com/barackobama/status/3569838653",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/tb/my.barackobama.com/page/community/post/obamaforamerica/gGMPVm",<br>
               "url" : "http://my.barackobama.com/page/community/post/obamaforamerica/gGMPVm",<br>
               "trackback_total" : "43"<br>
            },<br>
            "date" : "1251337427",<br>
            "content" : "Highlights from the tribute to Sen. Kennedy's life and <br>
                accomplishments from last year's Democratic National Convention: http://bit.ly/TJcyr",<br>
            "date_alpha" : "3 hours ago"<br>
         },<br>
         ...<br>
      ]<br>
   }<br>
}<br>
<br>
</code></pre>

<hr />

<h2>/linkpostcount</h2>

<b>Description:</b> Count of links posted by an author. This is the efficient,<br>
count-only version of /linkposts<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>   </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> url           </td><td> required        </td><td> URL string for the author. </td></tr>
<tr><td> contains      </td><td> optional        </td><td> A query filter for linkposts (the content must contain this string). </td></tr>
<tr><td> tracktype     </td><td> optional        </td><td> Type of posts. Options include: <code>tweet__various</code> (tweets and retweets) and <code>self__tweet</code> (tweets by user). </td></tr></tbody></table>

<h3>Example:</h3>

Fetch only the linkpost counts in json format that reference Topsy's Twitter account.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/linkpostcount.json?url=http://twitter.com/topsy"<br>
<br>
<br>
HTTP/1.1 200 OK<br>
Content-Length: 234<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Tue, 22 Sep 2009 13:51:10 -0700<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2490<br>
X-RateLimit-Reset: 1253653200<br>
Date: Tue, 22 Sep 2009 20:46:10 GMT<br>
<br>
{<br>
    "request" : {<br>
        "parameters" : {<br>
            "url" : "http://twitter.com/topsy"<br>
        },<br>
        "response_type" : "json",<br>
        "resource" : "linkpostcount",<br>
        "url" : "http://otter.topsy.com/linkpostcount.json?url=http%3A%2F%2Ftwitter.com%2Ftopsy"<br>
    },<br>
    "response" : {<br>
        "contains" : 0,<br>
        "all" : 46<br>
    }<br>
}<br>
<br>
</code></pre>

<hr />

<h2>/search</h2>

<b>Description:</b> List of results for a query.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>  </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> q            </td><td> required        </td><td> Search query string. (<a href='QuerySyntax.md'>query syntax</a>) </td></tr>
<tr><td> window       </td><td> optional        </td><td> Time window for results. (Options: <code>dynamic</code> - will pick the most relevant window. Possible responses are 1-23 hours or 1-100 days. (For example: h6 or d10). <code>h</code> last hour, <code>d</code> last day, <code>w</code> last week, <code>m</code> last month, <code>a</code> all time. (DEPRECATED: <code>auto</code> - automatically pick the most relevant window. This will return one of the standard h,d,w,m,a window values.).  </td></tr>
<tr><td> type         </td><td> optional        </td><td> The type of result.  Default is nothing, which includes all types.  Other supported values are <code>image</code>, <code>tweet</code> and <code>video</code></td></tr></tbody></table>

Accepts <a href='ResListParameters.md'>List Parameters</a>

<h3>Example:</h3>

Fetch search results in json format for the query "barack obama"<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/search.json?q=barack+obama&amp;window=dynamic"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 04:06:32 GMT<br>
Content-Length: 9097<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:11:31 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2498<br>
X-RateLimit-Reset: 1251349200<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "window" : "auto",<br>
         "q" : "barack obama"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "search",<br>
      "url" : "http://otter.topsy.com/search.json?q=barack+obama&amp;window=auto"<br>
   },<br>
   "response" : {<br>
      "window" : "d2",<br>
      "page" : 1,<br>
      "total" : "809",<br>
      "perpage" : 10,<br>
      "list" : [<br>
         {<br>
            "trackback_permalink" : "http://twitter.com/ewerickson/status/3562164195",<br>
            "hits" : 38,<br>
            "trackback_total" : 157,<br>
            "topsy_trackback_url" : "http://topsy.com/tb/www.redstate.com/erick/2009/08/26/breaking-rumors-surface-that-leon-panetta-is-resigning/",<br>
            "url" : "http://www.redstate.com/erick/2009/08/26/breaking-rumors-surface-that-leon-panetta-is-resigning/",<br>
            "content" : "Panetta is rumored to have sent a resignation letter to Barack Obama today:  http://bit.ly/CDMg9",<br>
            "title" : "BREAKING: Rumors Surface That Leon Panetta is Resigning - Erickâs blog - RedState",<br>
            "score" : 0.75521481,<br>
            "highlight" : "Panetta is rumored to have sent a resignation letter to <br>
                &lt;span class=\"highlight-term\"&gt;Barack&lt;/span&gt; &lt;span class=\"highlight-term\"&gt;Obama&lt;/span&gt; today:  http://bit.ly/CDMg9"<br>
         },<br>
         ...<br>
      ]<br>
   }<br>
}<br>
</code></pre>

<hr />

<h3>Example:</h3>

Fetch the most popular youtube videos today.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/search.json?q=site:youtube.com&amp;window=d"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 04:09:09 GMT<br>
Content-Length: 7086<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:14:09 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2496<br>
X-RateLimit-Reset: 1251349200<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "window" : "d",<br>
         "q" : "site:youtube.com"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "search",<br>
      "url" : "http://otter.topsy.com/search.json?q=site%3Ayoutube.com&amp;window=d"<br>
   },<br>
   "response" : {<br>
      "window" : "d",<br>
      "page" : 1,<br>
      "total" : "58258",<br>
      "perpage" : 10,<br>
      "list" : [<br>
         {<br>
            "trackback_permalink" : "http://twitter.com/danilogentili/status/3567528055",<br>
            "hits" : 2499,<br>
            "trackback_total" : 3450,<br>
            "topsy_trackback_url" : "http://topsy.com/trackback?url=http://www.youtube.com/watch?v=i_KPsH7f3xo",<br>
            "url" : "http://www.youtube.com/watch?v=i_KPsH7f3xo",<br>
            "content" : "ApÃ³s ver isso http://bit.ly/xOl3b, eu, Danilo Zentili, <br>
                peÃ§o perdÃ£o aos fÃ£s da Susxa que, como @Davis_Reimberg , sonhavam ser paquitas.",<br>
            "title" : "MEXEU COM A XUXA MEXEU COMIGO!!!",<br>
            "score" : 24.20444298,<br>
            "highlight" : "ApÃ³s ver isso http://bit.ly/xOl3b, eu, Danilo Zentili, <br>
                peÃ§o perdÃ£o aos fÃ£s da Susxa que, como @Davis_Reimberg , sonhavam ser paquitas."<br>
         },<br>
         ...<br>
      ]<br>
   }<br>
}<br>
</code></pre>

<hr />

<h2>/searchcount</h2>

<b>Description:</b> Count of results for a search query.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>   </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> q             </td><td> required        </td><td> Search query string. (<a href='QuerySyntax.md'>query syntax</a>) </td></tr>
<tr><td> dynamic       </td><td> optional        </td><td> If the value equals 1, the response will contain an extra window that is the best window for the given query. The possible responses are h1 through h23, or d1 through d100. These represent hourly or daily increments. NOTE: the output format of the response will change when this parameter is used. </td></tr></tbody></table>

<h3>Example:</h3>

Fetch only the search result counts in json format for a query of "Barack Obama".<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/searchcount.json?q=Barack+Obama"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 04:15:16 GMT<br>
Content-Length: 335<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:20:16 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2493<br>
X-RateLimit-Reset: 1251349200<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "q" : "Barack Obama"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "searchcount",<br>
      "url" : "http://otter.topsy.com/searchcount.json?q=Barack+Obama"<br>
   },<br>
   "response" : {<br>
      "w" : 2085,<br>
      "h" : 6,<br>
      "a" : 572027,<br>
      "d" : 330,<br>
      "m" : 9122<br>
   }<br>
}<br>
</code></pre>

<hr />

<h2>/searchhistogram</h2>

<b>Description:</b> The searchhistogram provides information to determine when a particular keyword peaked in the past days.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>   </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> q             </td><td> required        </td><td> Search query string. (<a href='QuerySyntax.md'>query syntax</a>) </td></tr>
<tr><td> slice         </td><td> optional        </td><td> The number of seconds for each slice. Defaults to 86400 (1 day) </td></tr>
<tr><td> period        </td><td> optional        </td><td> The number of slices.  Defaults to 30 (1 month) </td></tr>
<tr><td> count_method  </td><td> options         </td><td> This has two possible values, the default is "target" and the other possible value is "citation".  count_method specifies what is being counted, "target" means the number of unique links and "citation" means the number of unique tweets about links. </td></tr></tbody></table>

A searchhistorgram is a time-series of the number of distinct social media posts (tweets or links) that match a given query, over a defined time period. The granularity and the length of the time-series can be specified with the slice and period parameters.<br>
<br>
SearchHistograms have applications in analytics, trend detection, query freshness determination and social media monitoring. The <a href='http://analytics.topsy.com'>Topsy Analytics</a> application is built on this API call.<br>
<br>
SearchHistograms are generated from Topsy's real-time search index and are available ad-hoc for any query.  It should be noted that because the search index performs "sub-sampling", it underestimates counts for older time periods. In general, counts are accurate up to 3 months for most terms and up to 1 month for very popular terms (like iPhone and Justin Bieber).<br>
<br>
<h3>Example:</h3>

Fetch only the search result counts in json format for a query of "kindle".<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/searchhistogram.json?q=kindle"<br>
<br>
HTTP/1.1 200 OK<br>
Cache-Control: max-age=5<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Mon, 14 Feb 2011 21:35:05 GMT<br>
Last-Modified: Mon, 14 Feb 2011 21:35:00 GMT<br>
Server: lighttpd/1.4.26<br>
Content-Length: 1675<br>
Date: Mon, 14 Feb 2011 21:35:00 GMT<br>
X-RateLimit-Limit: 10000<br>
X-RateLimit-Remaining: 9998<br>
X-RateLimit-Reset: 1297722896<br>
Connection: close<br>
<br>
{"request":{"parameters":{"q":"kindle","type":"cited"},"response_type":"json","resource":"searchhistogram","url":"http://otter.topsy.com/searchhistogram.json?q=kindle&amp;type=cited"},"response":<br>
{"histogram":[2839,3748,4223,3530,5104,5439,5302,5192,5630,4935,4560,3687,4963,6003,6191,5068,5387,6273,4831,5069,4578,4530,5774,5918,4655,5072,5434,5086,5112,5589,5173,4751,5185,4749,5246,47<br>
97,4917,4901,5168,5429,6291,5646,5184,5436,4995,6385,5932,5945,7589,7697,6535,4619,3774,3944,4682,3672,3515,3068,3496,5457,5491,5496,4157,3571,3125,3187,3552,5233,5561,5753,4556,3960,4118,461<br>
3,5257,5619,4073,4240,3744,3784,4762,5053,4418,4293,4065,4061,4337,4421,3969,3909,4077,3889,3711,3968,4381,5130,5027,5249,4142,3844,3796,4245,4069,4080,4893,4512,3883,3986,4840,4641,4615,5088<br>
,5321,4006,4834,4391,4188,3930,4211,4192,3267,2668,3285,3533,3756,3877,3337,2620,2715,3106,2833,3635,3783,3107,3018,3012,3357,3528,3998,4808,3564,5103,6132,6944,7914,7297,6831,6081,4982,5467,<br>
6656,5724,7360,8795,5517,4521,4384,5913,6587,6021,6927,5323,4495,4641,5529,5847,6780,7274,4061,4966,4140,3034,4854,4498,3035,3188,2665,2616,3012,2697,3181,2559,2401,2217,2380,2388,2806,3772,3<br>
724,3018,2888,2900,2812,3417,2922,3972,2985,2206,2336,3949,8987,1933,1831,1445,1517,1230,1386,1282,1069,1919,651,663,583,694,697,794,901,726,764,654,729,895,958,986,885,718,692,975,1790,1081,<br>
1725,1239,525,592,542,605,766,1637,1064,353,341,363,507,653,743,330,48,112,318,390,477,537,506,407,345,389,442,597,758,557,411,582,520,500,703,572,521,385,354,385,422,726,1092,458,293,217,374<br>
,418,738,822,438,366,416,542,509,591,603,431,354,589,614,736,509,617,573,385,599,660,580,581],"period":300,"count_method":"target","slice":86400}}<br>
<br>
</code></pre>

<hr />

<h2>/searchdate</h2>

<b>Description:</b> Returns search results sorted by reverse chronology.  All options are the same as that of /search.<br>
<br>
This method performs regular search as /search, picks top N results based on relevance, then sort them by the timesstamp of the first citation. In other words, it is a timeline of high quality results. The quality level is controlled by parameter "zoom", the default value 10 will pick up to 100 results.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>  </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> q            </td><td> required        </td><td> Search query string. (<a href='QuerySyntax.md'>query syntax</a>) </td></tr>
<tr><td> window       </td><td> optional        </td><td> See /search documentation. </td></tr>
<tr><td> type         </td><td> optional        </td><td> See /search documentation. </td></tr>
<tr><td> zoom         </td><td> optional        </td><td> Zoom-level for depth / quality.  Default is 10, which picks 100 results </td></tr></tbody></table>

<hr />

<h2>/stats</h2>

<b>Description:</b> Count of tweets for a url. This is an efficient way<br>
of getting the counts only. For detailed information about a URL,<br>
use urlinfo.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>   </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> url           </td><td> required        </td><td> URL string for the target. </td></tr></tbody></table>

<h3>Example:</h3>

Fetch only the trackback counts in json format that reference Topsy's homepage.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/stats.json?url=http://topsy.com/"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 04:27:18 GMT<br>
Content-Length: 335<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:32:18 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2486<br>
X-RateLimit-Reset: 1251349200<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "url" : "http://topsy.com/"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "stats",<br>
      "url" : "http://otter.topsy.com/stats.json?url=http%3A%2F%2Ftopsy.com%2F"<br>
   },<br>
   "response" : {<br>
      "topsy_trackback_url" : "http://topsy.com/tb/topsy.com/",<br>
      "contains" : "1931",<br>
      "influential" : "874",<br>
      "all" : "1931"<br>
   }<br>
}<br>
</code></pre>

<hr />

<h2>/top</h2>

<b>Description:</b> A feed of Top 100, 1K, 5K and 20K links, photos, tweets & videos posted on the social web everyday.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>   </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> thresh        </td><td> required        </td><td> top100, top1k, top5k, top20k </td></tr>
<tr><td> type          </td><td> optional        </td><td> defaults to everything. Other values: image, video, tweet </td></tr>
<tr><td> locale        </td><td> optional        </td><td> defaults to all.  Other values:  en, ja, ko, de, pt, es, th, fr </td></tr></tbody></table>

Accepts <a href='ResListParameters.md'>List Parameters</a>

This method returns a feed of Top 100, or 1K (1000), 5K (5000), 20K (20,000) items posted on Twitter everyday.  The list is computed using a predictive algorithm, which dynamically adjusts ranking criteria to determine the threshold number of items everyday.  You can select a particular threshold with the <code>thresh</code> parameter.<br>
<br>
When <code>type</code> is not specified, the list includes all types of items.  There are independent lists for type image, video and tweet, that can be accessed with the <code>type</code> parameter.<br>
<br>
Several languages are supported by /top, described in the table above.<br>
<br>
<h3>Example:</h3>

Fetch the Top 100 tweets in English.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/top.json?thresh=top100&amp;type=tweet&amp;locale=en"<br>
<br>
HTTP/1.1 200 OK<br>
Cache-Control: max-age=5<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 23 Mar 2011 01:51:17 GMT<br>
Last-Modified: Wed, 23 Mar 2011 01:51:12 GMT<br>
Server: lighttpd/1.4.26<br>
Content-Length: 8440<br>
Date: Wed, 23 Mar 2011 01:51:13 GMT<br>
X-Varnish: 1488685665<br>
Age: 0<br>
Via: 1.1 varnish<br>
X-Served-By: ps391<br>
X-Cache: MISS<br>
Connection: close<br>
<br>
{<br>
   "request" : {<br>
      "resource" : "top",<br>
      "response_type" : "json",<br>
      "parameters" : {<br>
         "locale" : "en",<br>
         "type" : "tweet",<br>
         "thresh" : "top100"<br>
      },<br>
      "url" : "http://otter.topsy.com/top.json?locale=en&amp;thresh=top100&amp;type=tweet"<br>
   },<br>
   "response" : {<br>
      "page" : 1,<br>
      "locale" : "en",<br>
      "total" : 500,<br>
      "perpage" : 10,<br>
      "last_offset" : 14,<br>
      "hidden" : 1,<br>
      "thresh" : "top100",<br>
      "list" : [<br>
         {<br>
            "author_url" : "http://twitter.com/idothat2",<br>
            "date" : 1300844963,<br>
            "author_img" : "http://a1.twimg.com/profile_images/1246614074/idothattoo_normal.png",<br>
            "content" : "RT @IDoThat2: Make a fist with your left hand, squeeze your left thumb, then put your right index finger down your throat. NO GAG REFLEX.",<br>
            "date_alpha" : "41 seconds ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/idothat2/status/50368320272220160?utm_source=otter",<br>
               "url" : "http://twitter.com/idothat2/status/50368320272220160",<br>
               "mytype" : "tweet",<br>
               "title" : "Make a fist with your left hand, squeeze your left thumb, then put your right index finger down your throat. NO GAG REFLEX.",<br>
               "trackback_total" : 445<br>
            },<br>
            "author_nick" : "idothat2",<br>
            "firstpost_date" : 1300843743,<br>
            "topsy_author_url" : "http://topsy.com/twitter/idothat2?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/quixotic",<br>
            "date" : 1300844892,<br>
            "author_img" : "http://a0.twimg.com/profile_images/14300972/pic_mgmt_rhoffman_100x100_normal.gif",<br>
            "content" : "RT @quixotic: Here&amp;#39;s the 10 rules of massive entrepreneurship that I covered at SXSW.  http://lnkd.in/BfdBkT",<br>
            "date_alpha" : "2 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/quixotic/status/50369753562357761?utm_source=otter",<br>
               "url" : "http://twitter.com/quixotic/status/50369753562357761",<br>
               "mytype" : "tweet",<br>
               "title" : "Here&amp;#39;s the 10 rules of massive entrepreneurship that I covered at SXSW.  http://lnkd.in/BfdBkT",<br>
               "trackback_total" : 17<br>
            },<br>
            "author_nick" : "quixotic",<br>
            "firstpost_date" : 1300844076,<br>
            "topsy_author_url" : "http://topsy.com/twitter/quixotic?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/niw",<br>
            "date" : 1300844714,<br>
            "author_img" : "http://a0.twimg.com/profile_images/1255264346/discover_normal.jpg",<br>
            "content" : "RT @niw: Mac OS Xでどうぞ→ $ say &amp;quot;tahno see nurcomer gah popopo-poooon\\!&amp;quot;",<br>
            "date_alpha" : "5 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/niw/status/50293712605036544?utm_source=otter",<br>
               "url" : "http://twitter.com/niw/status/50293712605036544",<br>
               "mytype" : "tweet",<br>
               "title" : "Mac OS Xでどうぞ→ $ say &amp;quot;tahno see nurcomer gah popopo-poooon\\!&amp;quot;",<br>
               "trackback_total" : 21<br>
            },<br>
            "author_nick" : "niw",<br>
            "firstpost_date" : 1300826225,<br>
            "topsy_author_url" : "http://topsy.com/twitter/niw?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/herbcaen",<br>
            "date" : 1300844451,<br>
            "author_img" : "http://a3.twimg.com/profile_images/843522902/herb1_normal.jpg",<br>
            "content" : "RT @HerbCaen: Caress each Spanish syllable. Don&amp;#39;t say &amp;quot;Frisco.&amp;quot; Don&amp;#39;t say &amp;quot;San-Fran-Cis-Co.&amp;quot; That&amp;#39;s how tourists pronounce it. It&amp;#39;s &amp;quot;SanfrnSISco.&amp;quot;",<br>
            "date_alpha" : "9 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/herbcaen/status/50302206058053632?utm_source=otter",<br>
               "url" : "http://twitter.com/herbcaen/status/50302206058053632",<br>
               "mytype" : "tweet",<br>
               "title" : "Caress each Spanish syllable. Don&amp;#39;t say &amp;quot;Frisco.&amp;quot; Don&amp;#39;t say &amp;quot;San-Fran-Cis-Co.&amp;quot; That&amp;#39;s how tourists pronounce it. It&amp;#39;s &amp;quot;SanfrnSISco.&amp;quot;",<br>
               "trackback_total" : 23<br>
            },<br>
            "author_nick" : "herbcaen",<br>
            "firstpost_date" : 1300827990,<br>
            "topsy_author_url" : "http://topsy.com/twitter/herbcaen?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/ajelive",<br>
            "date" : 1300844327,<br>
            "author_img" : "http://a3.twimg.com/profile_images/955686894/AJE_TWITTER_ICON_normal.jpg",<br>
            "content" : "RT @AJELive: Reports of at least 4 people killed in the #Syrian city of #Daraa, where residents say electricity has been cut off: http://aje.me/hBUe4g",<br>
            "date_alpha" : "11 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/ajelive/status/50368232003084288?utm_source=otter",<br>
               "url" : "http://twitter.com/ajelive/status/50368232003084288",<br>
               "mytype" : "tweet",<br>
               "title" : "Reports of at least 4 people killed in the #Syrian city of #Daraa, where residents say electricity has been cut off: http://aje.me/hBUe4g",<br>
               "trackback_total" : 36<br>
            },<br>
            "author_nick" : "ajelive",<br>
            "firstpost_date" : 1300843708,<br>
            "topsy_author_url" : "http://topsy.com/twitter/ajelive?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/thinkprogress",<br>
            "date" : 1300844316,<br>
            "author_img" : "http://a1.twimg.com/profile_images/1256047404/TP_normal.gif",<br>
            "content" : "RT @thinkprogress: NEW POLL: Just 7% of Americans view the federal deficit as the most important problem facing U.S. today http://thkpr.gs/ecU4DU",<br>
            "date_alpha" : "11 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/thinkprogress/status/50362164892008449?utm_source=otter",<br>
               "url" : "http://twitter.com/thinkprogress/status/50362164892008449",<br>
               "mytype" : "tweet",<br>
               "title" : "NEW POLL: Just 7% of Americans view the federal deficit as the most important problem facing U.S. today http://thkpr.gs/ecU4DU",<br>
               "trackback_total" : 43<br>
            },<br>
            "author_nick" : "thinkprogress",<br>
            "firstpost_date" : 1300842264,<br>
            "topsy_author_url" : "http://topsy.com/twitter/thinkprogress?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/mohammad_syria",<br>
            "date" : 1300844280,<br>
            "author_img" : "http://a2.twimg.com/profile_images/1133769021/RWR_normal.png",<br>
            "content" : "RT @Mohammad_Syria: Confirmed: Eyewitnesses: 6 dead bodies inside #Omari mosque right now as army committed a massacre in #Daraa #Syria #mar15",<br>
            "date_alpha" : "12 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/mohammad_syria/status/50359652470362112?utm_source=otter",<br>
               "url" : "http://twitter.com/mohammad_syria/status/50359652470362112",<br>
               "mytype" : "tweet",<br>
               "title" : "Confirmed: Eyewitnesses: 6 dead bodies inside #Omari mosque right now as army committed a massacre in #Daraa #Syria #mar15",<br>
               "trackback_total" : 25<br>
            },<br>
            "author_nick" : "mohammad_syria",<br>
            "firstpost_date" : 1300841681,<br>
            "topsy_author_url" : "http://topsy.com/twitter/mohammad_syria?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/inhabitat",<br>
            "date" : 1300844109,<br>
            "author_img" : "http://a3.twimg.com/profile_images/51865670/OwliMcOwl_normal.jpg",<br>
            "content" : "RT @inhabitat: California just launched a new energy upgrade program that can qualify residents for thousands of dollars in rebates! http://bit.ly/hGsnHc",<br>
            "date_alpha" : "15 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/inhabitat/status/50318962348654592?utm_source=otter",<br>
               "url" : "http://twitter.com/inhabitat/status/50318962348654592",<br>
               "mytype" : "tweet",<br>
               "title" : "California just launched a new energy upgrade program that can qualify residents for thousands of dollars in rebates! http://bit.ly/hGsnHc",<br>
               "trackback_total" : 10<br>
            },<br>
            "author_nick" : "inhabitat",<br>
            "firstpost_date" : 1300832116,<br>
            "topsy_author_url" : "http://topsy.com/twitter/inhabitat?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/webseriestoday",<br>
            "date" : 1300843994,<br>
            "author_img" : "http://a1.twimg.com/profile_images/789016827/wst_100_normal.gif",<br>
            "content" : "RT @webseriestoday: A First: Interactive Film with Augmented Reality: ..It’s then their job to track down the victim, fin... http://bit.ly/fbpmOS #webseries",<br>
            "date_alpha" : "17 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/webseriestoday/status/50327403851022336?utm_source=otter",<br>
               "url" : "http://twitter.com/webseriestoday/status/50327403851022336",<br>
               "mytype" : "tweet",<br>
               "title" : "A First: Interactive Film with Augmented Reality: ..It’s then their job to track down the victim, fin... http://bit.ly/fbpmOS #webseries",<br>
               "trackback_total" : 17<br>
            },<br>
            "author_nick" : "webseriestoday",<br>
            "firstpost_date" : 1300835145,<br>
            "topsy_author_url" : "http://topsy.com/twitter/webseriestoday?utm_source=otter"<br>
         },<br>
         {<br>
            "author_url" : "http://twitter.com/impolitical",<br>
            "date" : 1300843992,<br>
            "author_img" : "http://a0.twimg.com/profile_images/653297476/Twitter_avatar_grn_normal.jpg",<br>
            "content" : "RT @impolitical: Hebert: Budget &amp;quot;was not designed to restore peace in the 40th Parliament.&amp;quot; http://ow.ly/4kcb2 #cdnpoli",<br>
            "date_alpha" : "17 minutes ago",<br>
            "target" : {<br>
               "topsy_trackback_url" : "http://topsy.com/twitter.com/impolitical/status/50330927347404802?utm_source=otter",<br>
               "url" : "http://twitter.com/impolitical/status/50330927347404802",<br>
               "mytype" : "tweet",<br>
               "title" : "Hebert: Budget &amp;quot;was not designed to restore peace in the 40th Parliament.&amp;quot; http://ow.ly/4kcb2 #cdnpoli",<br>
               "trackback_total" : 6<br>
            },<br>
            "author_nick" : "impolitical",<br>
            "firstpost_date" : 1300834843,<br>
            "topsy_author_url" : "http://topsy.com/twitter/impolitical?utm_source=otter"<br>
         }<br>
      ],<br>
      "offset" : 0<br>
   }<br>
}<br>
<br>
</code></pre>

---<br>
<br>
<h2>/trackbacks</h2>

<b>Description:</b> List of tweets (trackbacks) that mention the query URL, most recent first.<br>
<br>
NOTE: If you are only interested in the counts, call the more efficient method /stats instead.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>       </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> url               </td><td> required        </td><td> URL for the target. </td></tr>
<tr><td> contains          </td><td> optional        </td><td> Query string to filter results. </td></tr>
<tr><td> infonly           </td><td> optional        </td><td> Boolean value that filters trackbacks to influential only (default 0) </td></tr>
<tr><td> sort_method       </td><td> optional        </td><td> the order in which to return results. Options are "influence", "date" and "-date". </td></tr></tbody></table>

Accepts <a href='ResListParameters.md'>List Parameters</a>

<h3>Example:</h3>

Fetch posts (tweets) in json format that reference Topsy's homepage.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/trackbacks.json?url=http://topsy.com/"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 03:59:23 GMT<br>
Content-Length: 7363<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:04:23 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2467<br>
X-RateLimit-Reset: 1251345600<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "url" : "http://topsy.com/"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "trackbacks",<br>
      "url" : "http://otter.topsy.com/trackbacks.json?url=http%3A%2F%2Ftopsy.com%2F"<br>
   },<br>
   "response" : {<br>
      "topsy_trackback_url": "http://topsy.com/tb/topsy.com/",<br>
      "page" : 1,<br>
      "total" : "1931",<br>
      "perpage" : 10,<br>
      "list" : [<br>
         {<br>
            "permalink_url" : "http://twitter.com/imadnaffa/status/3565855201",<br>
            "date" : "1251324809",<br>
            "content" : "TOPSY - A search engine powered by tweets: http://topsy.com (this Search Engine can <br>
                        be powerful for sifting through Twitter- love it)!",<br>
            "type" : "tweet",<br>
            "author" : {<br>
               "url" : "http://twitter.com/imadnaffa",<br>
               "name" : "Imad Naffa",<br>
               "photo_url" : "http://a3.twimg.com/profile_images/378575667/imad_blue_shirt_normal.jpg",<br>
               "topsy_author_url" : "http://topsy.com/twitter/imadnaffa",<br>
               "influence_level" : "4"<br>
            },<br>
            "date_alpha" : "6 hours ago"<br>
         },<br>
         ...<br>
      ]<br>
   }<br>
}<br>
</code></pre>

<h3>Example:</h3>

Fetch posts (tweets) that reference Topsy's homepage from influential users only.<br>
<br>
<pre><code>curl -i "http://otter.topsy.com/trackbacks.json?url=http://topsy.com/&amp;infonly=1&amp;tracktype=tweet"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 04:03:25 GMT<br>
Content-Length: 7413<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:08:20 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2499<br>
X-RateLimit-Reset: 1251349200<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "infonly" : "1",<br>
         "tracktype" : "tweet",<br>
         "url" : "http://topsy.com/"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "trackbacks",<br>
      "url" : "http://otter.topsy.com/trackbacks.json?infonly=1&amp;tracktype=tweet&amp;url=http%3A%2F%2Ftopsy.com%2F"<br>
   },<br>
   "response" : {<br>
      "topsy_trackback_url": "http://topsy.com/tb/topsy.com/",<br>
      "page" : 1,<br>
      "total" : "874",<br>
      "perpage" : 10,<br>
      "list" : [<br>
         {<br>
            "permalink_url" : "http://twitter.com/imadnaffa/status/3565855201",<br>
            "date" : "1251324809",<br>
            "content" : "TOPSY - A search engine powered by tweets: http://topsy.com (this <br>
                        Search Engine can be powerful for sifting through Twitter- love it)!",<br>
            "type" : "tweet",<br>
            "author" : {<br>
               "url" : "http://twitter.com/imadnaffa",<br>
               "name" : "Imad Naffa",<br>
               "photo_url" : "http://a3.twimg.com/profile_images/378575667/imad_blue_shirt_normal.jpg",<br>
               "topsy_author_url" : "http://topsy.com/twitter/imadnaffa",<br>
               "influence_level" : "4"<br>
            },<br>
            "date_alpha" : "6 hours ago"<br>
         },<br>
         ...<br>
      ]<br>
   }<br>
}<br>
</code></pre>

<hr />

<h2>/urlinfo</h2>

<b>Description:</b> Information about an url.<br>
<br>
<h3>Parameters:</h3>

<table><thead><th> <b>Name</b>   </th><th> <b>Required</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> url           </td><td> required        </td><td> URL string for the target. </td></tr></tbody></table>

<h3>Example:</h3>

Fetch information about Twitter's homepage.<br>
<br>
<pre><code>$ curl -i "http://otter.topsy.com/urlinfo.json?url=http://twitter.com/"<br>
<br>
HTTP/1.0 200 OK<br>
Connection: close<br>
Date: Thu, 27 Aug 2009 04:17:51 GMT<br>
Content-Length: 694<br>
Content-Type: application/json; charset=utf-8<br>
Expires: Wed, 26 Aug 2009 21:22:51 -0700<br>
Status: 200<br>
X-RateLimit-Limit: 2500<br>
X-RateLimit-Remaining: 2491<br>
X-RateLimit-Reset: 1251349200<br>
<br>
{<br>
   "request" : {<br>
      "parameters" : {<br>
         "url" : "http://twitter.com/"<br>
      },<br>
      "response_type" : "json",<br>
      "resource" : "urlinfo",<br>
      "url" : "http://otter.topsy.com/urlinfo.json?url=http%3A%2F%2Ftwitter.com%2F"<br>
   },<br>
   "response" : {<br>
      "topsy_trackback_url" : "http://topsy.com/tb/twitter.com/",<br>
      "oneforty" : "Twitter: What are you doing? http://twurl.nl/pd8k44",<br>
      "url" : "http://twitter.com/",<br>
      "title" : "Twitter: What are you doing?",<br>
      "trackback_total" : "24152",<br>
      "description" : "Social networking and microblogging service utilising instant messaging, SMS or a web interface.",<br>
      "description_attribution" : "From DMOZ"<br>
   }<br>
}<br>
</code></pre>
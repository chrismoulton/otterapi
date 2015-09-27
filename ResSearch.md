# Resource: search #

**Description:** List of results for a query.

**URL Format:** `http://otter.topsy.com/search.`[format](ResponseFormats.md)`?query=parameters`

## Parameters: ##

| **Name**  | **Required** | **Description** |
|:----------|:-------------|:----------------|
| q         | required     | Search query string. ([query syntax](QuerySyntax.md)) |
| window    | optional     | Time window for results. (default: `a` Options: `auto` - automatically pick the most relevant window. `h` last hour, `d` last day, `w` last week, `m` last month, `a` all time |

Accepts [List Parameters](ResListParameters.md)

## Example: ##

Fetch search results in json format for the query "barack obama"

```
$ curl -i "http://otter.topsy.com/search.json?q=barack+obama&window=auto"

HTTP/1.0 200 OK
Connection: close
Date: Thu, 27 Aug 2009 04:06:32 GMT
Content-Length: 9097
Content-Type: application/json; charset=utf-8
Expires: Wed, 26 Aug 2009 21:11:31 -0700
Status: 200
X-RateLimit-Limit: 2500
X-RateLimit-Remaining: 2498
X-RateLimit-Reset: 1251349200

{
   "request" : {
      "parameters" : {
         "window" : "auto",
         "q" : "barack obama"
      },
      "response_type" : "json",
      "resource" : "search",
      "url" : "http://otter.topsy.com/search.json?q=barack+obama&window=auto"
   },
   "response" : {
      "window" : "d",
      "page" : 1,
      "total" : "809",
      "perpage" : 10,
      "list" : [
         {
            "trackback_permalink" : "http://twitter.com/ewerickson/status/3562164195",
            "hits" : 38,
            "topsy_trackback_url" : "http://topsy.com/tb/www.redstate.com/erick/2009/08/26/breaking-rumors-surface-that-leon-panetta-is-resigning/",
            "url" : "http://www.redstate.com/erick/2009/08/26/breaking-rumors-surface-that-leon-panetta-is-resigning/",
            "content" : "Panetta is rumored to have sent a resignation letter to Barack Obama today:  http://bit.ly/CDMg9",
            "title" : "BREAKING: Rumors Surface That Leon Panetta is Resigning - Erickâs blog - RedState",
            "score" : 0.75521481,
            "highlight" : "Panetta is rumored to have sent a resignation letter to <span class=\"highlight-term\">Barack</span> <span class=\"highlight-term\">Obama</span> today:  http://bit.ly/CDMg9"
         },
         ...
      ]
   }
}
```

## Example: ##

Fetch the most popular youtube videos today.

```
$ curl -i "http://otter.topsy.com/search.json?q=site:youtube.com&window=d"

HTTP/1.0 200 OK
Connection: close
Date: Thu, 27 Aug 2009 04:09:09 GMT
Content-Length: 7086
Content-Type: application/json; charset=utf-8
Expires: Wed, 26 Aug 2009 21:14:09 -0700
Status: 200
X-RateLimit-Limit: 2500
X-RateLimit-Remaining: 2496
X-RateLimit-Reset: 1251349200

{
   "request" : {
      "parameters" : {
         "window" : "d",
         "q" : "site:youtube.com"
      },
      "response_type" : "json",
      "resource" : "search",
      "url" : "http://otter.topsy.com/search.json?q=site%3Ayoutube.com&window=d"
   },
   "response" : {
      "window" : "d",
      "page" : 1,
      "total" : "58258",
      "perpage" : 10,
      "list" : [
         {
            "trackback_permalink" : "http://twitter.com/danilogentili/status/3567528055",
            "hits" : 2499,
            "topsy_trackback_url" : "http://topsy.com/trackback?url=http://www.youtube.com/watch?v=i_KPsH7f3xo",
            "url" : "http://www.youtube.com/watch?v=i_KPsH7f3xo",
            "content" : "ApÃ³s ver isso http://bit.ly/xOl3b, eu, Danilo Zentili, peÃ§o perdÃ£o aos fÃ£s da Susxa que, como @Davis_Reimberg , sonhavam ser paquitas.",
            "title" : "MEXEU COM A XUXA MEXEU COMIGO!!!",
            "score" : 24.20444298,
            "highlight" : "ApÃ³s ver isso http://bit.ly/xOl3b, eu, Danilo Zentili, peÃ§o perdÃ£o aos fÃ£s da Susxa que, como @Davis_Reimberg , sonhavam ser paquitas."
         },
         ...
      ]
   }
}
```
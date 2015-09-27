

Response formats are specified as a file-extension in the API request url. Topsy provides resources in [JSON format](#JSON.md) (".json") and [Javascript format (JSONP)](#Javascript.md) (".js"). There's also a [txt](#Txt.md) format for debugging.

# JSON #

When an API request uses a JSON response format, the response body will be in the form of a JSON object. An HTTP Header Content-Type: application/json` will also be sent.

#### Example Request: ####
```
http://otter.topsy.com/stats.json?url=http://blog.example.com/my-post
```

#### Example Response: ####
```
{'request':{'response_type':'json','parameters':{'url':'http://blog.example.com/my-post'}, ... }
```

# Javascript (JSONP) #

When an API request uses a Javascript response format, the response body will be a javascript function call that takes one parameter containing the response object. An HTTP Header Content-Type: application/javascript` will also be sent.

### Parameters: ###

| **Name**  | **Type** | **Description** |
|:----------|:---------|:----------------|
| callback       | string   | Javascript callback function name. (required) |

#### Example Request: ####
```
http://otter.topsy.com/stats.js?callback=foobar&url=http://blog.example.com/my-post
```

#### Example Response: ####
```
foobar({'request':{'response_type':'js','parameters':{'url':'http://blog.example.com/my-post'}, ... });
```

# Txt #

This is for debug purposes only! The TXT response type returns a Data::Dumper object version (a form of perl object serialization) of the response object.  This is useful for debugging / learning the API in the browser.  Please DO NOT parse this with a perl script.

#### Example Request: ####
```
http://otter.topsy.com/stats.txt?url=http://topsy.com/
```

#### Example Response: ####
```
### FOR DEBUG ONLY ###
$VAR1 = {
  'request' => {
    'response_type' => 'txt',
    'parameters' => {
      'url' => 'http://topsy.com/'
    },
    'request_type' => 'stats',
    'url' => 'http://otter.topsy.com/stats.txt?url=http%3A%2F%2Ftopsy.com%2F'
  },
  'response' => {
    'contains' => '1889',
    'influential' => '464',
    'all' => '1889'
  }
};
```
# List Parameters #

List parameters available to all list [resources](Resources.md).

| **Name**  | **Required** | **Description** |
|:----------|:-------------|:----------------|
| page      | optional     | page number of the result set. (default: `1`, max: `10`) |
| perpage   | optional     | limit number of results per page. (default: `10`, max: `100`) |
| offset    | optional     | offset from which to start the results, should be set to **last\_offset** parameter returned in the previous page. |
| mintime   | optional     | earliest date/time to restrict a result set. unix-timestamp format. ( Note - search.json can be used with either "window" or "mintime" and/or "maxtime" but not both. Using "window" as well as "mintime"/"maxtime" can provide 0 or incorrect results) |
| maxtime   | optional     | most recent date/time to restrict a result set. unix-timestamp format. (Note - search.json can be used with either "window" or "mintime" and/or "maxtime" but not both. Using "window" as well as "mintime"/"maxtime" can provide 0 or incorrect results) |
| allow\_lang | optional     | Language filter which lets you specify the languages you would like to see results in. Currently supports ja, zh, ko and en.  Option also takes a comma separated list of languages.  |


## Examples: ##
```
http://otter.topsy.com/search.json?q=New+York&page=2&offset=24
```

This query will fetch the second page of a search for "New York" and return a json object.

```
http://otter.topsy.com/search.json?q=New+York&perpage=25
```

This query will fetch the first 25 results of a search for "New York" and return a json object.
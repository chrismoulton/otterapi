

A successful Otter call returns with the **HTTP code 200**. Everything else
is an error or a special condition and all well-written apps must handle
these gracefully.

# 400 #

**Parameter check failed.** This error indicates that a required parameter is missing or a parameter has a value that is out of bounds.

# 403 #

**Forbidden.** You don't have access to this action.

# 404 #

**Action not supported.** This indicates you have requested a [resource](Resources.md) that does not exist.

# 500 #

**Unexpected internal error.** What it says. We'll strive NOT to return
these but your app should be prepared to see it.

# 503 #

**Temporarily unavailable.** This is an important error condition and your app MUST handle it. A 503 is returned for two different reasons:

  * The client has run out of its token allocation.  See RateLimit section for details.

  * The API is unavailable for scheduled or unscheduled downtime.  If something is wrong on our end, we'll try our best to return a 503 error code so you know whatever it is will be fixed shortly.
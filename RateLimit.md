# Usage Terms #

You can get a 30-day free trial of the Topsy Otter API by signing up for a key. This key will give you access for up to 7,000 calls a day.  During your free access period, we ask for two things:

1. ... link back to Topsy with the following "Powered by Topsy" logo:

![http://cdn.topsy.com/img/powered.png](http://cdn.topsy.com/img/powered.png)

2. ... allow us to say that you use Topsy.  In legal speak, we ask that you agree to grant Topsy a non-exclusive, royalty-free, license to use your trade names, trademarks, service marks, logos, domain names in presentations, marketing materials, customer lists and press releases.

# Rate Limit #

The Otter API uses a credit allocation system to ensure fair distribution of capacity and support multiple tiers of usage, both free and commercial. The allocation scheme allows for:

  1. 7,000 queries per day for free trial API key users. This requires a simple sign-up via our Topsy manage page - http://manage.topsy.com/app.
  1. Commercial API for larger volumes and extended use.  If your application requires larger volumes or access beyond the initial 30 days,please send us a note at api@topsy.com.

> You can check the status of your queries with the following call:

```
http://otter.topsy.com/credit.json
```

In addition, each request contains rate limit information in the HTTP response headers.

| **HTTP Header**            | **Description**|
|:---------------------------|:|
| `X-RateLimit-Limit`        | Total credits that can be allocated. |
| `X-RateLimit-Remaining`    | Total credits available. |
| `X-RateLimit-Reset`        | Timestamp (unix epoch) for when the credits will be reset. |

### Example HTTP Response Headers ###

```
X-RateLimit-Limit: 7000
X-RateLimit-Remaining: 2498
X-RateLimit-Reset: 1250791200
```

# Paging Limits #

All calls that take [list parameters](ResListParameters.md) limit `perpage` to 100 and `page` to 10. This gives you access to top 1,000 items on any list.

# Client Identification #

If you are using IP based credit limits, we request that you identify your application or service via the `User-Agent` HTTP header. This value should be the url to your service or application. This is not mandatory, but when under heavy load, we will give preference to clients that identify themselves. It is also possible to identify via `X-Topsy-UA` HTTP header, if modifying the `User-Agent` header is not possible.
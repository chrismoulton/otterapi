# The Otter URI #

The api is accessible via the uri: http://otter.topsy.com/

# API Request Format #

All requests are implemented via HTTP GET calls. The url of the request
can be broken down into three parts: [resource](Resources.md),
[response-format](ResponseFormats.md), and query parameters. A malformed
request will return a response with HTTP 400 status.

### Syntax ###

> `GET /`[resource](Resources.md)`.`[response-format](ResponseFormats.md)`?beta=BETAKEY&query=params HTTP/1.1`<br>
<blockquote><code>Host: otter.topsy.com</code></blockquote>

<h2>Next</h2>

<ul><li><a href='Resources.md'>Resources</a>
</li><li><a href='ResponseFormats.md'>ResponseFormats</a>
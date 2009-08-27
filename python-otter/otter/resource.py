#!/usr/bin/env python

import urllib2
import urllib
import urlparse
import json

class Resource(object):
    """Base class for calling Otter REST API
    >>> import otter
    >>> kw = otter.loadrc() # load beta key
    >>> r = Resource('search', **kw)
    >>> r(q='san francisco', window='h')
    >>> for page in r:
    ...   for item in page.response.list:
    ...     print item.title
    ...     print item.url
    """

    def __init__(self, resource, format='json', **kw):
        """resource = otter REST resource name (ie. search),
        format = (only json is supported right now),
        kw = keyword args to pass to the api"""
        self.resource = resource
        self.format = format
        self.res = None # store decoded json
        self.kw = kw

    @staticmethod
    def make_url(resource, response_format='json', **kw):
        """staticmethod to constuct an api url"""
        query = urllib.urlencode(kw)
        parts = (
            'http',
            'otter.topsy.com',
            '%s.%s' % (resource, response_format),
            '', # params
            query,
            '' # fragment
        )
        return urlparse.urlunparse(parts)

    @staticmethod
    def get(url):
        """use urllib2 to get the url and return decoded json"""
        f = urllib2.urlopen(url)
        data = f.read()
        return json.loads(data)

    def __call__(self, **kw):
        """call (HTTP GET) the API resource, return self"""
        self.kw.update(kw)
        self.url = self.make_url(self.resource, self.format, **self.kw)
        self.res = JsonObject(self.get(self.url))
        return self

    def next_page(self):
        """fetch the next page"""
        if self.res == None:
            raise RuntimeError('must get resource before calling next')
        page = int(self.res.response.page) + 1
        self.kw['page'] = page
        return self(**self.kw)

    def __iter__(self):
        """iterate over all the pages"""
        def gen():
            if self.res:
                try :
                    while True:
                        yield self
                        self.next_page()
                except urllib2.HTTPError, e:
                    pass
        return gen()

    def __getattr__(self, name):
        """quick access to response and request json objects"""
        if name == 'response':
            return self.res.response
        elif name == 'request':
            return self.res.request
        raise AttributeError

class JsonObject(object):
    """Wrapper around Json object and array"""

    def __init__(self, o):
        self.o = o

    def __getattr__(self, name):
        try:
            if isinstance(self.o, list):
                # allow querying of items in a list
                # for example: response.list.url
                r = []
                for i in self.o:
                    a = i[unicode(name)]
                    if isinstance(a, dict) or isinstance(a, list):
                        r.append(JsonObject(a))
                    else:
                        r.append(a)
                return JsonObject(r)
            else:
                a = self.o[unicode(name)]
                if isinstance(a, dict) or isinstance(a, list):
                    return JsonObject(a)
                else:
                    return a
        except KeyError:
            pass
        raise AttributeError("%s not found" % name)

    def __str__(self):
        return str(self.o)

    def __unicode__(self):
        return unicode(self.o)

    def __iter__(self):
        def gen():
            for i in self.o:
                yield JsonObject(i)
        return gen()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

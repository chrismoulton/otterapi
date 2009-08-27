"""
Interface to Topsy Otter RESTful API

Example usage:
>>> import otter
>>> kw = otter.loadrc() # load api key
>>> r = otter.Resouce('trending', **kw)
>>> r() # make api call to trending resource
>>> print r.response

Passing parameters to API:
>>> r = otter.Resource('search')
>>> r(q='san francisco', window='a')
>>> print r.response.list.url

Also see otter-api command line tool

Website: http://otter.topsy.com/
"""

__all__ = ["resource"]
__version__ = '0.1.0'
__version_info__ = (0, 1, 0)

from otter.resource import Resource

def loadrc():
    """read ~/.otterrc return dict
    useful for storing apikey ie.
    beta=betakey"""
    from os.path import expanduser, exists
    kw = {}
    rcfile = expanduser("~/.otterrc")
    if exists(rcfile):
        for l in open(rcfile):
            if l and l[0] == '#':
                continue
            l = l.strip()
            k, v = l.split('=', 1)
            kw[k] = v
    return kw
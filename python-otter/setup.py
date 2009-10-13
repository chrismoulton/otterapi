from distutils.core import setup

setup(
    name='python-otter',
    version='0.1.0',
    description='Python bindings for Topsy Otter REST API',
    long_description="""Otter API is a RESTful HTTP web service to Topsy.
Topsy is a search engine that ranks URLs by the number and quality of tweets
they receive. The quality of tweets is determined by the influence of the
Twitter users (referred to as authors) - which is based on their position in
the retweet network. URLs that are mentioned by important authors are ranked
higher.

The Otter API provides access to topsy search results, url information and
author information along with the intermediate data (like author influence)
that is used in creation of search rankings. http://topsy.com/ has been
created using the Otter API, and almost everything available on the site is
accessible to developers.""",
    author='Jason Toffaletti',
    author_email='jason@topsy.com',
    maintainer='Jason Toffaletti',
    maintainer_email='jason@topsy.com',
    url='http://code.google.com/p/otterapi/',
    packages=['otter'],
    scripts=['otter-api'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Freeware',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
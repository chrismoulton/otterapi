from distutils.core import setup

setup(
    name='python-otter',
    version='0.1.0',
    description='Python bindings for Topsy Otter REST API',
    author='Jason Toffaletti',
    author_email='jason@topsy.com',
    url='http://code.google.com/p/otterapi/',
    packages=['otter'],
    scripts=['otter-api'],
)
from distutils.core import setup
setup(
  name = 'gobiko.apns',
  packages = [
    'gobiko',
    'gobiko.apns'
  ],
  version = '0.1.7',
  description = 'A library for interacting with APNs using HTTP/2 and token-based authentication.',
  author = 'Gene Sluder',
  author_email = 'gene@gobiko.com',
  url = 'https://github.com/kajensen/python-apns',
  download_url = 'https://github.com/kajensen/python-apns/tarball/0.1.7',
  keywords = [
    'apns', 
    'push notifications',
  ],
  classifiers = [],
  install_requires=[
    'cryptography>=39.0.0',
    'hyper',
    'pyjwt',
  ],
)

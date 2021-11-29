from distutils.core import setup
setup(
  name = 'infusionsoft-im',
  packages = ['infusionsoft'],
  version = '0.1',
  license='MIT',
  description = 'Infusionsoft REST API wrapper written in Python.',
  author = 'LazyAfternoons',
  author_email = 'lazydev@outlook.it',
  url = 'https://github.com/LazyAfternoons/infusionsoft-im',
  download_url = 'https://github.com/LazyAfternoons/infusionsoft-im/archive/refs/tags/v0.1.tar.gz',
  keywords = ['INFUSIONSOFT', 'REST', 'API'],
  install_requires=[
          'validators',
          'beautifulsoup4',
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
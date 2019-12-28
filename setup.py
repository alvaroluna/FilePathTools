from distutils.core import setup

setup(name = 'PathManager', # How you named your package folder (MyLib)
      packages = ['PathManager'], # Chose the same as "name"
      version = '0.0.2', # Start with a small number and increase it with every change you make
      license='MIT',
      description = 'This module allows you to input a file path, step back n-levels toward\nthe root directory, and append an optional sub folder string.', # Give a short description about your library
      author = 'ALVARO LUNA', # Type in your name
      author_email = 'aluna@objectiveapplications.com',
      url = 'https://github.com/alvaroluna/PathManager.git',
      download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz', # I explain this later on
      keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'], # Keywords that define your package best
      install_requires = [], # required modules that need to be installed through pip
      dependency_links = [], # required modules not on pip - ex: 'http://github.com/user/repo/tarball/master#egg=package-1.0'
      classifiers = ['Development Status :: 5 - Production/Stable', # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
                     'Intended Audience :: Developers, PyRevit users',
                     'Topic :: Software Development :: Build Tools',
                     'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 2', # Specify which pyhton versions that you want to support
                     'Programming Language :: Python :: 3',
                     'Programming Language :: IronPython :: 2'
                     ]
      )

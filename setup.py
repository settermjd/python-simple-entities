from setuptools import setup


setup(name='entities',
      version='0.1',
      description='A simple package to create some entities',
      long_description='A simple package to do unit testing and code coverage with some '
                       'simple entities as our test subject.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='entities',
      url='http://github.com/settermjd/python-entities',
      author='Matthew Setter',
      author_email='matthew@matthewsetter.com',
      license='MIT',
      packages=['entities'],
      install_requires=[

      ],
      test_suite='nose.collector',
      tests_require=[
          'nose'
      ],
      include_package_data=True,
      zip_safe=False)

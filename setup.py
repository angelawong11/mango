from setuptools import setup

setup(name='mango',
      version='0.1',
      description='Coastal flood modeling tools',
      url='https://github.com/angelawong11/mango',
      author='angelawong11',
      author_email='angela.wong11@gmail.com',
      license='MIT',
      packages=['mango'],
      install_requires=[
          'numpy',
      ],
      setup_requires=['pytest-runner'],
      test_requires=[
          'pytest',
      ],
      test_suite="pytest",
      scripts=[],
      zip_safe=False)

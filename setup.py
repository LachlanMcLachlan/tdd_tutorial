from setuptools import setup

setup(name='tdd_tutorial',
      version='1.0',
      description='package containing code for the python tdd tutorial',
      classifiers=[
              'Development Status :: 4 - Beta',
              'License :: OSI Approved :: MIT License',
              'Programming Language :: Python :: 3.7',
              'Topic :: Education :: Testing'],
      install_requires=['pytest'],
      author='Lachlan McLachlan',
      author_email='lachlan.mclachlan@outlook.com',
      url='https://github.com/LachlanMcLachlan/tdd_tutorial',
      license='MIT',
      packages=['tdd_tutorial'],
      zip_safe=False)
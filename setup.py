from setuptools import setup
  
# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()
  
  
# specify requirements of your package here
REQUIREMENTS = ['requests', 'termcolor']
  
# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]
  
# calling the setup function 
setup(name='shelldict',
      version='1.0.0',
      description='A simple commandline dictionary.',
      long_description=long_description,
      url='https://github.com/0Kwanele0/shelldict',
      author='Kwanele Gamedze',
      author_email='kwanelegamedze4@gmail.com',
      license='MIT',
      packages=['dict'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='dictionary english shell commandline'
      )

from setuptools import setup, find_packages
 
setup(name='importutils',
      version='0.1',
      url='https://github.com/dattran2346/importutils',
      license='MIT',
      author='Tran Quang Dat',
      author_email='dattran2346@gmail.com',
      description='Utility to import the minimal dependencies during computer vision project',
      long_description=open('README.md').read(),
      packages=['importutils'],
      zip_safe=False)
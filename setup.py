from setuptools import setup, find_packages

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

setup(name='importutils',
      version='0.12',
      url='https://github.com/dattran2346/importutils',
      license='MIT',
      author='Tran Quang Dat',
      author_email='dattran2346@gmail.com',
      description='Utility to import the minimal dependencies during computer vision project',
      long_description=open('README.md').read(),
      install_requires=load_requirements("requirements.txt"),
      packages=['importutils'],
      zip_safe=False)
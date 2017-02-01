import sys
from setuptools import setup

if sys.version_info < (2,7):
  sys.exit("Python 2.7 or higher is required")

def readme():
  with open('README.md') as f:
    return f.read()

setup(name="ziron",
      version="0.0.1",
      description="Andrews and Arnold Python module for Ziron API",
      long_description=readme(),
      keywords=["aaisp", "api", "ziron", "tracking"],
      url="",
      author="Stuart Bruce",
      license="MIT",
      packages=["ziron", "tests"],
      install_requires=["requests"],
      include_package_data=True)

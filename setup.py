
from setuptools import setup

setup(name="quickpackage",
	version="1.1",
	description="Instantly create and upload python package for your script",
	url="https://github.com/yask123/quick-package",
	author="Yask Srivastava",
	author_email="yask123@gmail.com",
	license='MIT',
	packages=["quickpackage"],
	scripts=["bin/quickpackage"],
	zip_safe=False)

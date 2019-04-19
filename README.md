# demo-helloworld-library

## Step 0 :: Clone your project project with [Git command](https://git-scm.com/)
```
$git clone https://github.com/<username>/demo-helloworld-library.git
$cd demo-helloworld-library
```

## Step 1 :: create file `~/.pypirc`

```
[distutils]
index-servers =
  pypi

[pypi]
repository=https://pypi.python.org/pypi
username=username
password=password
```

And change permission

```
$chmod 600 ~/.pypirc
```

## Step 2 :: To publish your code into [PyPI](https://pypi.org/)
List of files
* README.md
* LICENSE.txt
* setup.cfg
* setup.py

Edit file `setup.py`
```
from setuptools import setup

setup(
    name="helloworld-library",  // change to your name
    version='0.3',  // change to version as same as tag version
    package_dir={'' : 'src'},
    packages=['HelloWorld'],
    url='https://github.com/up1/demo-helloworld-library', // change to your repository
    author='your name', 
    author_email='your email',
)

```

Add all files and folders to git repo
```
$git add -A
$git commit -m "Hello First Library"
$git tag 1.0 -m "Add tag for version 1.0"
$git push origin master
$git push —tags origin master
```

Deploy to PyPI
```
$python setup.py register -r pypi
$python setup.py sdist upload -r pypi
```

# ft_package

A simple package able to count occurrences of a string in a list. Contains a function <code>count_in_list()</code>:
``` python
from ft_filter import ft_filter

def count_in_list(iterable: list, to_find: str) -> int:
	filtered = ft_filter(lambda x: x == to_find, iterable)
	count = sum(1 for item in filtered)
	return count
```
## installation
1. get the latest version of dependencies:
``` shell
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
```
2. generate distribution packages from the folder containing <code>pyproject.toml</code>:
``` shell
python3 -m build
```
3. install the package:
``` shell
python3 -m pip install ./dist/ft_package-0.0.1.tar.gz
```
4. check the package version:
``` shell
python3 -m pip show -v ft_package
```

## removing a package
``` shell
python3 -m pip uninstall ft_package
```

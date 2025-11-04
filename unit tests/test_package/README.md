To run python tests inside a folder / module, we first need to create a __init__.py
This will tell python that the folder is not a normal directory, but a python package.
Then, run pytest folder_name to run every test file inside the folder.

# Python Packages / Directory resolution



1. Python treats folders as normal folders. If you define ___init__.py, then it treats them as a package. So it considers it as a single package (collection of libraries / modules ). Therefore when you run your code using pytest from parent directory, the parent directory would be in sys.path too.

2. If you run pytest test_package from unit tests folder, 
    you will receive an error saying no module calculator found.

3. So, you can run python -m pytest test_package from unit tests folder. Runs pytest as a module. This will include parent directory (unit tests) in the sys.path and hence calculator module will be found. 

4. Other way is to add __init__.py in test_package folder. And then running pytest test_package will work too.
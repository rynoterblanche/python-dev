### Basic setup

```
cd demo

# install pylint
python -m pip install pylint
# or
# python -m pip install -r tools/requirements.txt

# generate a pylint rc file
pylint --generate-rcfile | out-file -encoding utf8 tools/pylint/.pylintrc

# run pylint on a specific file
pylint ./src/core/workflow.py

# run pylint on your src folder
pylint ./src

# run pylint with rc file
pylint ./src --rcfile=tools/pylint/.pylintrc

# automate linting with a CI build script, for example: 
./tools/pylint/pylint.sh
```

### Important notes on using .pylintrc
- update the rc file to fit your project needs
- make a list of all the features you want to enable from the [Pylint docs](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html) and configure your rc file to enable only them

**What if you run into too many errors to manage at once on an existing project?**
- comment out all the features raising errors 
- incrementally enable features and fix issues you deem are real problems
- if certain errors are not deemed important, disable that feature
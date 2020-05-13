# sqlova-test

setup for running and testing **sqlova** container available [here](https://github.com/paulfitz/mlsql)

Visit the GitHub repository here https://github.com/paulfitz/mlsql and follow the instruction to install the **sqlova** container.

Once installed, create a Python Virtual Environment with Python Version 3.7 and activate it

> **Note**: if you don't have Python 3.7 available on your system, you can use [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) to not only manage Virtual Environments, but also specify which Python version to install. Instructions for installing specific Pythons are available [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html#installing-a-different-version-of-python) 

Once the environemt is created and activated, clone the repository with all the driver code available here  or https://github.com/zayd62/sqlova-test

Change the working directory into the cloned repository and install the Python dependencies using

```python
pip install -r requirements.txt
```
> **Note** the python virtual environemt **MUST** be activated before running this command

Once the container and the environment is setup, run the following to start the container. on Ubuntu 18.04, the command is 

> **Note** the docker container requires 3GB of Memory to run

```bash
sudo docker start sqlova
```
## hardcoded variables

### test_dataset_explicit.py

| line number | variable name | What it should change to    |
| ----------- | ------------- | --------------------------- |
| 9           | db_pth        | it should point to the test dataset. Available in the repository [here](https://github.com/zayd62/final-year-project) and the file is called `dataset.sqlite3`|

### test_dataset_generic.py

| line number | variable name | What it should change to    |
| ----------- | ------------- | --------------------------- |
| 9           | db_pth        | it should point to the test dataset. Available in the repository [here](https://github.com/zayd62/final-year-project) and the file is called `dataset.sqlite3`|

### interactive.py

| line number | variable name | What it should change to                                                                                                                                      |
| ----------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 51          | db_pth        | it should point to the test dataset. Available in the repository [here](https://github.com/zayd62/final-year-project) and the file is called `dataset.sqlite3` |

## interactive and test

run (in the activate and setup virtual environment and docker container) in the root of the repository

```bash
python interactive.py # for the interactive mode
python test_dataset_generic.py # for running the tests
python test_dataset_explicit.py # for running the tests
```
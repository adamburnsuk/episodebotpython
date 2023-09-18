# Project Setup with Python's `venv`

This guide provides instructions on how to set up and manage a Python virtual environment using the built-in `venv` module. This ensures that dependencies remain consistent across different setups.

## Pre-requisites

- Make sure Python 3.3 or newer is installed on your machine. To check the installed version, run:
  ```bash
  python3 --version

## Setting Up a New Virtual Environment

1. Navigate to the Project Directory:
Open a terminal or command prompt and navigate to the root directory of your project:

```
cd /path/to/your/project
```

2.  Create the Virtual Environment
To create a virtual environment named 'env' (or another name of your choice) within the project directory, run:

```
python3 -m venv env
```

This action creates a new directory named 'env' which houses the virtual environment.  Remember to add 'env/' to your '.gitignore' file to prevent the environment from being tracked by version control.

3. Activate the Virtual Environment:
### MacOS/Linux:

```
source env/bin/activate
```
### Windows (Command Prompt):

```
.\env\Scripts\activate
```

Post activation, your terminal or command prompt will display the virtual environment's name ('env'), indicating that it's active.  For instance:

```
(env) username@hostname:path/to/your/project$
```

4. Installing Dependencies:
If your project contains a 'requirements.txt' file that lists it's dependencies, install them with `pip` after activating the virtual environment:

```
pip install -r requirements.txt
```

## Deactivating the Virtual Environment
To exit the virtual environment and revert back to the system-wide Python setup, run: 

```
deactivate
```

Post-deactivation, the terminal or command prompt won't display the virtual environment's name.

## Cloning and Setting Up on a New Computer
For shifting to a new computer or sharing the project:

1. Clone the repository or copy the project files.
2. Navigate to the project directory.
3. Follow the "Setting Up a New Virtual Environment" instructions mentioned above.

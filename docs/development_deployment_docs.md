# Development Deployment Docs

This document helps you to deploy this django task project for bitpin company on a debian based linux machine.


## Install required tools

Update and Upgrade the server.

```bash
sudo apt-get update
sudo apt-get upgrade
```

Install python and related tools

```bash
sudo apt install python3 python3-pip python3-setuptools python3-dev build-essential python3-venv
```

Make sure you are in the project directory or cd to the task project directory. and create a virtual environment named venv (**Note**: because venv is ignored in gitignore file, I recomend you to use same name to keep your environment alongside your project).

```bash
python3 -m venv venv
```

Activate the venv

```bash
source venv/bin/activate
```

upgrade the pip

```bash
pip3 install --upgrade pip
```

Install the requirements of the python project inside the virtual environment:

```bash
pip3 install -r requirements.txt
```

Change directory to bitpin django project

```bash
cd bitpin_task
```

run migrate to create database and tables initially

```bash
python3 manage.py migrate
```

Now you can run the development server for bitpin task

```bash
python3 manage.py runserver
```



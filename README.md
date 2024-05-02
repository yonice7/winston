# Lucas

Lucas is a program to that helps you to automate the control of your personal finances, saving you hours of transactions record entry, calculation, sheets editing, etc.

## Installation

### Set a virtual environment for macos

If you're using macos it's strongly recommended to set a virtual environment so you can still the modules using pip

```shell
# for practicity have this alias for python and pip in your .zshrc
alias python=python3
alias pip=pip3

# go to the dir ~/.local since all your config files should go there
cd ~/.local
# create the venv
python -m venv venv
# go to the venv dir
cd venv
# active the venv
source bin/activate
# deactive the venv
deactive
```

Once the environment is already activated go to the repository folder `cd /path/to/lucas` and install the required modules

```shell
# in ~/path/to/lucas/ repository run
pip install -r requirements.txt
```

Create your Gmail credentails, look the at the guide [here](https://developers.google.com/workspace/guides/create-credentials?hl=es-419#google-cloud-console)

```shell
# 1. download the json file
# 2. move to the lucas local repository
mv ~/Downloads/credential_name.json /path/to/lucas/google_credentials.json
```

## Usage

## Contribuiting

## License

[MIT](https://choosealicense.com/licenses/mit/)

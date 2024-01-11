# Python Toolbox 

## Compatibility
This code was written and tested with python 3.10.12 on ubuntu version 22.04.1.

## Functionality
- Change file extensions within a folder.
- Port scanning.
- Encrypt and Decrypt string messages
- Services scanning.

The functions are organized into files that has very suggestive names to what the functions perform. e.g. the functionality for encrypt and decrypt messages are implemented in a file called 'encrypt_decrypt_util.py', etc.

## Usage
Clone this project from github into a folder in your computer.

```
git clone ...
```

Create a Virtual Environment
```
cd python-toolbox
python3 -m venv venv
source venv/bin/activate
```
Install required libraries
```
pip install -r requirements.txt
```

See example of usage in the files 'examples.py'. In order to run the examples, just uncomment the block of code that you wish to run and, then, run the 'example.py' file.
```
python3 examples.py
```

## Extend the toolbox

Make your modifications e.g. create new functionalities, customize the existing functionality, etc. After making your modifications, you can run a linter that is configured, so the new code is pep8 compliant. You just need to run the shell script included in this repo:
```
sh run-autopep8.sh
```
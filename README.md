# Python Toolbox 

## Compatibility
This code was written and tested with python 3.10.12 on ubuntu version 22.04.1.

## Functionality
- Change file extensions within a folder.
- Port scanning.
- Encrypt and Decrypt string messages
- Services scanning.
- (Generate python code automatically with shell script and openai API).

The functions are organized into files that has very suggestive names to what the functions perform. e.g. the functionality for encrypt and decrypt messages are implemented in a file called 'encrypt_decrypt_util.py', etc.

## Usage
Clone this project from github into a folder in your computer.

```bash
git clone https://github.com/rasi10/python-toolbox.git
```

Create a Virtual Environment
```bash
cd python-toolbox
python3 -m venv venv
source venv/bin/activate
```
Install required libraries
```bash
pip install -r requirements.txt
```

See example of usage in the files 'examples.py'. In order to run the examples, just uncomment the block of code that you wish to run and, then, run the 'example.py' file.
```bash
python3 examples.py
```

## Extend the toolbox

Make your modifications e.g. create new functionalities, customize the existing functionality, etc. After making your modifications, you can run a linter that is configured, so the new code is pep8 compliant. You just need to run the shell script included in this repo:
```bash
sh run-autopep8.sh
```

In order to get a score to see how compliant the code is with pep8, you can run the script run-pylint.sh:
```bash
sh run-pylint.sh
```

## Generating code automatically
There is a script within the project called "run-generate-code.sh". This script takes one string as a parameter and use that string as a request towards openai API. With other words, you can request for code to be generated for you. E.g. the command bellow:

```bash
sh run-generate-code.sh "Write a hello world in python"
```

The comman above will create a python file under the folder 'generated_scripts/', called python_script.py. If it is a small script, it will most often work "out-of-the-box". Otherwise, if it is a little more complex script it may eventually require small modifications.

<div style="background-color: #8B0000; padding: 10px; border: 1px solid #ffcc00; border-radius: 5px;">
    <strong>NOTE:</strong> In order to use the script 'run-generate-code.sh', you need to create a .env file on the root folder of the project. The only variable required in there is "API_TOKEN", which your token to the openai API service.
</div>

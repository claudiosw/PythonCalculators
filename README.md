# About the project
This is a project to practice testing and clean code
# Preparing / Installing

### Clone the PythonCalculators repository
```
git clone https://github.com/claudiosw/PythonCalculators.git
```

### Access the project directory:
```
cd PythonCalculators
```

### Create the virtual environment:
```
python -m venv venv

```

### Run the virtual environment:
```
venv\Scripts\activate

```

### Install the required Python packages:
```
pip install -r requirements.txt
```

# Run the Server 

Run these commands to run the server

```
set FLASK_APP=src
flask run
```

# Test
Run this command to run the tests:

```
pytest
```

# Use
To use this application, you need to send HTTP POST to the server. One way to do a POST is using the program Postman.
## Use Calculator 1

Do a POST to the url http://127.0.0.1:5000/calculator_1

With this data in the body (you can change the number):
```
{"real_number": 1}
```

## Use Calculator 2

Do a POST to the url http://127.0.0.1:5000/calculator_2

With this data in the body (you can change the numbers):
```
{"list_real_numbers": [1, 2, 3]}
```
## Use Calculator 3

Do a POST to the url http://127.0.0.1:5000/calculator_3

With this data in the body (you can change the numbers):
```
{"list_real_numbers": [1, 2, 3]}
```
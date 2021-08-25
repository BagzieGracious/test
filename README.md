# test
This is just a challenge

Use the following endpoints to perform the specified tasks 
    
    EndPoint                                           | Functionality
    ------------------------                           | ----------------------
    Get /users/                                        | Fetch all users
    Post /users/                                       | Add all users
    Post /deposits/<user_id>                           | Deposit Amount
    Post /withdraws/<user_id>                          | withdraw Amount
    Post /transactions/<user_id>                       | Transact Amount
    
# Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone git@github.com:BagzieGracious/test.git
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ source venv/bin/activate
```
Install the dependencies in the requirements.txt file using pip
```sh
$ pip install -r requirements.txt
```

Start the application by running
```sh
$ python run.py
```
Run tests
```sh
$ pytest
```


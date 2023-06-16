# Automation
## _Apply Shares and Check Status_

![N|Solid](https://meroshare.cdsc.com.np/assets/img/brand-login.png)

## Add config.py in root directory

Add a file named config.py in the root directory.
Inside the file make a variable credentials which is a list of dictonaries

```sh
credentials = [
    {
        'dp_id'  : '',
        'username' : '',
        'password' : '',
        'crn' : '',
        'pin' : ''
    },
    {
        'dp_id'  : '',
        'username' : '',
        'password' : '',
        'crn' : '',
        'pin' : ''
    }
]
```
## How to Run the program ?
Note: Make sure you have python 3.6+ installed in your device.
### Create and activate virtual environment
For Windows:
```
python -m venv venv
venv\Scripts\activate
```
For Linux/Mac:
```
python3 -m venv venv
source ./venv/bin/activate
```

### Install requirements.txt
After activating the virtualenv, install the dependencies as follows:
```
pip install -r requirements.txt
```
For Linux/Mac, use `pip3` instead of `pip`.

### Run the program
```sh
python main.py
```
For Linux/Mac, use `python3` instead of `python`.

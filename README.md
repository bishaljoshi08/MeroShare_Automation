# Automation

## _Apply Shares and Check Status_

![N|Solid](https://meroshare.cdsc.com.np/assets/img/brand-login.png)

## Add config.py in root directory

Add a file named config.py in the root directory.
Inside the file make a variable credentials which is a list of dictinaries
Also in case you have multiple bank linked to the meroshare:
If to use the second bank place the name of the account holder in the list mult_bank_name
If to use the third bank place the name of the account holder in the list mult2_bank_name
Also despite having multiple banks lined to the account you dont need to add these variables if you are willing to apply from the first bank.
Note: Make sure that the name is same and all the letters should be caps.

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

mult_bank_name = ['RAM PRASAD POUDEL', 'BIDHYA DEVI BHANDARI']
mult2_bank_name = ['PUSHPA KAMAL DAHAL', 'RAVI LAMICHHANE']
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

### For Developers

Use the guidelines as specified below:

- Use [precommit](https://pre-commit.com/) to format your code before commit

  - Install precommit as follows

    ```bash
    pip install pre-commit
    ```

  - Now, install precommit git hooks scripts

    ```bash
    pre-commit install
    ```

  - Whenever you commit, pre-commit should be activated and certain changes will be made. Stage your changes and commit them as you normally would.

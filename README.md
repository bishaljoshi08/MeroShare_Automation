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
### Create Virtual Environment

### Install requirements.txt

### Run the program
```sh
python main.py
```

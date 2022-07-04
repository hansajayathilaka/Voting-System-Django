Install pipx
```commandline
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```
Install Brownie
```commandline
pipx install eth-brownie
```
Initialize Brownie Project
```commandline
brownie init
```
Compile Code
```commandline
brownie compile
```
Run scripts
```commandline
brownie scripts/file.py
```
By default, brownie use ganache-cli and create a temporary network.
Run Tests
```commandline
brownie test
brownie test -pdb # To get python console on fail
brownie test -S # More discriptive view
```
Get Network List
```commandline
brownie networks list
```


Brownie add account from cli
```commandline
brownie accounts new <account_name>
```
Brownie get account list and delete one
```commandline
brownie accounts list
brownie accounts delete <account_name>
```
Get Brownie Console
```commandline
brownie console
```
Access account from python added by cli
```python
account = accounts.load("<account_name>")
```
Install ganache-cli for local testing
```commandline
npm install -g ganache-cli
```

Deploy Contract
```commandline
brownie run scripts/deploy.py --network rinkeby
```
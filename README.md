# Voting System API with Blockchain
This project is a REST full API with django rest framework. It uses blockchain to store the voting.

### Note
1. Clone the project from [GitHub](https://github.com/hansajayathilaka/Voting-System-Django)
2. Create virtual environment and install all the dependencies `python -m venv venv && .\venv\Scripts\activate && pip install -r requirements.txt`
3. Run migrations `python manage.py migrate`
4. Create admin user `python manage.py createsuperuser`
5. Create `.env` file and add the below
```dotenv
# https://infura.io/
NETWORK_NAME=rinkeby
NETWORK_URL=https://rinkeby.infura.io/v3/xxxxxx

# Chain ID of the network
CHAIN_ID=x

# Public and private keys of the account to use for the owner of the contract
PUBLIC_KEY=0x0000000000000
PRIVATE_KEY=0x000000000000000000000

# https://infura.io/
WEB3_INFURA_PROJECT_ID=xxxxxxxxxxxxxxxxxx

# https://etherscan.io/myapikey
ETHERSCAN_TOKEN=xxxxxxxxxxxxxxxxxxxxx

PROJECT_NAME=VotingSystem

```
6. Deploy contract `python deploy.py`
7. Run `python manage.py runserver`

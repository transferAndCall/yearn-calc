# yaLINK Vault Info

## Setup

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## read.py

Set the environment variable `RPC_URL` to a mainnet JSONRPC provider URL

Run the following command, replacing "youraddress" with your actual address

The script can also be ran without a "youraddress"

```
python read.py youraddress
```

### Output

- **Health factor**: The current health factor of the vault
- **Vault balance**: The current balance of the vault
- **Vault supply**: The current supply of yaLINK tokens
- **Insurance fund**: The current balance of the insurance fund
- **Credit - Debt**: Balance of credit minus debt. If positive, the vault is profitable. If negative, the vault is not profitable.
- **Percent locked**: The amount of aLINK locked from safe withdrawals
- **Current yaLINK rate**: The amount of yaLINK earned when depositing (divide by this number) and aLINK earned when withdrawing (multiply by this number)
- **My balance (yaLINK)**: Your current yaLINK balance
- **My percentage share**: Your percentage share of the vault
- **Can withdraw (yaLINK)**: The amount you can withdraw from safe withdraw
- **Can withdraw (aLINK)**: The total amount of aLINK you can earn from withdrawing
- **Insurance gains**: The amount of aLINK you would gain if insurance is claimed


## harvest.py

Run ganache-cli with a fork of mainnet, unlocking the Yearn: Deployer's address

Replace PROJECT_ID with your Infura project ID

```
ganache-cli --fork https://mainnet.infura.io/v3/PROJECT_ID --unlock 0x2d407ddb06311396fe14d4b49da5f0471447d45c
```

Then run the following command

```
python harvest.py
```

### Output

- **Harvesting crops**: Info line to indicate the script is running
- **Calling harvest on the USDC strategy**: Ensures the USDC strategy has the latest gains
- **Calling yearn on the controller**: Ensures the controller (for the USDC vault) is up to date
- **Calling delegatedHarvest on the yaLINK vault**: Harvests the yaLINK vault
- **Rate Before**: The rate of getPricePerFullShare before calling harvest
- **Rate After**: The rate of getPricePerFullShare after calling harvest
- **Increase**: The percentage increase of the rate from before and after calling harvest

## insurance.py

Run ganache-cli with a fork of mainnet, unlocking the Yearn: Deployer's address

Replace PROJECT_ID with your Infura project ID

```
ganache-cli --fork https://mainnet.infura.io/v3/PROJECT_ID --unlock 0x2d407ddb06311396fe14d4b49da5f0471447d45c
```

Then run the following command

```
python insurance.py
```

### Output

- **Claiming insurance**: Info line to indicate the script is running
- **Calling claimInsurance on the delegated controller**: Transfers the insurance fund (aLINK) from the vault and sends it to the controller
- **Calling inCaseTokensGetStuck on the delegated controller**: Transfers the aLINK from the controller to the yearn deployer
- **Transferring aLINK to yaLINK vault**: Transfers the aLINK from the yearn deployer to the vault
- **Rate Before**: The rate of getPricePerFullShare before the insurance claim
- **Rate After**: The rate of getPricePerFullShare after the insurance claim
- **Increase**: The percentage increase of the rate from before and after the insurance claim

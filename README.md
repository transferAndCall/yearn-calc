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

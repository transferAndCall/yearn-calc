import os
import json
import sys
from web3 import Web3

import common

RPC_URL = os.getenv('RPC_URL')
w3 = Web3(Web3.HTTPProvider(RPC_URL))

def main():
    controller_contract = common.load_delegated_controller(w3)
    want = controller_contract.functions.want(common.yalink_vault_address).call()
    aave_contract = common.load_aave(w3)
    lending_pool = aave_contract.functions.getLendingPool().call()
    lending_pool_contract = common.load_lending_pool(w3, lending_pool)
    account_data = lending_pool_contract.functions.getUserAccountData(common.yalink_vault_address).call()
    print(f'Health factor:\t\t{account_data[7] / 1e18}')
    vault_contract = common.load_yalink_vault(w3)
    vault_balance = vault_contract.functions.balance().call()
    print(f'Vault balance:\t\t{vault_balance / 1e18}')
    total_supply = vault_contract.functions.totalSupply().call()
    print(f'Vault supply:\t\t{total_supply / 1e18}')
    rate = vault_contract.functions.getPricePerFullShare().call()
    locked = vault_contract.functions.locked().call()
    print(f'Percent locked:\t\t{locked / 1e18}')
    print(f'Current yaLINK rate:\t{rate / 1e18}')
    if (len(sys.argv) > 1):
        my_balance = vault_contract.functions.balanceOf(str(sys.argv[1])).call()
        print(f'My balance (yaLINK):\t{my_balance / 1e18}')
        can_withdraw = rate / 1e18 * my_balance / 1e18
        can_withdraw_yalink = vault_contract.functions.maxWithdrawal(str(sys.argv[1])).call()
        print(f'Can withdraw (yaLINK):\t{can_withdraw_yalink / 1e18}')
        print(f'Can withdraw (aLINK):\t{can_withdraw}')


if __name__ == '__main__':
    main()

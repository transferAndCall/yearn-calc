import os
import json
import sys
from web3 import Web3

import common

w3 = Web3(Web3.HTTPProvider('http://localhost:8545', request_kwargs={'timeout':10000}))

def main():
    w3.eth.defaultAccount = common.yearn_deployer
    print('Claiming insurance...')
    delegated_controller_contract = common.load_delegated_controller(w3)
    yalink_vault_contract = common.load_yalink_vault(w3)
    alink_contract = common.load_alink_contract(w3)
    rate_before = yalink_vault_contract.functions.getPricePerFullShare().call()
    print('Calling claimInsurance on the delegated controller...')
    txhash_claim = delegated_controller_contract.functions.claimInsurance(common.yalink_vault_address).transact({'gas':2000000})
    w3.eth.waitForTransactionReceipt(txhash_claim)
    print('Calling inCaseTokensGetStuck on the delegated controller...')
    balance_alink_controller = alink_contract.functions.balanceOf(common.delegated_controller_address).call()
    txhash_stuck = delegated_controller_contract.functions.inCaseTokensGetStuck(common.alink_address, balance_alink_controller).transact({'gas':2000000})
    w3.eth.waitForTransactionReceipt(txhash_stuck)
    print('Transferring aLINK to yaLINK vault...')
    txhash_transfer = alink_contract.functions.transfer(common.yalink_vault_address, balance_alink_controller).transact({'gas':2000000})
    w3.eth.waitForTransactionReceipt(txhash_transfer)
    rate_after = yalink_vault_contract.functions.getPricePerFullShare().call()
    print(f'Rate Before:\t{rate_before}')
    print(f'Rate After:\t{rate_after}')
    increase = rate_after - rate_before
    percent = increase / rate_before * 100
    print(f'Increase:\t{percent:.18f}%')


if __name__ == '__main__':
    main()

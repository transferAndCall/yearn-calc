import os
import json
import sys
from web3 import Web3

import common

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

def main():
    w3.eth.defaultAccount = common.yearn_deployer
    print('Harvesting crops...')
    usdc_strategy_contract = common.load_usdc_strategy(w3)
    controller_contract = common.load_controller(w3)
    delegated_controller_contract = common.load_delegated_controller(w3)
    yalink_vault_contract = common.load_yalink_vault(w3)
    rate_before = yalink_vault_contract.functions.getPricePerFullShare().call()
    print('Calling harvest on the USDC strategy...')
    txhash_harvest_usdc = usdc_strategy_contract.functions.harvest().transact()
    w3.eth.waitForTransactionReceipt(txhash_harvest_usdc)
    print('Calling yearn on the controller...')
    txhash_yearn = controller_contract.functions.yearn('0xA30d1D98C502378ad61Fe71BcDc3a808CF60b897', '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984', 1).transact()
    w3.eth.waitForTransactionReceipt(txhash_yearn)
    print('Calling delegatedHarvest on the yaLINK vault...')
    txhash_harvest = delegated_controller_contract.functions.delegatedHarvest('0x25fAcA21dd2Ad7eDB3a027d543e617496820d8d6', 1).transact()
    w3.eth.waitForTransactionReceipt(txhash_harvest)
    rate_after = yalink_vault_contract.functions.getPricePerFullShare().call()
    print(f'Rate Before:\t{rate_before}')
    print(f'Rate After:\t{rate_after}')
    increase = rate_after - rate_before
    percent = increase / rate_before * 100
    print(f'Increase:\t{percent:.18f}%')


if __name__ == '__main__':
    main()

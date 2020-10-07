yearn_deployer = '0x2D407dDb06311396fE14D4b49da5F0471447d45C'
aave_address = '0x24a42fD28C976A61Df5D00D0599C34c4f90748c8'
aave_abi = [ { "constant": "true", "inputs": [], "name": "getLendingPool", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "payable": "false", "stateMutability": "view", "type": "function" } ]
lending_pool_abi = [ { "constant": "true", "inputs": [ { "internalType": "address", "name": "_user", "type": "address" } ], "name": "getUserAccountData", "outputs": [ { "internalType": "uint256", "name": "totalLiquidityETH", "type": "uint256" }, { "internalType": "uint256", "name": "totalCollateralETH", "type": "uint256" }, { "internalType": "uint256", "name": "totalBorrowsETH", "type": "uint256" }, { "internalType": "uint256", "name": "totalFeesETH", "type": "uint256" }, { "internalType": "uint256", "name": "availableBorrowsETH", "type": "uint256" }, { "internalType": "uint256", "name": "currentLiquidationThreshold", "type": "uint256" }, { "internalType": "uint256", "name": "ltv", "type": "uint256" }, { "internalType": "uint256", "name": "healthFactor", "type": "uint256" } ], "payable": "false", "stateMutability": "view", "type": "function" } ]
yalink_vault_address = '0x29E240CFD7946BA20895a7a02eDb25C210f9f324'
yalink_vault_abi = [ { "constant": "true", "inputs": [], "name": "insurance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": "false", "stateMutability": "view", "type": "function" }, { "constant": "true", "inputs": [], "name": "balance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": "false", "stateMutability": "view", "type": "function" }, { "constant": "true", "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": "false", "stateMutability": "view", "type": "function" }, { "constant": "true", "inputs": [], "name": "getPricePerFullShare", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": "false", "stateMutability": "view", "type": "function" }, { "constant": "true", "inputs": [], "name": "locked", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": "false", "stateMutability": "view", "type": "function" }, { "constant": "true", "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "maxWithdrawal", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": "false", "stateMutability": "view", "type": "function" }, { "constant": "true", "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": "false", "stateMutability": "view", "type": "function" } ]
delegated_controller_address = '0x2be5D998C95DE70D9A38b3d78e49751F10F9E88b'
delegated_controller_abi = [ { "constant": "true", "inputs": [ { "internalType": "address", "name": "_vault", "type": "address" } ], "name": "want", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "payable": "false", "stateMutability": "view", "type": "function" }, { "constant": "false", "inputs": [ { "internalType": "address", "name": "_strategy", "type": "address" }, { "internalType": "uint256", "name": "parts", "type": "uint256" } ], "name": "delegatedHarvest", "outputs": [], "payable": "false", "stateMutability": "nonpayable", "type": "function" } ]
controller_address = '0x9E65Ad11b299CA0Abefc2799dDB6314Ef2d91080'
controller_abi = [ { "constant": "false", "inputs": [ { "internalType": "address", "name": "_strategy", "type": "address" }, { "internalType": "address", "name": "_token", "type": "address" }, { "internalType": "uint256", "name": "parts", "type": "uint256" } ], "name": "yearn", "outputs": [], "payable": "false", "stateMutability": "nonpayable", "type": "function" } ]
usdc_strategy_address = '0xA30d1D98C502378ad61Fe71BcDc3a808CF60b897'
usdc_strategy_abi = [ { "constant": "false", "inputs": [], "name": "harvest", "outputs": [], "payable": "false", "stateMutability": "nonpayable", "type": "function" }, ]

def load_controller(w3):
    return w3.eth.contract(abi=controller_abi, address=controller_address)

def load_delegated_controller(w3):
    return w3.eth.contract(abi=delegated_controller_abi, address=delegated_controller_address)

def load_yalink_vault(w3):
    return w3.eth.contract(abi=yalink_vault_abi, address=yalink_vault_address)

def load_usdc_strategy(w3):
    return w3.eth.contract(abi=usdc_strategy_abi, address=usdc_strategy_address)

def load_aave(w3):
    return w3.eth.contract(abi=aave_abi, address=aave_address)

def load_lending_pool(w3, lending_pool):
    return w3.eth.contract(abi=lending_pool_abi, address=lending_pool)

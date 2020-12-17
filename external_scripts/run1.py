from web3 import Web3, HTTPProvider
import os
import json
import pprint

# -------------------------- Connect to Dev network -------------------------- #

w3 = Web3(HTTPProvider("http://127.0.0.1:7545",
                       request_kwargs={'timeout': 60}))
print(f"Web3 is connected : {w3.isConnected()}")

# --------------------------------- Utilities -------------------------------- #


def fromWei(amount):
    return w3.fromWei(amount, "ether")

# --------------------------- Get the contract abi --------------------------- #

abi_path = "./vapp/src/contracts/"
with open(os.path.join(abi_path, 'TokenHolderPayer.json'), "r") as file:
    property_contract_compiled = json.load(file)
    property_contract_abi = property_contract_compiled['abi']
    property_contract_bytecode = property_contract_compiled['bytecode']
# --------------------------- Import some accounts --------------------------- #

accounts = w3.eth.accounts

# ------------------------------ Deploy contract ----------------------------- #

TokenHolder = w3.eth.contract(
    abi=property_contract_abi, bytecode=property_contract_bytecode)
tx_hash = TokenHolder.constructor("Property Name", "RET").transact({"from":accounts[0]})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

property_contract = w3.eth.contract(
    address=tx_receipt.contractAddress, abi=property_contract_abi)

print(f"Contract address : {property_contract.address}")

# ---------------------------- let mint some tokens --------------------------- #

property_contract.functions.mint(accounts[0], 1000).transact({'from': accounts[0], 'gas': 420000, 'gasPrice': 21000})
total_supply = property_contract.functions.totalSupply().call()
token_balance = property_contract.functions.balanceOf(accounts[0]).call()
print(f"Token balance : {token_balance} of {total_supply}")

# ----------------------------------- Misc ----------------------------------- #

# balance_1 = w3.eth.getBalance(account_1.address)
# balance_2 = w3.eth.getBalance(account_2.address)
# print(f"account_1 balance = {fromWei(balance_1)} ETH")
# print(f"account_2 balance = {fromWei(balance_2)} ETH")

# broker_address = "0x40952C36E39596ab268C70635AA49DE87968E652"
# with open(os.path.join(abi_path, 'Broker.json'), "r") as file:
#     broker_abi = json.load(file)

# broker = w3.eth.contract(address=broker_address, abi=broker_abi)

# dir(broker.functions)

from web3 import Web3, HTTPProvider
import json
import os


w3 = Web3(HTTPProvider("http://127.0.0.1:7545",
                       request_kwargs={'timeout': 60}))
print(f"Web3 is connected : {w3.isConnected()}")

accounts = w3.eth.accounts
# ------------------------------- get contract ------------------------------- #
abi_path = "./vapp/src/contracts/"
with open(os.path.join(abi_path, 'TokenHolderPayer.json'), "r") as file:
    property_contract_compiled = json.load(file)
    property_contract_abi = property_contract_compiled['abi']


contract_address = "0xE5972821D1218120C4E98986A3eEc997931690b4"

property_contract = w3.eth.contract(address=contract_address, abi=property_contract_abi)

# ------------------- buy some token from realestate agent ------------------- #
amount = 500 

# Allow token to be sent
property_contract.functions.increaseAllowance(accounts[1], amount).transact({'from':accounts[0], 'gas': 420000, 'gasPrice': 21000})

balance = property_contract.functions.balanceOf(accounts[1]).call()
print(f"initial balance {balance}")
tx_hash = property_contract.functions.transferFrom(accounts[0], accounts[1], 500).transact({'from':accounts[1], 'gas': 420000, 'gasPrice': 21000})
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
balance = property_contract.functions.balanceOf(accounts[1]).call()
print(f"final balance {balance}")



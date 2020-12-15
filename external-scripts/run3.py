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


contract_address = "0x50E31f6307E958d20a90b68FE3593259783aE9Ff"

property_contract = w3.eth.contract(address=contract_address, abi=property_contract_abi)

# --------------------- put money on contract for gas fee -------------------- #
nonce = w3.eth.getTransactionCount(accounts[3])
private_key = accounts[3]._private

tx = {
    'nonce': nonce,
    'to': property_contract.address,
    'value': w3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei'),
}
signed_tx = w3.eth.account.signTransaction(tx, "b0f85de30ba2409d6f641c7e91739d682ae61d12056ed6debb7e629b6b272310")
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

# ------------------------------- split payment ------------------------------ #
value = w3.toWei(10, "ether")
balance_eth = w3.eth.getBalance(accounts[1])
print(balance_eth)
property_contract.functions.splitPayement().transact({'from':accounts[0], 'gas': 840000, 'gasPrice': 21000, "value":value})
balance_eth = w3.eth.getBalance(accounts[1])
print(balance_eth)
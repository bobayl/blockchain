from bitcoinlib.wallets import Wallet, wallet_delete, wallet_create_or_open
from bitcoinlib.transactions import *


# Create or open Wallets (Wallet1, Wallet2)
w3 = wallet_create_or_open('Wallet3', network='testnet', witness_type='segwit')
w4 = wallet_create_or_open('Wallet4', network='testnet', witness_type='segwit')

# Get the keys and addresses:
key3 = w3.get_key()
address3 = key3.address
key4 = w4.get_key()
address4 = key4.address
print("**** Wallet3 Address ****")
print(address3)
print(key3)
print("**** Wallet4 Address ****")
print(address4)
print(key4)
print("********")

# Scan Wallet1 for transactions and UTXOs:
w3.scan()
w4.scan()
print("**** Wallet Info ****")
print(w3.info())
print(w4.info())
print("**** UTXOS updating... ****")
w3.utxos_update()
w4.utxos_update()
print("**** UTXOS ****")
print(w3.utxos())
print(w3.utxos())

# Create transaction:
print("**** Transaction t1 ***")
t = w3.send_to('tb1q7c2ajtymf56g8yqel7lelqy99rtnwxmuh7fttm', 300000, fee=1500)
print(t.info())
print(t.pushed)

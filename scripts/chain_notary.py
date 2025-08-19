"""Store model hashes on Ethereum for auditability."""

from web3 import Web3


def notarize_model(model_hash):
    """Writes hash to blockchain."""
    w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_KEY"))
    contract = w3.eth.contract(address="0x...", abi=...)
    tx_hash = contract.functions.storeHash(model_hash).transact()
    return tx_hash

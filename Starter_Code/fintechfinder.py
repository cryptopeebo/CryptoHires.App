# 🌐 Decentralized Talent Showcase: CryptoHires Universe
################################################################################

# 📚 Cosmic Libraries
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account, Web3
from web3.gas_strategies.time_based import medium_gas_price_strategy

# 🛸 Core Space Functions for Interstellar Wallet Transactions
################################################################################

def forge_eth_account():
    """Carve a space wallet and an Ethereum account using cosmic seed phrase."""
    mnemonic = os.getenv("MNEMONIC")
    space_wallet = Wallet(mnemonic)
    private_key, public_key = space_wallet.derive_account("eth")
    eth_account = Account.privateKeyToAccount(private_key)
    return eth_account

def retrieve_eth_reserve(w3_instance, eth_address):
    """Beam Ether balance for a given Ethereum space address."""
    balance_in_wei = w3_instance.eth.get_balance(eth_address)
    balance_in_eth = w3_instance.fromWei(balance_in_wei, "ether")
    return balance_in_eth

def launch_eth_transfer(w3_instance, eth_account, recipient, wage_in_eth):
    try:
        # Convert wage to cosmic Wei
        value_in_wei = w3_instance.toWei(wage_in_eth, "ether")

        # Estimate Stellar Gas
        gas_estimate = w3_instance.eth.estimateGas({
            "from": eth_account.address,
            "to": recipient,
            "value": value_in_wei
        })

        # Craft Interstellar Transaction
        txn_details = {
            "from": eth_account.address,
            "to": recipient,
            "value": value_in_wei,
            "gas": gas_estimate,
            "gasPrice": w3_instance.eth.gasPrice,
            "nonce": w3_instance.eth.getTransactionCount(eth_account.address),
        }

        # Sign & Propel through Space
        signed_txn = w3_instance.eth.account.signTransaction(txn_details, eth_account.privateKey)
        return w3_instance.eth.sendRawTransaction(signed_txn.rawTransaction)
    except ValueError as e:
        if 'insufficient funds' in str(e):
            return "Error: Not enough cosmic fuel to propel transaction."
        else:
            return f"Error: {e}"

# 🎇 Starlit App Galaxy
################################################################################

# 🌟 Stellar Interface
import streamlit as st

# 🌌 Web3 Intergalactic Initialization
load_dotenv()
web3_instance = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# 📖 Star Maven Directory
stellar_talents = {
    "Nebula Paystream": ["Nebula Paystream", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", 0.20, "Images/Nebula.jpeg"],
    "AngelCash Shadow": ["AngelCash Shadow", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", 0.33, "Images/angelcashshadow.jpeg"],
    "MoonVault Obscura": ["MoonVault Obscura", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", 0.19, "Images/MoonVault .jpeg"],
    "VoltGem Twins": ["VoltGem Twins", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", 0.16, "Images/VoltGemTwins.jpeg"],
}

# 📜 Stellar Names
talent_names = list(stellar_talents.keys())

# 🎇 Starlit Display
def beam_up_talents():
    """Illuminate the interstellar fintech professionals."""
    talent_list = list(stellar_talents.values())
    for idx in range(len(talent_names)):
        st.image(talent_list[idx][4], width=200)
        st.write("Star Alias: ", talent_list[idx][0])
        st.write("Galactic Address: ", talent_list[idx][1])
        st.write("Cosmic Rating: ", talent_list[idx][2])
        st.write("Stellar Rate: ", talent_list[idx][3], " ETH/hr")
        st.text(" ")

# 🎉 Starlit Portal Creation
st.title("CryptoHires Universe: Stellar Talent Constellation")
st.markdown("### Embark on a Galactic Voyage with Fintech Star Mavens!")
st.text(" ")

# 🎨 Stellar Sidebar
st.sidebar.title("Client's Galactic Finances")
eth_account = forge_eth_account()
st.sidebar.write("Space Address: ", eth_account.address)
st.sidebar.write("Etherium Vault: ", retrieve_eth_reserve(web3_instance, eth_account.address), "ETH")

# 🎯 Star Selection
selected_talent = st.sidebar.selectbox("Pick Your Star Maven", talent_names)
worked_hours = st.sidebar.number_input("Galactic Work Duration (in hours)")

# 📝 Stellar Info
chosen_star = stellar_talents[selected_talent]
st.sidebar.write("Star Maven: ", chosen_star[0])
hourly_fee = chosen_star[3]
st.sidebar.write("Rate (ETH/hr): ", hourly_fee)
recipient_address = chosen_star[1]
st.sidebar.write("Recipient's Galactic Address: ", recipient_address)

# 💰 Stellar Compensation Calculation
total_wage = hourly_fee * worked_hours
st.sidebar.write("Total Stellar Compensation (in ETH): ", total_wage)

# 💸 Cosmic Transaction
if st.sidebar.button("Reward Star Maven"):
    transaction_receipt = launch_eth_transfer(web3_instance, eth_account, recipient_address, total_wage)
    st.sidebar.write("Intergalactic Transaction Successful! Receipt: ", transaction_receipt)
    st.balloons()

# 🌟 Fire up Starlit Portal
beam_up_talents()

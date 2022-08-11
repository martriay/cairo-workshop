from nile.utils import *

ALIAS = "uwu_token"
decimals = 18

def run(nre):
    account_a = nre.get_or_deploy_account("ACCOUNT_A")
    account_b = nre.get_or_deploy_account("ACCOUNT_B")
    token_address, _ = nre.get_deployment(ALIAS)
    
    print_balance(nre, account_a.address, 'a')
    print_balance(nre, account_b.address, 'b')

    recipient = from_hex(account_b.address)
    amount = to_uint(to_decimals(0.5))

    print(f"transfer {from_decimals(from_uint(amount))} to {account_b.address}")
    account_a.send(token_address, 'transfer', [recipient, *amount], max_fee=0)

    print_balance(nre, account_a.address, 'a')
    print_balance(nre, account_b.address, 'b')


def get_balance(nre, address):
    balance = nre.call(ALIAS, "balanceOf", [from_hex(address)])[0]
    return from_hex(balance)

def print_balance(nre, address, alias):
    balance = get_balance(nre, address)
    print(f"balance {alias}", from_decimals(balance))

def from_decimals(x):
    return x / (10 ** decimals)

def to_decimals(x):
    return x * (10 ** decimals)

def from_hex(x):
    return int(x, 16)

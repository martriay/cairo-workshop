from nile.utils import *

ALIAS = "uwu_token"
decimals = 18

def run(nre):
    account_a = nre.get_or_deploy_account("ACCOUNT_A")

    name = str_to_felt("UwuToken")
    symbol = str_to_felt("UWU")
    initial_supply = to_uint(to_decimals(1337))
    recipient = int(account_a.address, 16)

    arguments = [
        name,
        symbol,
        decimals,                         
        *initial_supply,
        recipient
    ]

    token_address, _ = nre.deploy("UwuToken", arguments, alias=ALIAS)
    print("UwuToken deployeado en", token_address)

    supply = from_hex(nre.call("uwu_token", "totalSupply")[0])
    print("total supply:", from_decimals(supply))

    name = nre.call("uwu_token", "name")[0]
    print("token name:", felt_to_str(name))

    symbol = nre.call("uwu_token", "symbol")[0]
    print("token symbol:", felt_to_str(symbol))


def from_decimals(x):
    return x / (10 ** decimals)

def to_decimals(x):
    return x * (10 ** decimals)

def from_hex(x):
    return int(x, 16)

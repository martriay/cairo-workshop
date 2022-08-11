# Getting Started with Cairo (workshop) 👶🏻✨

This repository works as an introductory guide to develop StarkNet smart contracts with the [Cairo](cairo-lang.org) programming language, the [OpenZeppelin Contracts for Cairo](https://github.com/OpenZeppelin/cairo-contracts/) library, and the [Nile](https://github.com/OpenZeppelin/nile/) development environment.

## 1. Installation

### First time?

Before installing Cairo on your machine, you need to install `gmp`:

```bash
sudo apt install -y libgmp3-dev # linux
brew install gmp # mac
```

> If you have any troubles installing gmp on your Apple M1 computer, [here’s a list of potential solutions](https://github.com/OpenZeppelin/nile/issues/22).

### Set up your project

Create a directory for your project, then `cd` into it and create a Python virtual environment.

```bash
mkdir cairo-workshop
cd cairo-workshop
python3 -m venv env
source env/bin/activate
```

Install the [Nile](https://github.com/OpenZeppelin/nile) development environment and the [OpenZeppelin Contracts](https://github.com/OpenZeppelin/cairo-contracts/).

```bash
pip install cairo-nile openzeppelin-cairo-contracts
```

Run `init` to kickstart a new project. Nile will create the project directory structure and install [the Cairo language](https://www.cairo-lang.org/docs/quickstart.html), a [local network](https://github.com/Shard-Labs/starknet-devnet/), and a [testing framework](https://docs.pytest.org/en/6.2.x/).
```bash
nile init
```

## 2. Deploy a preset

Rename `contracts/contract.cairo` to `contracts/UwuToken.cairo` and replace its contents with:

```cairo
%lang starknet

from openzeppelin.token.erc20.presets.ERC20 import constructor
```

What this does is to import the [ERC20 basic preset](https://github.com/OpenZeppelin/cairo-contracts/blob/ad399728e6fcd5956a4ed347fb5e8ee731d37ec4/src/openzeppelin/token/erc20/presets/ERC20.cairo) and re-exporting it.

That's it! That's our basic ERC20 contract. Let's try to compile it:

```
(env) ➜  workshop nile compile
📁 Creating artifacts/abis to store compilation artifacts
🤖 Compiling all Cairo contracts in the contracts directory
🔨 Compiling contracts/UwuToken.cairo
✅ Done
```

Magic ✨

## 3. Deploy it (with a script!)

Let's now try to deploy our contract. Although we could simply use `nile deploy` like this:

```bash
nile deploy UwuToken <name> <symbol> <decimals> <initial_supply> <recipient> --alias uwu_token
```

Truth is that there's still some representation issues to overcome:
- strings (`name` and `symbol`) need to be converted to an integer representation first
- uint256 values such as `initial_supply` need to be represented by two `felt`s since they're just 252bits

To overcome this issues, it's easier to write a deployment script instead of using the CLI directly. Therefore we need to create a `scripts/` directory and create a `deploy.py` file in it:

> Note: you can find this script already written in this repo

```python
# scripts/deploy.py
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
    print("UwuToken deployed at", token_address)

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
```



## 4. Write a custom contract (i.e. extend a library)

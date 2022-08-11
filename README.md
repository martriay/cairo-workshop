# [Workshop] Getting Started with Cairo

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

Install the [Nile](https://github.com/OpenZeppelin/nile) development environment and then run `init` to kickstart a new project. Nile will create the project directory structure and install [the Cairo language](https://www.cairo-lang.org/docs/quickstart.html), a [local network](https://github.com/Shard-Labs/starknet-devnet/), and a [testing framework](https://docs.pytest.org/en/6.2.x/).

```bash
pip install cairo-nile openzeppelin-cairo-contracts
nile init
```

## 2. Deploy a preset



## 3. Write a script

## 4. Write a custom contract (i.e. extend a library)

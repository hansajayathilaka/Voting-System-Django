import os

from brownie import accounts, config, network, project


def get_owner():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def connect_network(network_name=os.getenv("NETWORK_NAME")):
    network.connect(network_name)


def load_project(location="ethereum", name=os.getenv("PROJECT_NAME")):
    VotingSystem = project.load(location, name=name)
    VotingSystem.load_config()

    connect_network(os.getenv("NETWORK_NAME"))
    return VotingSystem


def get_project():
    return getattr(project, os.getenv("PROJECT_NAME"))

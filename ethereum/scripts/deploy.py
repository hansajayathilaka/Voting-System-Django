from brownie import config, network
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

from ethereum.scripts.utils import get_owner, load_project


def deploy_vote_storage():
    VotingSystem = load_project('../../ethereum')

    # gas_strategy = LinearScalingStrategy("10 gwei", "50 gwei", 1.5)
    voteStorage = VotingSystem.DynamicVoteStorage.deploy(
        {
            'from': get_owner(),
            # 'gas_price': gas_price(gas_strategy)
        },
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f'Contract deployed to {voteStorage.address}')


def main():
    deploy_vote_storage()

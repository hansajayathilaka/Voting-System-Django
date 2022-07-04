from datetime import datetime

from brownie import Wei
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

from ethereum.scripts.utils import get_owner, get_project

gas_strategy = LinearScalingStrategy(Wei('10 gwei'), Wei('50 gwei'), 2)


def create_election(election_id, start_date: datetime, end_date: datetime, candidates: list):
    VotingSystem = get_project()
    transaction = VotingSystem.DynamicVoteStorage[-1].create_election(
        election_id,
        start_date.timestamp(),
        end_date.timestamp(),
        candidates,
        {
            'from': get_owner(),
            # 'gas_price': gas_price(gas_strategy)
        }
    )
    transaction.wait(1)
    return transaction


def create_vote(election_id, voter_id, candidate_index):
    VotingSystem = get_project()
    transaction = VotingSystem.DynamicVoteStorage[-1].create_vote(
        election_id,
        voter_id,
        candidate_index,
        {
            'from': get_owner(),
            'gasLimit': 50000,
        }
    )
    transaction.wait(1)
    return transaction


def get_result(election_id, candidate_id):
    VotingSystem = get_project()
    res = VotingSystem.DynamicVoteStorage[-1].get_vote(election_id, candidate_id)
    return res


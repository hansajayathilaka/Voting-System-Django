from asyncore import read
from brownie import accounts, config, VoteStorage, network # type: ignore


def read_contract():
    return VoteStorage[-1]


def main():
    voteStorage = read_contract()
    res = voteStorage.get_result(0)
    print(res)

// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./VoteStorage.sol";


contract DynamicVoteStorage {

    address public owner;
    mapping(uint256 => address) private voteStorages;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Permission denied.");
        _;
    }

    function create_election(uint256 election_id, uint start_date, uint end_date, uint256[] memory candidates) public onlyOwner {
        VoteStorage voteStorage =  new VoteStorage(start_date, end_date, candidates);
        voteStorages[election_id] = address(voteStorage);
    }

    function create_vote(uint256 election_id, uint256 user_id, uint256 candidate_id) public onlyOwner {
        address election_address = voteStorages[election_id];
        VoteStorage voteStorage = VoteStorage(election_address);
        voteStorage.create_vote(user_id, candidate_id);
    }

    function get_vote(uint256 election_id, uint256 candidate_id) public view returns(uint256) {
        address election_address = voteStorages[election_id];
        VoteStorage voteStorage = VoteStorage(election_address);
        return voteStorage.get_vote(candidate_id);
    }

}

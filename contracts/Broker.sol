// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

import "@openzeppelin/contracts/presets/ERC1155PresetMinterPauser.sol";

contract Broker is ERC1155PresetMinterPauser {
    event Log(
        address indexed _from,
        string message
    );

    constructor(string memory uri) ERC1155PresetMinterPauser(uri) {
        emit Log(msg.sender, "Deployed");
    }
}

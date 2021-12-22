// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract StructTest {

    struct TestStructType {
        uint256 number;
        bool b;
        string text;
    }

    function testStructEncoding(TestStructType memory _testStruct) pure external returns(uint256, bool, string memory) {
        return (_testStruct.number, _testStruct.b, _testStruct.text);
    }

}
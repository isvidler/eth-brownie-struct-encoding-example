// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract StructTest {

    struct TestStructType {
        uint256 n;
        bool b;
        string t;
        address a;
        uint256[] i;
    }

    function testStructEncoding(TestStructType memory _testStruct) 
    pure 
    external 
    returns(
        uint256, 
        bool, 
        string memory, 
        address,
        uint256[] memory
    ) {
        return (_testStruct.n, _testStruct.b, _testStruct.t, _testStruct.a, _testStruct.i);
    }

}
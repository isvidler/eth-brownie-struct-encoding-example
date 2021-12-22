# `eth-brownie` struct encoding example

## Overview
This repository contains an example of encoding a struct, so that it can be used in a function call, using the `eth-brownie` framework for Solidity smart contract development (https://github.com/eth-brownie/brownie).

## Running tests
Run `brownie test`

## Files
1. [`contracts/StructTest.sol`](https://github.com/isvidler/eth-brownie-struct-encoding-example/blob/94535442ec94e7bb9d58da45f89b859f3c9f2027/contracts/StructTest.sol) - contains the test smart contract that defines a struct type, and a `pure` function that accepts the struct type as an argument, and returns its values as a tuple.
2. [`tests/test_struct_encoding.py`](https://github.com/isvidler/eth-brownie-struct-encoding-example/blob/94535442ec94e7bb9d58da45f89b859f3c9f2027/tests/test_struct_encoding.py) - contains a test which does the actual struct encoding and function calling.

## How to encode structs with `eth-brownie`
`brownie` actually handles encoding for you, in almost all cases. To call a smart contract function that accepts a struct as a parameter, pass in a tuple that contain the correct data types in order.

Refer to the [`test_struct` test](https://github.com/isvidler/eth-brownie-struct-encoding-example/blob/94535442ec94e7bb9d58da45f89b859f3c9f2027/tests/test_struct_encoding.py#L16 ) in [`tests/test_struct_encoding.py`](https://github.com/isvidler/eth-brownie-struct-encoding-example/blob/94535442ec94e7bb9d58da45f89b859f3c9f2027/tests/test_struct_encoding.py) for an example.
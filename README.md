# eth-brownie struct encoding example

## Overview
This repository contains an example of encoding a struct, so that it can be used in a function call, using the `eth-brownie` framework for Solidity smart contract development (https://github.com/eth-brownie/brownie).

## Files
1. `contracts/StructTest.sol` - contains the test smart contract that defines a struct type, and a `pure` function that accepts the struct type as an argument, and returns its values as a tuple.
2. `tests/test_struct_encoding.py` - contains a test which does the actual struct encoding and function calling.

## How to encode structs with `eth-brownie`
TODO
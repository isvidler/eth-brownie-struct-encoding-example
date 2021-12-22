# `eth-brownie` struct encoding example

## Overview
This repository contains an example of encoding a struct, so that it can be used in a function call, using the `eth-brownie` framework for Solidity smart contract development (https://github.com/eth-brownie/brownie).

## Running tests
Run `brownie test`

## Files
1. [`contracts/StructTest.sol`](https://github.com/isvidler/eth-brownie-struct-encoding-example/blob/94535442ec94e7bb9d58da45f89b859f3c9f2027/contracts/StructTest.sol) - contains the test smart contract that defines a struct type, and a `pure` function that accepts the struct type as an argument, and returns its values as a tuple.
2. [`tests/test_struct_encoding.py`](https://github.com/isvidler/eth-brownie-struct-encoding-example/blob/94535442ec94e7bb9d58da45f89b859f3c9f2027/tests/test_struct_encoding.py) - contains a test which does the actual struct encoding and function calling.

## How to encode structs with `eth-brownie`
`brownie` actually handles encoding for you, in almost all cases. To call a smart contract function that accepts a struct as a parameter, pass in a tuple that contains the correct data types in order.

Refer to the [`test_struct` test](https://github.com/isvidler/eth-brownie-struct-encoding-example/blob/94535442ec94e7bb9d58da45f89b859f3c9f2027/tests/test_struct_encoding.py#L16 ) in [`tests/test_struct_encoding.py`](https://github.com/isvidler/eth-brownie-struct-encoding-example/blob/94535442ec94e7bb9d58da45f89b859f3c9f2027/tests/test_struct_encoding.py) for an example.

## How did I figure this out?
No documentation exists on encoding structs in `brownie` (that I could find). The intuition came from knowing how Solidity encodes structs, which is just a packed encoding, where each variable in the struct is stored sequentially. I guessed that `brownie` would just transparent accept the variables with the correct data type in order, and it happened to work.

## What about ApeSafe?
ApeSafe uses `brownie` under the hood -- specifically the `brownie.Contract` class for crafting transactions, which is what we're also using in our tests. So, in theory, encoding structs should function exactly the same.

ApeSafe is being a pain to set up, so I haven't been able to directly test it, but it should be the same.
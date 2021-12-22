import pytest
from brownie import accounts, StructTest

@pytest.fixture(scope="module", autouse=True)
def test_struct_contract() -> StructTest:
    return accounts[0].deploy(StructTest)

@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    """Isolate each test's environment automatically. Effectively resets state of Blockchain, without
    requiring the redeployment of the contracts.
    """
    # Intentionally left blank -- no implementation is needed
    pass

def test_struct(test_struct_contract: StructTest):
    n = 775
    b = False
    t = 'test'
    a = '0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87'
    i = [9, 9, 2, 4, 6]

    # This is the key part
    # In python, represent the struct as a tuple with the correct data types in order
    struct = (n, b, t, a, i)
    assert (n, b, t, a, i) == test_struct_contract.testStructEncoding(struct)

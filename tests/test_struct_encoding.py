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
    assert (n, b, t) == test_struct_contract.testStructEncoding((n, b ,t))
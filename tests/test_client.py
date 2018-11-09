import os
import pytest

try:
    MSPKC_TESTKEY = os.environ['MSPKC_TESTKEY']
    MSPKC_TESTURL = os.environ['MSPKC_TESTURL']
except KeyError:
    raise KeyError("MSPKC_TESTKEY and MSPKC_TESTURL env vars must be defined to perform the tests")


def test_client():
    pass

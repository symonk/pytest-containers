from pytest_containers import is_xdist_worker
from pytest_containers.constants import EnvironmentVars
from pytest_containers.constants import Constants
import pytest


def test_is_master(monkeypatch: pytest.MonkeyPatch):
    with monkeypatch.context() as patcher:
        patcher.setenv(EnvironmentVars.PYTEST_XDIST_WORKER, Constants.MASTER)
        assert is_xdist_worker()
    

def test_is_not_master():
    assert not is_xdist_worker()
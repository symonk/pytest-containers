import pytest

from pytest_containers import is_xdist_worker
from pytest_containers.constants import Constants
from pytest_containers.constants import EnvironmentVars


def test_is_master(monkeypatch: pytest.MonkeyPatch):
    with monkeypatch.context() as patcher:
        patcher.setenv(EnvironmentVars.PYTEST_XDIST_WORKER, Constants.MASTER)
        assert is_xdist_worker()


def test_is_not_master(monkeypatch: pytest.MonkeyPatch):
    with monkeypatch.context() as patcher:
        patcher.setenv(EnvironmentVars.PYTEST_XDIST_WORKER, "gw0")
        assert not is_xdist_worker()

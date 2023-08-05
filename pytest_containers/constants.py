from enum import Enum


class Constants(str, Enum):
    """String constants"""

    MASTER = "master"
    
    
class EnvironmentVars(str, Enum):
    """Environment Variable Lookups"""
    PYTEST_XDIST_WORKER = "PYTEST_XDIST_WORKER"
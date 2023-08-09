from abc import ABC, abstractmethod
from typing import Generic, Tuple
from mbpo.utils.type_aliases import OptimizerState, OptimizerTrainingOutPut
import chex
from mbpo.systems.base_systems import System, SystemParams


class BaseOptimizer(ABC, Generic[OptimizerState, OptimizerTrainingOutPut]):
    def __init__(self, system: System):
        self.system = system
        pass

    @abstractmethod
    def act(self, obs: chex.Array, opt_state: OptimizerState, system_params: SystemParams, evaluate: bool = True) ->\
            Tuple[chex.Array, OptimizerState]:
        pass

    def train(self, opt_state: OptimizerState, *args, **kwargs) -> OptimizerTrainingOutPut:
        return opt_state

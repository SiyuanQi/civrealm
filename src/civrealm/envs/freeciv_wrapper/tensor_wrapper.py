import numpy as np

from civrealm.envs import FreecivBaseEnv
from civrealm.envs.freeciv_wrapper.config import default_tensor_config

from .action_wrapper import TensorAction
from .core import Wrapper
from .observation_wrapper import CacheLastObs, TensorObservation
from .tensor_base_wrapper import TensorBase


class TensorWrapper(Wrapper):
    """
    Tensor wrapper that composes `TensorBase`, `TensorAction`, `TensorObservation`
    and `CacheLastObs`.

    Parameters
    ----------
    env
    config:
        tensor env configuration

    Attributes
    ----------
    config: dict
        tensor wrapper configuration

    """

    def __init__(self, env: FreecivBaseEnv, config: dict = default_tensor_config):
        self.config = config
        super().__init__(
            CacheLastObs(
                TensorObservation(TensorAction(TensorBase(env, config=config)))
            )
        )

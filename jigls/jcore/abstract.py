from jigls.jeditor.utils import UniqueIdentifier
from typing import Dict, List, Optional
from uuid import UUID


class JAbstractBase:
    def __init__(
        self,
        name: str,
        uid: Optional[str] = None,
        exec: bool = True,
        traceback: bool = False,
    ) -> None:
        self._name: str = name
        self._uid: str = UniqueIdentifier() if uid is None else uid
        self._exec: bool = exec  # control flag to enable or disable
        self._traceback: bool = traceback

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def uid(self):
        return self._uid

    @property
    def exec(self):
        return self._exec

    @exec.setter
    def exec(self, value: bool) -> None:
        self._exec = value

    @property
    def traceback(self):
        return self._traceback

    @traceback.setter
    def traceback(self, value: bool) -> None:
        self._traceback = value

    def __repr__(self) -> str:
        return "name:%s uid:%s exec:%s" % (self._name, self._uid, self._exec)


class JAbstractOperation(object):
    def __init__(
        self,
        name: str = str(),
        inputs: List[str] = list(),
        outputs: List[str] = list(),
        params: Dict = {},
    ):

        self._name: str = name
        self._inputs: List[str] = inputs
        self._outputs: List[str] = outputs
        self._params: Dict = params

    @property
    def name(self):
        return self._name

    @property
    def inputs(self):
        return self._inputs

    @property
    def outputs(self):
        return self._outputs

    @property
    def params(self):
        return self._params

    def Compute(self, inputs):
        raise NotImplementedError

    def __getstate__(self):
        return {
            "name": self.name,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "params": self.params,
        }

    def __repr__(self):
        return "%s(name='%s', needs=%s, provides=%s)" % (
            self.__class__.__name__,
            self.name,
            self.inputs,
            self.outputs,
        )

from jigls.jeditor.utils import UniqueIdentifier
from typing import Dict, List, Optional
from uuid import UUID


class JAbstractBase:
    def __init__(self, name: str, uid: Optional[str] = None) -> None:
        self._name: str = name
        self._uid: str = UniqueIdentifier() if uid is None else uid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid: str) -> None:
        self._uid = uid

    def __repr__(self) -> str:
        return "name:%s uid:%s" % (self._name, self._uid)


class JAbstractOperation(object):
    def __init__(
        self,
        name: str = str(),
        inputs: List[str] = list(),
        outputs: List[str] = list(),
        params: Dict = {},
    ):

        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.params = params

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

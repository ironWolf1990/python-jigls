from jigls.jcore.abstract import JAbstractOperation
from typing import Any, Callable, Dict, Iterable, List, Optional, Union
import operator

from .data import OptionalArg


class JOperation(JAbstractOperation):
    def __init__(
        self,
        name: str,
        inputs: List[str],
        outputs: List[str],
        params: Dict = {},
        fn: Callable = None,
    ):
        super().__init__(name=name, inputs=inputs, outputs=outputs, params=params)
        self.fn: Optional[Callable] = fn

    def Compute(self, named_inputs, outputs=None):

        inputs = [
            named_inputs[d] for d in self.inputs if not isinstance(d, OptionalArg)
        ]

        optionals = {
            n: named_inputs[n]
            for n in self.inputs
            if isinstance(n, OptionalArg) and n in named_inputs
        }

        kwargs = {k: v for d in (self.params, optionals) for k, v in d.items()}

        result = self.fn(*inputs, **kwargs)  # type:ignore

        if len(self.outputs) == 1:
            result = [result]

        result = zip(self.outputs, result)

        if outputs:
            outputs = set(outputs)
            result = filter(lambda x: x[0] in outputs, result)

        return dict(result)

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

    def __getstate__(self):
        return super().__getstate__().update({"fn": self.fn})

    def __repr__(self):
        func_name = self.fn and getattr(self.fn, "__name__", None)
        return u"%s(name='%s', needs=%s, provides=%s, fn=%s)" % (
            self.__class__.__name__,
            self.name,
            self.inputs,
            self.outputs,
            func_name,
        )

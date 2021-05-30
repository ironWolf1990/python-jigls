from os import name
from typing import List, Dict, Optional
from pydantic import BaseModel, create_model, ValidationError, validator
from uuid import UUID
from pprint import pprint

from pydantic import BaseModel as PydanticBaseModel
from pydantic.types import UUID4


class JBaseModel(PydanticBaseModel):
    __slots__ = "__weakref__"


class JSocketModel(JBaseModel):
    name: str
    uid: UUID4
    nodId: UUID4
    index: int
    type: int
    multiConnection: bool


class JNodeModel(JBaseModel):
    name: str
    uid: UUID4
    socketList: List[JSocketModel]


class JGrNodeModel(JBaseModel):
    node: JNodeModel
    posX: float
    posY: float


class JEdgeModel(JBaseModel):
    uid: UUID4
    startSocket: UUID4
    destnSocket: UUID4


class JModel(BaseModel):
    nodes: List[Optional[JNodeModel]]
    edges: List[Optional[JEdgeModel]]


"""
def TestPydantic():
    nodes = [
        {
            "nodeId": "abd6fc3f882544f5b75661c92fccbd0d",
            "posX": 531.724609375,
            "posY": -975.3916015624995,
            "socketCount": 2,
            "socketInfo": {
                "0": {
                    "socketId": "79977735631c42728339fbc31f911c67",
                    "socketType": 1,
                    "multiConnection": True,
                },
                "1": {
                    "socketId": "681f60634c63490ca583cbc0b2fc773b",
                    "socketType": 2,
                    "multiConnection": False,
                },
            },
        },
    ]
    edges = [
        {
            "edgeId": "1613b0fe65ed40f29c83aef487e33c13",
            "sourceSocketId": "2ee3e89af6f6448eab004e8d5ec3b633",
            "destinationSocketId": "79977735631c42728339fbc31f911c67",
        },
    ]

    o = JModel(nodes=nodes, edges=edges)
    print(o.json(indent=2))
    pprint(o, indent=2)


TestPydantic()
"""

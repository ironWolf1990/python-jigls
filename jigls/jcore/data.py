from typing import Dict


class Data(object):
    def __init__(self, value=None, flag=True):
        self.value = value
        self.enable = flag

    def GetData(self):
        return self.value

    def SetData(self, data):
        self.value = data

    def __repr__(self):
        output = "None" if not self.enable else self.value
        return u"%s(value='%s', enable=%s)" % (
            self.__class__.__name__,
            output,
            self.enable,
        )


class OptionalArg(str):
    def __repr__(self):
        return 'OptionalArg("%s")' % self


class ParamArgs(str):
    def __repr__(self):
        return 'ParamArgs("%s")' % self


class DataPlaceholderNode(str):
    def __repr__(self):
        return 'DataPlaceholderNode("%s")' % self


class DeleteInstruction(str):
    def __repr__(self):
        return 'DeleteInstruction("%s")' % self

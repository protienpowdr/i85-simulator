from collections.abc import Callable
from typing import Any
from enum import Enum, auto

class AppWidgetType(Enum):
    SourceEditor = auto()
    ToolBar = auto()

class AppFunction(Enum):
    RequestFileOpen = auto()

class AppWidgetResolver:
    __slots__ = 'registry'
    def __init__(self):
        self.registry : dict[AppWidgetType,Callable[...,Any]] = {}

    def add_entry(self,key,value):
        self.registry.update({key:value})

    def get_entry(self,key):
        return self.registry.get(key)



class AppFunctionResolver:
    __slots__ = 'registry'
    def __init__(self):
        self.registry : dict[AppFunction,Callable[...,Any]] = {}

    def add_entry(self,key,value):
        self.registry.update({key:value})

    def get_entry(self,key):
        return self.registry.get(key)

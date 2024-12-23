"""Represents a client session"""

from __future__ import annotations

from collections.abc import Generator
from importlib import import_module
from pathlib import Path
from types import ModuleType

from .component import Component
from .reference import Reference

ROUTES_FOLDER = Path().absolute().joinpath("routes")


def routes() -> Generator[ModuleType]:
    """Finds, imports and returns the modules in the routes folder"""
    for route_path in ROUTES_FOLDER.glob("*.py"):
        yield import_module(str(route_path))


def get_component(route) -> Component:
    return None or next(
        component
        for component in reversed(route.__dict__.values())
        # using `reversed` because components are typically closer to the bottom of the file
        if isinstance(component, Component)
    )


class Application:
    """Represents a client session"""

    references: dict[str, Reference] = {}

    def __init__(self) -> None:
        self._routes: set[ModuleType] = set()
        self._modules: set[ModuleType] = set()
        self._components: set[Component] = set()
        self.references: set[Reference] = set()

    def build(self) -> str | None:
        """Builds the application for production"""
        for route in routes():
            self._routes.add(route)

            for var in route.__dict__.values():
                if isinstance(var, ModuleType):
                    self._modules.add(var)

                if isinstance(var, Component):
                    self._components.add(var)

        imported_modules = self._modules - self._routes
        # TODO: Figure out how to build the CST tree for output

        """
        TODO: In this order
        Add imports to build_code
        Add references to build_code
        Add Functions to build_code
        Add Components to build_code
        """

import ast
import os
import sys
import importlib
import pkgutil

from model import Dependency


class ImportsParser:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def parse(self) -> list[Dependency]:
        with open(self.filepath) as f:
            content = f.read()
        tree = ast.parse(content)

        dependencies = []

        for node in tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_name = alias.name
                    is_standard_library = self._is_standard_library(import_name)
                    dependencies.append(Dependency(self.filepath, import_name, is_standard_library))
            elif isinstance(node, ast.ImportFrom):
                module_path = node.module
                if module_path:
                    is_standard_library = self._is_standard_library(module_path)
                    dependencies.append(Dependency(self.filepath, module_path, is_standard_library))

        return dependencies

    def _is_standard_library(self, module_name):
        """
        Check if the given module is part of the standard library
        """
        try:
            module = importlib.import_module(module_name)
        except ImportError:
            return False

        if hasattr(module, "__file__"):
            return module.__file__.startswith(sys.prefix)
        else:
            return module.__name__ in sys.builtin_module_names

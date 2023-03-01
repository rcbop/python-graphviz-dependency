from model import Dependency


class DotGenerator:
    """ Generates graphviz dot file from source map """
    def __init__(self, source_map: dict[str, Dependency]) -> None:
        self.source_map = source_map

    def generate(self) -> None:
        print("digraph {")
        print('ranksep="3 equally";')
        print('nodesep="1 equally";')
        print('node [shape=box];')
        graph_nodes = {
            f'"{file}" -> "{dep.import_name}"'
            for file, dependencies in self.source_map.items()
            for dep in dependencies
            if dep.is_standard_library
        }
        graph_nodes = graph_nodes.union({
            f'"{file}" -> "{dep.import_name}" [color=red]'
            for file, dependencies in self.source_map.items()
            for dep in dependencies
            if not dep.is_standard_library
        })
        for node in graph_nodes:
            print(node)
        print("}")

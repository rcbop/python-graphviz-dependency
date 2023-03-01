from dataclasses import dataclass

@dataclass
class Dependency:
    file: str
    import_name: str
    is_standard_library: bool

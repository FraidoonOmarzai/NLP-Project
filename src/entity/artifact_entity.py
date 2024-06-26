from dataclasses import dataclass


@dataclass
# @dataclass decorator is used to automatically generate __init__, and other special methods based on class variables.
class DataIngestionArtifact:
    imbalanced_data_path: str
    raw_data_path: str

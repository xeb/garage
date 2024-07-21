from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Optional
import yaml

@dataclass
class Query:
    description: Optional[str] = None
    location_address: Optional[str] = None
    place_name: Optional[str] = None
    caption: Optional[str] = None
    #people: List[str] = field(default_factory=list)
    people: List[str] = None
    transcription: Optional[str] = None
    duration: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    exact_date: Optional[datetime] = None
    width: Optional[int] = None
    height: Optional[int] = None
    age: Optional[int] = None
    limit: int = None
    offset: int = None
    file_type: Optional[str] = None
    file_hash: Optional[str] = None
    num_faces: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def to_yaml(self) -> str:
        def datetime_representer(dumper, data):
            return dumper.represent_scalar('!datetime', data.isoformat())

        yaml.add_representer(datetime, datetime_representer)

        # Create a dictionary of non-null values
        non_null_dict = {k: v for k, v in asdict(self).items() if v is not None}

        return yaml.safe_dump(non_null_dict, default_flow_style=False)

    @classmethod
    def from_yaml(cls, yaml_str: str) -> 'Query':
        def datetime_constructor(loader, node):
            value = loader.construct_scalar(node)
            return datetime.fromisoformat(value)

        yaml.add_constructor('!datetime', datetime_constructor)
        data = yaml.safe_load(yaml_str)
        return cls(**data)

    def __str__(self) -> str:
        return f"Query:\n{self.to_yaml()}"

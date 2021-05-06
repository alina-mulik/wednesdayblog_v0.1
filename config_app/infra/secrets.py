import json
from typing import NamedTuple, Dict, Any


class Secrets(NamedTuple):
    data: Dict[str, str]

    @staticmethod
    def from_json(json_data: Dict[str, Any]) -> 'Secrets':
        assert isinstance(json_data, dict)

        for k, v in json_data.items():
            assert isinstance(k, str) and len(k)
            assert isinstance(v, str)
            assert k.upper() == k, f'"{k}" given'

        return Secrets(data=json_data)

    @staticmethod
    def from_file(file_path: str) -> 'Secrets':
        with open(file_path, 'r') as f:
            return Secrets.from_json(json.load(f))

    def ensure_secret(self, name: str) -> str:
        assert isinstance(name, str) and len(name)
        assert name.upper() == name, f'"{name}" given'
        assert name in self.data, f'"{name}" not in [{list(self.data.keys())}]'
        return self.data[name]

    def optional_secret(self, name: str) -> str:
        assert isinstance(name, str) and len(name)
        assert name.upper() == name, f'"{name}" given'
        return self.data.get(name, '')
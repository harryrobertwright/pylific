from dataclasses import dataclass

from src.models.study import Study
from src.types import JSON


@dataclass
class Parser:
    data: JSON

    def parse(self) -> Study:
        return Study(**self.data)

""" """

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CurrencyListDTO:
    name: Optional[str] = field(default=None)
    symbol: Optional[str] = field(default=None)

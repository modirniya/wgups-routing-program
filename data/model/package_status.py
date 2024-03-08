from dataclasses import dataclass, field
from typing import Optional

from util.strings import *


@dataclass
class PackageStatus:
    event: str
    package_id: int
    time: Optional[str] = field(default="00:00")
    truck_id: Optional[str] = field(default=None)

    def __str__(self):
        if self.event == TAG_DELIVERED:
            return f"{GREEN}#{self.package_id:<8}{TAG_DELIVERED} at {self.time} by truck #{self.truck_id}{RESET}"
        elif self.event == TAG_EN_ROUTE:
            return f"{YELLOW}#{self.package_id:<8}{TAG_EN_ROUTE} left the hub at {self.time} by truck #{self.truck_id}{RESET}"
        return f"{RED}#{self.package_id :<8}{self.event}{RESET}"

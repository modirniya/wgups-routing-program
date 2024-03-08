from dataclasses import dataclass, field
from typing import Optional

from data.model.package_status import PackageStatus


@dataclass
class Package:
    package_id: int
    address_id: int
    delivery_deadline: str
    weight: int
    notes: Optional[str] = field(default=None)
    delivery_status: Optional[list] = field(default=None)

    def __repr__(self):
        str_status = ""
        for i, status in enumerate(self.delivery_status):
            str_status += f"\n\t\t\t{i+1}- {str(status)}"
        return f"""
    Package ID: {self.package_id}
    Delivery deadline: {self.delivery_deadline}
    Weight:     {self.weight}
    Notes:      {self.notes}
    Status:     {str_status}"""
        pass

    def update_status(self, status: PackageStatus):
        if not self.delivery_status:
            self.delivery_status = list()
        self.delivery_status.append(status)

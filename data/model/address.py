from dataclasses import dataclass


@dataclass
class Address:
    address_id: int
    name: str
    street: str
    city: str
    state: str
    zip_code: str

    def __repr__(self):
        return \
    f"""
    Recipient Name: {self.name}
    Recipient Address : {self.street}
                         {self.city} {self.state} {self.zip_code}"""

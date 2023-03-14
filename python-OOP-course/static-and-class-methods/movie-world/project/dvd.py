from calendar import month_name


class DVD:
    def __init__(
        self,
        name: str,
        dvd_id: int,
        creation_year: int,
        creation_month: str,
        age_restriction: int,
    ):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        _, month, year = date.split(".")
        month = month_name[int(month)]
        year = int(year)

        return cls(name, dvd_id, year, month, age_restriction)

    def __repr__(self) -> str:
        return (
            f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
            f"has age restriction {self.age_restriction}. "
            f"Status: {'rented' if self.is_rented else 'not rented'}"
        )

class Hospital:

    def __init__(self, tuple: tuple) -> None:
        # hospital_id
        # hospital_name
        # bed_count
        self.hospital_id = tuple[0]
        self.hospital_name = tuple[1]
        self.bed_count = tuple[2]

    def __str__(self) -> str:
        return f"""Numero de Hospital {self.hospital_id}
        Nombre de hospital {self.hospital_name}
        Numero de camas {self.bed_count}"""
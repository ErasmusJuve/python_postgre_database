class Doctor():
        
    def __init__(self, tuple:tuple) -> None:
        # doctor_id
        # doctor_name
        # hospital_id
        # joining_date
        # speciality
        # salary
        # experience
        self.doctor_id = tuple[0]
        self.doctor_name = tuple[1]
        self.hospital_id = tuple[2]
        self.joining_date = tuple[3]
        self.speciality = tuple[4]
        self.salary = tuple[5]
        self.experience = tuple[6]
        
    def __str__(self) -> str:
        return f'''Numero del doctor {str(self.doctor_id)} 
        Nombre de doctor {self.doctor_name} 
        Numero del hospital al que pertenece {str(self.hospital_id)} 
        Fecha que se unio al equipo {self.joining_date} 
        Especialidad {self.speciality} 
        Salario {str(self.salary)} 
        Experiencia {str(self.experience)}'''

   
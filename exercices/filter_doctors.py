

import conection as con


def filter_doctor_by_salary_and_specialty(specialty: str, salary: float):

    try:
        conection = con.get_connection()
        cursor = conection.cursor()
        query = """SELECT * FROM doctores WHERE speciality = %s and salary > %s;"""
        cursor.execute(query, (specialty, salary,))
        records = cursor.fetchall()

        for row in records:
            print("Numero del doctor ", row[0])
            print("Nombre de doctor ", row[1])
            print("Numero del hospital al que pertenece ", row[2])
            print("Fecha que se unio al equipo ", row[3])
            print("Especialidad ", row[4])
            print("Salario ", row[5])
            print("Experiencia ", row[6])
            print('-----')

    except Exception as e:
        raise e

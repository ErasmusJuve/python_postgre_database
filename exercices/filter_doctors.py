

import conection as con


def filter_doctor_by_salary_and_specialty(specialty: str, salary: float):
    """Regresa la lista de doctores con la especialdiad de y un slario mayor a 30000

    Args:
        specialty (str): Nombre de la especialidad por la cual se filtrara
        salary (float): Salario minimo por el cual se filtrara

    Raises:
        e: En caso de existir un error mostrara el traceback
    """    

    try:
        connection = con.get_connection()
        cursor = connection.cursor()
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

        # Cerramos la conexion 
        con.close_connection(connection)
    except Exception as e:
        raise e

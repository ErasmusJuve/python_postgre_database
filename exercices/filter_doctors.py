import conection as con
from POJO.Doctor import Doctor


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
            print(Doctor(row))
            print('-----')

        # Cerramos la conexion 
        con.close_connection(connection)
    except Exception as e:
        raise e

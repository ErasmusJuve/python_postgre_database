import conection as con


def get_hospital_detail(hospital_id: int):
    """Retorna el detalle del hospital, segun el id que reciba

    Args:
        hospital_id (int): Id del hospital del cual se mostrara su informacion

    Raises:
        e: En caso de existir un error mostrara el traceback
    """
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        select_query = """SELECT * FROM hospitales WHERE hospital_id = %s"""
        cursor.execute(select_query, (hospital_id,))
        records = cursor.fetchall()
        print(f'------Detalle del hospital numero {hospital_id}------')

        for row in records:
            print("Numero de hospital ", row[0])
            print("Nombre de hospital ", row[1])
            print("Numero de camas ", row[2])

    except Exception as e:
        raise e


def get_doctor_detail(doctor_id: int):
    """Retorna el detalle del doctor, segun el id recibido

    Args:
        doctor_id (int): Id del doctor del cual se mostrara su informacion

    Raises:
        e: En caso de existir un error mostrara el traceback
    """
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        select_query = """SELECT * FROM doctores WHERE doctor_id = %s"""
        cursor.execute(select_query, (doctor_id,))
        records = cursor.fetchall()
        print(f'------Detalle del doctor numero {doctor_id}------')

        for row in records:
            # doctor_id, doctor_name, hospital_id, joining_date, speciality, salary, experience
            print("Numero del doctor ", row[0])
            print("Nombre de doctor ", row[1])
            print("Numero del hospital al que pertenece ", row[2])
            print("Fecha que se unio al equipo ", row[3])
            print("Especialidad ", row[4])
            print("Salario ", row[5])
            print("Experiencia ", row[6])

        # Cerramos la conexion 
        con.close_connection(connection)
    except Exception as e:
        raise e

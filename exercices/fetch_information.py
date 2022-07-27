import connection as con
from POJO.Doctor import Doctor
from POJO.Hospital import Hospital

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
            print(Hospital(row))

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
            docto = Doctor(row)
            print(docto)

        # Cerramos la conexion 
        con.close_connection(connection)
    except Exception as e:
        raise e

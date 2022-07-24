import conection as con
from POJO.Doctor import Doctor


def get_doctors_by_hospital(hospital_id: int):
    """Retorna los doctores que pertenezcan al hospital indicado con el hospital_id

    Args:
        hospital_id (int): Id del hospital por el cual se realizara el filtro

    Raises:
        e: En caso de existir un error mostrara el traceback
    """    
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        query = """SELECT * FROM doctores WHERE hospital_id =%s"""
        cursor.execute(query, (hospital_id,))
        records = cursor.fetchall()

        for row in records:
            print(Doctor(row))
            print('------')
        # Cerramos la conexion 
        con.close_connection(connection)
    except Exception as e:
        raise e

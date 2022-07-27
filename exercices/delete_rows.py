import connection as con

def delete_doctor(id : int):
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        query = """DELETE FROM doctores WHERE doctor_id=%s;"""
        cursor.execute(query, (id,))
        connection.commit()
        con.close_connection(connection)
    except Exception as e:
        raise e
    else:
        print(f"Doctor numero {id} eliminado correctamente")

def delete_hospital(id : int):
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        query = """DELETE FROM hospitales WHERE hospital_id=%s;"""
        cursor.execute(query, (id,))
        connection.commit()
        con.close_connection(connection)
    except Exception as e:
        raise e
    else:
        print(f"Hospital numero {id} eliminado correctamente")
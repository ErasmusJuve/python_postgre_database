import connection as con


def insert_doctor(data: tuple):
    """Inserta un nuevo doctor segun los datos recibidos en la tuple data

    Args:
        data (tuple): Datos del doctor

    Raises:
        e: En caso de existir un error mostrara el traceback
    """
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO doctores VALUES (%s,%s,%s,%s,%s,%s,%s);"""
        cursor.execute(query, data,)
        connection.commit()
        # Cerramos la conexion
        con.close_connection(connection)
    except Exception as e:
        raise e
    else:
        print(f"Doctor {data[1]} registrado correctamente")


def insert_hospital(data: tuple):
    """Inserta un nuevo hospital segun los datos en la tupla data

    Args:
        data (tuple): Datos del hospital a registrar

    Raises:
        e: En caso de existir un error mostrara el traceback
    """
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO hospitales VALUES (%s, %s, %s);"
        cursor.execute(query, data)
        connection.commit()
        con.close_connection(connection)
    except Exception as e:
        raise e
    else:
        print(f'Hospital {data[1]} registrado correctamente')

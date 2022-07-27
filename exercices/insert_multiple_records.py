import connection as con


def insert_many_doctors(all_data: list):
    """Inserta varios registros de tipo doctor, segun los datos recibidos en la lista de tuplas

    Args:
        data (list): Lista de tuplas con los datos de los doctores

    Raises:
        e: En caso de existir un error mostrara el traceback
    """
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO doctores VALUES (%s,%s,%s,%s,%s,%s,%s);"""
        cursor.executemany(query, all_data)
        connection.commit()
        con.close_connection(connection)
    except Exception as e:
        raise e
    else:
        print(f"Doctores registrados correctamente")


def insert_many_hospitals(hospitals_data: list):
    """Inserta varios registros de tipo hospital segun los datos en la lista de tuplas recibida

    Args:
        data (list): Lista de tuplas con los datos de los hospitales a registrar

    Raises:
        e: En caso de existir un error mostrara el traceback
    """
    try:
        connection = con.get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO hospitales VALUES (%s, %s, %s);"
        cursor.executemany(query, hospitals_data)
        connection.commit()
        con.close_connection(connection)
    except Exception as e:
        raise e
    else:
        print(f'Hospitales registrados correctamente')

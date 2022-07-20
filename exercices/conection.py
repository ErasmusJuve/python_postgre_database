import psycopg2


def get_connection():
    """Retorna una conexion a la base de datos

    Returns:
        connection: E sla coneccion a la base de datos
    """
    connection = psycopg2.connect(
        user="usuario_dev",
        password='userdev12345',
        host='127.0.0.1',
        port="5432",
        database='hospital_db')
    return connection


def close_connection(connection):
    """Cierra la conexion activa que le pasamos como parametro

    Args:
        connection (connection): Conexion a cerrar
    """
    if connection:
        connection.close()


def read_database_version():
    """Retorna la version de la base de datos

    Raises:
        e: En caso de existir un error mostrara el traceback
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f'La version de la base de datos es {db_version}')
        close_connection(connection)
    except (Exception, psycopg2.Error) as e:
        raise e


def main():
    read_database_version()


if __name__ == "__main__":
    main()

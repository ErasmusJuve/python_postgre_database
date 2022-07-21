import datetime
import conection as con
from dateutil.relativedelta import relativedelta


def update_doctor_experience(doctor_id: int):
    """Actualiza la experiencia del doctor en años cumplidos

    Args:
        doctor_id (int): Id del doctor que se actualizara la experiencia

    Raises:
        e: En caso de existir un error mostrara el traceback
    """    
    try:
        # Get joining date
        connection = con.get_connection()
        cursor = connection.cursor()
        select_query = """SELECT joining_date FROM Doctores WHERE doctor_id = %s"""
        cursor.execute(select_query, (doctor_id,))
        joining_date = cursor.fetchone()

        # Parsear la fecha de la base de datos auna fecha con formato YYYY-MM-DD HH:MM:SS
        joining_date_parsed = datetime.datetime.strptime(
            ''.join(map(str, joining_date)), '%Y-%m-%d')
        # Obtenemos la fecha actual
        today_date = datetime.datetime.now()
        # obtenemos la diferencia entre las fechas, con anios cumplidos
        experience = relativedelta(today_date, joining_date_parsed).years

        # Actualizamos la experiencia del doctor
        connection = con.get_connection()
        cursor = connection.cursor()
        sql_select_query = """UPDATE Doctores set experience = %s WHERE doctor_id =%s"""
        cursor.execute(sql_select_query, (experience, doctor_id))
        # Hacemos commit de los cambios
        connection.commit()

        # Mostramos un msj de confirmacion del cambio
        print("Doctor Id:", doctor_id,
              " Experiencia actualizada a ", experience, "años")

        # Cerramos la conexion 
        con.close_connection(connection)

    except (Exception,) as e:
        raise e

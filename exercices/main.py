import conection
import fetch_information


def main():

    # Solucion del ejercicio 1
    conection.read_database_version()

    # solucion del ejercicio 2
    fetch_information.get_hospital_detail(2)
    fetch_information.get_doctor_detail(105)


if __name__ == "__main__":
    main()

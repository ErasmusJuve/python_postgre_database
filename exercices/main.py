import conection
import fetch_information
import filter_doctors
import filter_doctors_by_hospital


def main():

    # Solucion del ejercicio 1
    print("Ejercicio 1: Conectarse a la base de datos e imprimir la version")
    conection.read_database_version()
    print('-'*50)

    # solucion del ejercicio 2
    print('Ejercicio 2: Obtener la informacion del hospital y doctor por numero de id')
    fetch_information.get_hospital_detail(2)
    fetch_information.get_doctor_detail(105)
    print('-'*50)

    # Solucion del ejercicio 3
    print('Ejercicio 3: Obtener la info de doctores donde el salario sea mayor a $30000 y especialidad sea Garnacologist')
    filter_doctors.filter_doctor_by_salary_and_specialty('Garnacologist', 30000)
    print('-'*50)

    # Solucion del ejercicio 4
    print("Ejercicio 4: Obtener la lista de doctores que pertenezcan a un hospital")
    filter_doctors_by_hospital.get_doctors_by_hospital(2)
    print('-'*50)

if __name__ == "__main__":
    main()

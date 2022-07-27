import connection

import fetch_information
import filter_doctors
import filter_doctors_by_hospital
import update_doctor_experience
import insert_records
import insert_multiple_records
import delete_rows

MENU = '''
1: Conectarse a la base de datos e imprimir la version
2: Obtener la informacion del hospital y doctor por numero de id
3: Obtener la info de doctores donde el salario sea mayor a $30000 y la especialidad sea Garnacologist
4: Obtener la lista de doctores que pertenezcan a un hospital
5: Actualizar la experiencia del doctor
7: insertar registros
8: Insertar multiples registros a la vez
9: Eliminar registros

0: Salir del sistema
 '''


def main():

    flag = True
    while flag:
        option = int(input(MENU))

        if option == 1:
            # Solucion del ejercicio 1
            print("Ejercicio 1: Conectarse a la base de datos e imprimir la version")
            conection.read_database_version()
        elif option == 2:
            # solucion del ejercicio 2
            print(
                'Ejercicio 2: Obtener la informacion del hospital y doctor por numero de id')
            fetch_information.get_hospital_detail(2)
            fetch_information.get_doctor_detail(105)
        elif option == 3:
            # Solucion del ejercicio 3
            print('Ejercicio 3: Obtener la info de doctores donde el salario sea mayor a $30000 y la especialidad sea Garnacologist')
            filter_doctors.filter_doctor_by_salary_and_specialty(
                'Garnacologist', 30000)
        elif option == 4:
            # Solucion del ejercicio 4
            print(
                "Ejercicio 4: Obtener la lista de doctores que pertenezcan a un hospital")
            filter_doctors_by_hospital.get_doctors_by_hospital(2)
        elif option == 5:
            # solucion del ejercicio 5
            print('Ejercicio 5: Actualizar la experiencia del doctor')
            update_doctor_experience.update_doctor_experience(101)
        elif option == 6:
            pass
            ##
        elif option == 7:
            # Solucion ejercicio 7
            print("Ejercicio 7: insertar registros")
            doctor_data = (109, "Fernando", 3, "2010-07-12",
                           "Oncologist", 25000, 0)
            insert_records.insert_doctor(doctor_data)
            hospital_data = ('5', 'Angeles', 500)
            insert_records.insert_hospital(hospital_data)
        elif option == 8:
            # Solucion ejercicio 8
            print('Ejercicio 8: Insertar multiples registros a la vez')
            doctors_data = [(110, "Martin", 5, "2012-05-23", "Dentist", 30000, 0),
                            (111, "Eduardo", 5, "2017-03-05", "Dermatologist", 20000, 0)]
            insert_multiple_records.insert_many_doctors(doctors_data)

            hospitals_data = [(6, "ABC", 100), (7, "DALINDE", 210)]
            insert_multiple_records.insert_many_hospitals(hospitals_data)

        elif option == 9:
            # Solucion ejercicio 9
            print('Ejercicio 9: Eliminar registros')
            delete_rows.delete_doctor(109)
            delete_rows.delete_hospital(6)

        elif option == 0:
            flag = False
            print("Hasta pronto!!")


if __name__ == "__main__":
    main()

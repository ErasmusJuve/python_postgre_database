## Python Database Programming Exercise

Este ejercico tiene la finalidad de ayudarme a mejorar mis habilidades de programcion en python y unirlas con mis habilidades de base de datos  

Con este ejercicio se realizaran operaciones CRUD

Requisitos:
1. Python 3.10.2 (Minimo)
2. Base de datos postgres version 14.4 (Minimo)
3. Libreria **psycopg2**
4. Libreria **python-dateutil**


## Creacion del contenedor de la base dedatos

```docker
docker run -p 5432:5432 --name bd_hospital -v `pwd`\bd_hospital:/var/lib/postgresql/data -e POSTGRES_PASSWORD=admin12345 -d postgres:14.4-alpine
```

## Queries para crear la base de datos y tablas

### Crear base de datos
```sql
    CREATE database hospital_db;
```

### Crear usuario dev
CREATE ROLE usuario_dev WITH
	LOGIN
	NOSUPERUSER
	CREATEDB
	NOCREATEROLE
	INHERIT
    
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'userdev12345';

### Crear tabla hospital
```SQL
    CREATE TABLE public.hospitales(
        hospital_id serial NOT NULL,
        hospital_name character varying(100) NOT NULL,
        bed_count integer NOT NULL,
        PRIMARY KEY (hospital_id)
    );

    ALTER TABLE IF EXISTS public.hospitales
        OWNER to usuario_dev;

    INSERT INTO hospitales (hospital_id, hospital_name, bed_count) 
    VALUES 
    ('1', 'Mayo Clinic', 200), 
    ('2', 'Cleveland Clinic', 400), 
    ('3', 'Johns Hopkins', 1000), 
    ('4', 'UCLA Medical Center', 1500);
```

### Crear tabla doctor
```sql
CREATE TABLE public.doctores (
    doctor_id serial NOT NULL,
    doctor_name character varying(100) NOT NULL,
    hospital_id serial NOT NULL,
    joining_date date NOT NULL,
    speciality character varying(100) NOT NULL,
    salary double precision NOT NULL,
    experience smallint,
    PRIMARY KEY (doctor_id),
    CONSTRAINT hospital_doctor FOREIGN KEY (hospital_id)
        REFERENCES public.hospitales (hospital_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT
        NOT VALID
);

ALTER TABLE IF EXISTS public.doctores
    OWNER to usuario_dev;

INSERT INTO doctores (doctor_id, doctor_name, hospital_id, joining_date, speciality, salary, experience) 
    VALUES 
    ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
    ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
    ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
    ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
    ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
    ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
    ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
    ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);

```

### Resultado de los selects a cada tabla

```sql
SELECT * FROM Hospitales
```

![](https://i.imgur.com/wlN04gp.png)


```sql
SELECT * FROM Doctores
```

![](https://i.imgur.com/UzecmLD.png)


Data model de la base de datos 

![](https://i.imgur.com/G7dsnUE.png)

## Ejercicio 1: Conectarse a la base de datos e imprimir la version

Instalamos la libreria psycopg2  
```bash
pip install psycopg2
```

Resultado esperado
```
('PostgreSQL 14.4 on x86_64-pc-linux-musl, compiled by gcc (Alpine 11.2.1_git20220219) 11.2.1 20220219, 64-bit',)
```

## Ejercicio 2: Obtener la informacion del hospital y doctor por numero de id

Resultado esperado:  

```
Printing Hospital record
Hospital Id: 2
Hospital Name: Cleveland Clinic
Bed Count: 400

Printing Doctor record
Doctor Id: 105
Doctor Name: Linda
Hospital Id: 3
Joining Date: 2004-06-04
Specialty: Garnacologist
Salary: 42000
Experience: None
```


## Ejercicio 3: Obtener la info de los doctores donde el salario sea mayor a $30000 y especialidad sea Garnacologist

Resultado esperado 
```
Doctor Id:  105
Doctor Name: Linda
Hospital Id: 3
Joining Date: 2004-06-04
Specialty: Garnacologist
Salary: 42000
Experience: None 
 
Doctor Id:  107
Doctor Name: Richard
Hospital Id: 4
Joining Date: 2014-08-21
Specialty: Garnacologist
Salary: 32000
Experience: None 
```

## Ejercicio 4: Obtener la lista de doctores que pertenezcan a un hospital

Resultado esperado
```
Numero del doctor  103
Nombre de doctor  Susan
Numero del hospital al que pertenece  2
Fecha que se unio al equipo  2016-05-19
Especialidad  Garnacologist
Salario  25000.0
Experiencia  None

Numero del doctor  104
Nombre de doctor  Robert
Numero del hospital al que pertenece  2
Fecha que se unio al equipo  2017-12-28
Especialidad  Pediatric
Salario  28000.0
Experiencia  None
```

## Ejercicio 5 Actualizar la experiencia del doctor

Resultado esperado 
```
Doctor Id: 101  Experiencia actualizada a  17 años
```

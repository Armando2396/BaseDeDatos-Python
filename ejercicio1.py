#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que 
# también será de tipo texto.
#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

conn = sqlite3.connect('basedeDatosAlumno.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS Alumnos(
    id INTEGER, nombre TEXT, apellido TEXT
) """)

c.execute("INSERT INTO Alumnos VALUES (1, 'armando', 'martinez')")
c.execute("INSERT INTO Alumnos VALUES (2, 'pepe', 'jimenez')")
c.execute("INSERT INTO Alumnos VALUES (3, 'ana', 'arauz')")
c.execute("INSERT INTO Alumnos VALUES (4, 'gaby', 'navarro')")
c.execute("INSERT INTO Alumnos VALUES (5, 'alex', 'martinez')")
c.execute("INSERT INTO Alumnos VALUES (6, 'arian', 'martinez')")
c.execute("INSERT INTO Alumnos VALUES (7, 'adelain', 'elizondro')")
c.execute("INSERT INTO Alumnos VALUES (8, 'ashely', 'taylor')")
conn.commit()

c.execute("SELECT * FROM Alumnos WHERE nombre='armando'")
estudiantes = c.fetchone()
print(estudiantes)

c.close()
conn.close()
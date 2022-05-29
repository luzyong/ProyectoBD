import mysql.connector as con
from mysql.connector import Error


class Conexion:
    connection = ''
    cur = ''


    def __init__(self):
        self.connection = con.connect( host='localhost', user= 'USER', password='PASSWORD', database='DATABASE' )
        self.cur = self.connection.cursor()


    def Select(self, campo='*', tabla=''):
        try:
            self.cur.execute( f"SELECT {campo} FROM {tabla}" )

        except Error as error:
            return error

        else:
            return self.cur.fetchall()
        

    def Insert(self, tabla='',campos='', valores=''):
        try:
            if campos=='':
                self.cur.execute(f"INSERT INTO {tabla} VALUES {valores}")
            else:
                self.cur.execute(f"INSERT INTO {tabla}{campos} VALUES {valores}")
            self.connection.commit()

        except Error as error:
            return error

        else:
            return 1
        


    def Update(self, tabla='', campos='', condicion=''):
        try:
            self.cur.execute(f"UPDATE {tabla} SET {campos} WHERE {condicion}")
            self.connection.commit()

        except Error as error:
            return error

        else:
            return 1
       


    def Delete(self, tabla='', condicion=''):
        try:
            self.cur.execute(f"DELETE FROM {tabla} WHERE {condicion}")
            self.connection.commit()

        except Error as error:
            return error

        else:
            return 1
        

    
'''conexion = Conexion()

result = conexion.Select(tabla='alumno')
if type(result)=='array':
    for resultado in result:
        print(resultado[1])
else:
    print(result)'''
#import the module
import mysql.connector


def listar(cur):
    #Ejecuto query SELECT  
    cur.execute("SELECT * FROM clientes")
    #Fetch all records from table
    res = cur.fetchall()
    #print
    print("------------------------------------------------------------------------")
    print("ID Nombre        Nacimiento     Direccion   Localidad   Telefono")
    print("------------------------------------------------------------------------")
          
    for x in res:
        print(str(x[0])+"  "+x[1]+"  "+x[2]+"  "+x[5]+"  "+x[3]+"  "+x[4])
    print("------------------------------------------------------------------------") 


def optiones():
    print("Ingrese 1 para imprimir 'Opcion 1'.")
    print("Ingrese 2 para imprimir 'Opcion 2'.")
    print("Ingrese 3 para imprimir 'Opcion 3'.")
    print("Ingrese 4 para imprimir 'Opcion 4'.")
    print("Ingrese 5 para Salir")

def main():

    con = mysql.connector.connect( 
        host="localhost",
        user="root",
        passwd="",
        database="practicasql1b"
        )

    #opne cursor
    cur = con.cursor()

    while True:
        optiones()
        option = int(input())
        if option == 1:
            listar(cur)
        elif option == 2:
            print("Opcion 2")
        elif option == 3:
            print("Opcion 3")
        elif option == 4:
            print("Opcion 4")
        elif option == 5:
            break

#call main
main()
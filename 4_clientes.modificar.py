#Importo el modulo que conecta con Mysql
import mysql.connector


def listar(cur):
    #Ejecuto query SELECT  
    cur.execute("SELECT * FROM clientes")
    
    #Busco todos los registros de la tabla
    resultado = cur.fetchall()
    #print
    print("------------------------------------------------------------------------")
    print("ID Nombre        Nacimiento     Direccion   Localidad   Telefono")
    print("------------------------------------------------------------------------")
          
    for x in resultado:
        print(str(x[0])+"  "+x[1]+"  "+x[2]+"  "+x[5]+"  "+x[3]+"  "+x[4])
    print("------------------------------------------------------------------------") 

def alta(con,cur):
    #Ingreso de valores para ser insertados en la BD
    #cid=input("Ingrese ID:")
    cnom=input("Ingrese Nombre:")
    cnac=input("Ingrese Nacimiento:")
    cdir=input("Ingrese Direccion:")
    cloc=input("Ingrese Localidad:")
    ctel=input("Ingrese Telefono:")
    cem=input("Ingrese Email:")
    cal=input("Ingrese Fecha Alta:")
    cgr=input("Ingrese Grupo:")
    
    #Ejecuto Query de Inserción
    sql = "INSERT INTO clientes (nombre_cliente, fecha_nacimiento, direccion, localidad, telefono, email, fecha_alta, grupo_clientes) VALUES (%s, %s,%s, %s,%s, %s, %s, %s)"    #create list of values typed from user to insert in customer table
    valores = (cnom,cnac,cdir,cloc,ctel,cem,cal,cgr)
    
    #Ejecuto query con valores ingresados
    cur.execute(sql, valores)
    
    #Confirmo los cambios en la base de datos
    con.commit()

    #display success message
    print(cur.rowcount, "Cliente ingresado.")

def baja(con,cur):
    #read the customer ID for which record to be deleted
    cid=input("Ingrese ID del cliente a borrar:")
    #Ejecuto Query de Baja
    #sql = "DELETE FROM clientes where id_cliente = '"+cid+"'"
    sql = f"DELETE FROM clientes where id_cliente = {cid}"
    
    #execute delete query
    cur.execute(sql)
    
    #Confirmo los cambios en la base de datos
    con.commit()
    
    #display success message
    print(cur.rowcount, "Registro borrado.")

def modificar(con,cur):
    #read values to be updated
    
    cid=input("Ingrese ID del cliente:")
    cnom=input("Ingrese Nombre:")
    cnac=input("Ingrese Nacimiento:")
    cdir=input("Ingrese Direccion:")
    cloc=input("Ingrese Localidad:")
    ctel=input("Ingrese Telefono:")
    cem=input("Ingrese Email:")
    cal=input("Ingrese Fecha Alta:")
    cgr=input("Ingrese Grupo:")

    #create update query
    sql = "update clientes set nombre_cliente='"+cnom+"', fecha_nacimiento='"+cnac+"',direccion='"+cdir+"', localidad='"+cloc+"', telefono='" +ctel+"' , email='" +cem+"', fecha_alta='" +cal+"' , grupo_clientes='" +cgr+"' where id_cliente="+cid
    #Execute Update query on opened cursor
    cur.execute(sql)
    #commit Changes to DB
    con.commit()
    #display success message
    print(cur.rowcount, "Record updated.")

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
            alta(con, cur)
        elif option == 3:
            baja(con, cur)
        elif option == 4:
            modificar(con, cur)
        elif option == 5:
            break

#call main
main()
from os import close
import sqlite3
from sqlite3.dbapi2 import Cursor








def abrir (NombreBD):
    conexion:sqlite3.connect(NombreBD)
    cur = conexion.cursor()
    return cur

def Registro_TablaDB1_Datos(conexion,Datos):
    TablaDB='INSERT INTO Estudiante VALUES (Id_estudiante, Nombre_est, Tipo_Documento,Nom_acudiente,Correo_acudiente); '
    Cursor = conexion.cursor()
    Cursor.execute(TablaDB, Datos)

    conexion.commit()
    conexion.close()
    

def Registro_TablaDB2_sintomas(conexion,Datos):
    TablaDB='INSERT INTO SintomasAntecedentes VALUES (Id_estudiante, sintomas, Temperatuea,Antecedentes,Contacto personasCovid, Convive_personasSalud,Convive_personasMay); '
    Cursor = conexion.cursor()
    Cursor.execute(TablaDB, Datos)
    conexion.commit()
    conexion.close()



def consulta(conexionDB,consulta):
    conexionDB.execute(consulta)
    return conexionDB


def formelista(conexion,lista):
    for registro in conexion:
        lista.append(registro)


def cerrar (conexion):
    conexion.close()


def obtenersintomas(listasintomas,sintomas,sin_Estudiante):
    c_desplazamiento = 0

    while c_desplazamiento > 11:
        sinto = sintomas &1
        if sinto == 1:
            sin_Estudiante.append(listasintomas[c_desplazamiento])
            sintomas = sintomas >> 1
            c_desplazamiento += 1

def obtenerAntecedentes(listAntecedentes,Antecendetes,Antcd_Estudiante):
    c_desplazamiento = 0

    while c_desplazamiento > 5:
        antc = Antecendetes &1
        if antc == 1:
            Antcd_Estudiante.append(listAntecedentes[c_desplazamiento])
            Antecendetes = Antecendetes >> 1
            c_desplazamiento += 1






def Numero_Checbox(l_Num):                              #FUNCION PARA TRANSFORMA LA LISTA OBTENIA DE NUMEROS, EN UN 
            Cont = 1                                    # SOLO NUMERO
            Despl =l_Num[0]
            while Cont < len(l_Num):
                  Despl = Despl << 1
                  Despl = Despl ^ l_Num [Cont]
                  Cont = Cont + 1
            return(Despl)



            



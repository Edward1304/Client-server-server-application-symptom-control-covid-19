

#PROTECTO FINAL DE ASIGNATURA   TECNICAS DE PROGAMACION 
#ESTUDIANTE: Edward Fabian Goyeneche Velandia
#DOCENTE: Luz Angela Aristizabal
#SEMESTRE:  2020-1

from Libreria_DB import Formar_lista
from sqlite3.dbapi2 import DateFromTicks, connect
import sys
from GUIcovid import *
from ConexionDBsqlite import *
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5. QtCore import pyqtSlot
from Lb_Fun_sqlite import *


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class AplicacionCOVID_19 (QtWidgets.QMainWindow):
      def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.B_Guardar.clicked.connect(self.boton_presionado)
            self.ui.B_Guardar.clicked.connect(self.insertar_Registro_DB_Tabla)           #Botones de guardado y grabado en base de Datos
            self.ui.B_Guardar.clicked.connect(self.insertar_t2)                          #y botones  de  las distintas consultas
            self.ui.Consul_1.clicked.connect(self. ConsultaN1)
            self.ui.Consul_16.clicked.connect(self. ConsultaN2)
            self.ui.Consul_17.clicked.connect(self. ConsultaN3)
            self.ui.Consul_18.clicked.connect(self. ConsultaN4)
            self.ui.Consul_19.clicked.connect(self. ConsultaN4)
            


            #tabla interfaz consulta 1

            self.ui.Tabla_consulta.setColumnWidth(0,98)
            self.ui.Tabla_consulta.setColumnWidth(1,100)
            self.ui.Tabla_consulta.setColumnWidth(2,120)
            self.ui.Tabla_consulta.setColumnWidth(3,120)
            self.ui.Tabla_consulta.setColumnWidth(4,150)
            self.ui.Tabla_consulta.setColumnWidth(5,150)


            #tabla interfaz consulta 2
            self.ui.Tabla_consulta_2.setColumnWidth(0,250)
            self.ui.Tabla_consulta_2.setColumnWidth(1,250)


            
            #tabla interfaz consulta 3 
            self.ui.Tabla_consulta_3.setColumnWidth(0,190)
            self.ui.Tabla_consulta_3.setColumnWidth(1,190)
            self.ui.Tabla_consulta_3.setColumnWidth(0,190)


            #tabla interfaz consulta 4
            self.ui.Tabla_consulta_4.setColumnWidth(0,250)
            self.ui.Tabla_consulta_4.setColumnWidth(1,250)


            #tabla interfaz consulta 5
            self.ui.Tabla_consulta_4.setColumnWidth(0,250)
            self.ui.Tabla_consulta_4.setColumnWidth(1,250)

            
           




     
#/////////////////////////////////////////////////////////////////////////////

      def insertar_Registro_DB_Tabla(self):                                #Metodo que   toma datos  ingresados  en linea de texto y combbobox
            conexion = abrir("BaseDB_covid.db")                            # y los guarda en una base de datos
            Numero_Documento = self.ui.Doc_Num.text()      
            Nombre_Estudiante = self.ui.Nom_Est.text()
            Tipo_Documento = self.ui.Tipo_Doc.currentText()
            Nombre_Acudiente = self.ui.Nom_Acu.text()
            Correo_Electronico = self.ui.Cor_Acu.text()
            
            if int(self.Temperatura.text()) > 36:
             self.Diagnostico.setText('Fiebre')
            else :
             self.Diagnostico.setText('Normal')
             

            Registro_TablaDB1_Datos(conexion, (Numero_Documento,Nombre_Estudiante ,Tipo_Documento ,Nombre_Acudiente ,  Correo_Electronico))
           





#/////////////////////////////////////////////////////////////////////////////
      def checkboxsintomas(self): 
          self.ui.checkBox.stateChange.connect(self.Seleccion_Sintomas)
          self.ui.checkBox_2.stateChange.connect(self.Seleccion_Sintomas)
          self.ui.checkBox_3.stateChange.connect(self.Seleccion_Sintomas)            #Metodo  que   toma la seleccion de los checkbox y los  direciona al
          self.ui.checkBox_4.stateChange.connect(self.Seleccion_Sintomas)           # otro metodo  los cuales los va operar
          self.ui.checkBox_5.stateChange.connect(self.Seleccion_Sintomas)
          self.ui.checkBox_6.stateChange.connect(self.Seleccion_Sintomas)
          self.ui.checkBox_7.stateChange.connect(self.Seleccion_Sintomas)
          self.ui.checkBox_8.stateChange.connect(self.Seleccion_Sintomas)
          self.ui.checkBox_9.stateChange.connect(self.Seleccion_Sintomas)
          self.ui.checkBox_10.stateChange.connect(self.Seleccion_Sintomas)
          self.ui.checkBox_11.stateChange.connect(self.Seleccion_Sintomas)
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
      
      def Seleccion_Sintomas(self):                                          #Metodo que   crea una lista en  la cual se guarda la selecion  en numero binario
            TotalSinto = []
            

            if self.ui.checkBox.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)


            if self.ui.checkBox_2.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)

            
            if self.ui.checkBox_3.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)

            
            if self.ui.checkBox_4.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)
            
            if self.ui.checkBox_5.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)
            
            if self.ui.checkBox_6.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)

            if self.ui.checkBox_7.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)
            
            if self.ui.checkBox_8.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)
            
            if self.ui.checkBox_9.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)

            if self.ui.checkBox_10.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)

            
            if self.ui.checkBox_11.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalSinto)
            else:
                  opc = 0
                  opc.append(TotalSinto)

            print(TotalSinto)
            listasintomas = ["Temperatura mayor a 37","Dolor de garganta","Malestar General",
             "Escalofrios","Dolor Muscular","Tos seca Constante","Dificultades para Respirar",
            "Secrecion Nasal","Perdida de olfato o gusto","Diarrea","Fiebre"]      

            SintomasLista= Numero_Checbox(TotalSinto)
            sintomaNUM =[]                                                                        #parte del metodo en la cual se llama las funciones que convierte 
            Numero_Sintoma = obtenersintomas(listasintomas,SintomasLista, sintomaNUM)            #la lista a un  nuemro y la funcion que convierte el binario a  numero y el numero 
                                                                                                # y se codifican los sintomas
            LS = Numero_Sintoma 
            




#/////////////////////////////////////////////////////////////////////////////
      def  checkboxantecedente(self):
            self.ui.checkBox_12.stateChange.connect(self.Seleccion_antecendentes)
            self.ui.checkBox_13.stateChange.connect(self.Seleccion_antecendentes)
            self.ui.checkBox_14.stateChange.connect(self.Seleccion_antecendentes)              #Metodo similar al anterior pero que  trabaja los antecedentes
            self.ui.checkBox_15.stateChange.connect(self.Seleccion_antecendentes)
            self.ui.checkBox_16.stateChange.connect(self.Seleccion_antecendentes)




#/////////////////////////////////////////////////////////////////////////////  
      def Seleccion_Antecedente(self):
            TotalAntec = [] 
            opc = 1

            if self.ui.checkBox12.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalAntec)
            else:
                  opc = 0
                  opc.append(TotalAntec)


            if self.ui.checkBox_13.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalAntec)
            else:
                  opc = 0
                  opc.append(TotalAntec)

            
            if self.ui.checkBox_14.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalAntec)
            else:
                  opc = 0
                  opc.append(TotalAntec)

            
            if self.ui.checkBox_15.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalAntec)
            else:
                  opc = 0
                  opc.append(TotalAntec)
            
            if self.ui.checkBox_5.stateChange.connect() == True:
                  opc= 1
                  opc.append(TotalAntec)
            else:
                  opc = 0
                  opc.append(TotalAntec)

            print(TotalAntec)



            listantedentes = ["Diabetes","Hipertencion","Enfermedad del Corazon","Enfermedad Pulmonar","Asma"]          #Funciones similares al metodo anterior pero
            Antecedentes_Lista = Numero_Checbox(TotalAntec)                                                             # conantecedentes
            ante_num = []
            Numero_Antecedente = obtenerAntecedentes(listantedentes,Antecedentes_Lista,ante_num)
            LA= Numero_Antecedente


      def vivir_abuelos (self):
            if self.radioButton.isChecked():
                  if self.radioButton_5 .isChecked() and  self.radioButton_7 .isChecked() :
                        self.label_55.setText("Vive con su abuelos y  ambos estan Vacunados")
                        lista =[1,0,1,1,1]
                  elif self.radioButton_5 .isChecked() and  self.radioButton_8 .isChecked() :
                        self.label_55.setText("Vive con su abuelos y su abuela esta vacunada y  su abuelo no esta vacunada")
                        lista =[1,0,1,0,0]
                  elif self.radioButton_6 .isChecked() and  self.radioButton_7 .isChecked() :
                        self.label_55.setText("Vive con su abuelos y su abuela  no esta vacunada y  su abuelo esta vacunada") 
                        lista =[1,0,0,1,0]
                  elif self.radioButton_6 .isChecked() and  self.radioButton_8 .isChecked() :
                        self.label_55.setText("Vive con su abuelos y  ninguno de los 2 esta vacuando")
                        lista =[1,0,0,0,0] 
                   
            elif self. radioButton.isChecked() :
                  self.label_55.setText("No vive con sus abueelos")   
                  lista =[0,1,0,0,0]
            else:
                  self.label_55.setText("No ha selecionado nada") 

            lva = lista
            Num_lva = Numero_Checbox(lva)
            print(Num_lva)


                  
            

                     
                  


                        






#/////////////////////////////////////////////////////////////////////////////    
      def insertar_t2(self):
            conexion = abrir("BaseDB_covid.db")
            Numero_Documento = self.ui.Doc_Num.text()                #Metodo para llenar la tabla de sintomas y antecedente, de la base de datos, con los datos 
            Sintomas = self.Seleccion_Sintomas()                    #obtenidos de la linea de texto de interfas y de  los metodos de sintomas y antecedente
            Temperatura_Est = self.ui.Temperatura.text()
            Antecendente_Est = self.Seleccion_Antecedente()
            Cont_Per_Cov = self.ui.Contacto_Covid.currentText()
            Convive_Salud = self.ui.Conv_salud.currentText()
            Convive_Mayores = self.ui.Conv_May.currentText()
            Diagnostico_Temp = self.ui.Diagnostico.text()
            abuelos_Vacuna = self.vivir_abuelos()



            Registro_TablaDB2_sintomas (conexion, (Numero_Documento,Sintomas ,Temperatura_Est,Antecendente_Est , Cont_Per_Cov,Convive_Salud,Convive_Mayores,Diagnostico_Temp,))



  #/////////////////////////////////////////////////////////////////////////////    
      def ConsultaN1(self):
            listasintomas = ["Temperatura mayor a 37","Dolor de garganta","Malestar General",   #Consulta   donde se  puede buscar el estudiante
             "Escalofrios","Dolor Muscular","Tos seca Constante","Dificultades para Respirar",  #  y se muestra todos sus datos  en una tabala y 
            "Secrecion Nasal","Perdida de olfato o gusto","Diarrea","Fiebre"]                   # mostrar los sintomas que posee en una lista (ventana widget)
            BaseDB= "BaseDB_covid.db"

            conectar = abrir(BaseDB)
            Nombre_Consulta= self.ui.codigoB.text()
            Nombre_Consulta= "SELECT Estudiante.Id_estudiante,Nombre_est,Tipo_documento,Nom_acudiente,Correo_acudiente   ,SintomasAntecedentes.Sintomas FROM Estudiante JOIN SintomasAntecedentes ON Estudiante.Nombre_est= Nombre_Consulta"
            datoB = self.consulta(conectar,Nombre_Consulta)
            i = len(datoB)
            self.ui.tabla_buscar.setRowCount(i)
            tablerow = 0
            for row in datoB:
                  self.ui.Tabla_consulta.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
                  self.ui.Tabla_consulta.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
                  self.ui.Tabla_consulta.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
                  self.ui.Tabla_consulta.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
                  self.ui.Tabla_consulta.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
                  self.ui.Tabla_consulta.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))

                  tablerow += 1

            Lista=[]
            
            Formar_lista(datoB,Lista)
            lista_sintomas_estudiante = []
            obtenersintomas(listasintomas,Lista[(row[1])],lista_sintomas_estudiante)

            self.ui.lisWidget.addItem(lista_sintomas_estudiante)
            





#/////////////////////////////////////////////////////////////////////////////
      def ConsultaN2(self):
            BaseDB= "BaseDB_covid.db"
            conectar = abrir(BaseDB)
            buscar = "SELECT Nombre_est, Nom_acudiente FROM  Estudiante"    #metodo de consulta 2  donde se mustra en una tabla el estudiante
            mostrar = consulta(conectar,buscar)                              # y su acudiente
            lista= []
            formelista(mostrar,lista)


            self.ui.Tabla_consulta_2.setItem(QtWidgets.QTableWidgetItem(lista[0]))
            self.ui.Tabla_consulta_2.setItem(QtWidgets.QTableWidgetItem(lista[1]))



#/////////////////////////////////////////////////////////////////////////////
      def ConsultaN3(self):
            BaseDB= "BaseDB_covid.db"          
            conectar = abrir(BaseDB)
            buscar = 'SELECT Estudiante.Nombre_est,SintomasAntecedentes.Antecedentes,Convive_personasMay  FROM  Estudiante JOIN SintomasAntecedentes ON Convive_personasMay = "si"'
            mostrar = consulta(conectar,buscar)
            lista= []                                                                     #Consulta 3 , estudiantes que conviven con personas mayores
            formelista(mostrar,lista)       
            self.ui.Tabla_consulta_3.setItem(QtWidgets.QTableWidgetItem(lista[0]))
            self.ui.Tabla_consulta_3.setItem(QtWidgets.QTableWidgetItem(lista[1]))
            self.ui.Tabla_consulta_3.setItem(QtWidgets.QTableWidgetItem(lista[2]))



#/////////////////////////////////////////////////////////////////////////////

      def ConsultaN4(self):
            BaseDB= "BaseDB_covid.db"
            conectar = abrir(BaseDB)
            buscar = "SELECT Estudiante.Nombre_est,SintomasAntecedentes.Temperatura  FROM  Estudiante JOIN SintomasAntecedentes ON Temperatura >38"
            mostrar = consulta(conectar,buscar)
            lista= []                                                                     #consulta  4 , estuddiantes q con temperatura superior
            formelista(mostrar,lista) 

            self.ui.Tabla_consulta_4.setItem(QtWidgets.QTableWidgetItem(lista[0]))
            self.ui.Tabla_consulta_4.setItem(QtWidgets.QTableWidgetItem(lista[1]))

#/////////////////////////////////////////////////////////////////////////////
      def ConsultaN5(self):
            BaseDB= "BaseDB_covid.db"
            conectar = abrir(BaseDB)
            buscar = "SELECT Estudiante.Nom_acudiente,SintomasAntecedentes.Temperatura  FROM  Estudiante JOIN SintomasAntecedentes ON Temperatura <37"
            mostrar = consulta(conectar,buscar)
            lista= []
            formelista(mostrar,lista)                                                        #consulta 5 , estudiantes con temperatira  inferior

            self.ui.Tabla_consulta_5.setItem(QtWidgets.QTableWidgetItem(lista[0]))
            self.ui.Tabla_consulta_5.setItem(QtWidgets.QTableWidgetItem(lista[1]))

            



#/////////////////////////////////////////////////////////////////////////////
      
      @pyqtSlot()
      def boton_presionado(self):
                                                          # metodo que  al momento de guardar , da el diagnostico de fiebre
       if int(self.Temperatura.text()) > 36:
        self.Diagnostico.setText('Fiebre')
       else :
            self.Diagnostico.setText('Normal')


#/////////////////////////////////////////////////////////////////////////////

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Resultado = AplicacionCOVID_19()
    Resultado.show()
    sys.exit(app.exec_())



            








            



            

            




            



          




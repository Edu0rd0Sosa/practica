import tkinter as tk
from tkinter import Label,Frame,ttk,Button,Entry,END
import mysql.connector
from tkinter import messagebox
import re
try:
  db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="escuela")
except mysql.connector.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    exit()
class proveedor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.db=db
        self.wigets()
    def actualizar_alumno(self):
        id=self.entrada_id.get()
        nombre =self.entrada_nombre.get()
        edad = self.entrada_edad.get()
        email = self.entrada_email.get()
        curp= self.entrada_curp.get()
        matricula=self.entrada_matricula.get()
        
    
        # Validar que los campos no estén vacíos
        if not id or not curp or not nombre or not edad or not email or not matricula:
            messagebox.showerror("Error al actualizar al alumno", "Por favor ingrese todos los datos del alumno")
            return 
        if id.isdigit():
            pass
        else:
            messagebox.showerror("AGREGA UN ID VALIDO","el id que agregaste no es valido  por favor agrega uno")
            return
        if self.validar_nombre(nombre)==False:
            messagebox.showerror("error el nombre es invalido","ingrese solo letras             ")
            return
        if self.validar_edad(edad)==False:
            messagebox.showerror("La edad es invalida","has agregado una dato que es invalido \n solo agrega una edad de menor a 99 años")
            return
        if self.validar_email(email)==False:
            messagebox.showerror("tienes el gmail mal escrito","agrega el gmail correcto      ")
            return
        if self.validar_curp(curp)==False:
            messagebox.showerror("tienes el CURP mal escrito","DEBES DE POBNER BIEN LA CURP         \nojo las curps deben tener 18 caracteres\n(letras MAYUSCULAS Y de 4 a 9 numeros)")
            return
        if self.validar_matricula(matricula)==False:
            messagebox.showerror("Error al agregar la matricula","agrega solo numeros para la matricula \nson 10 digitos en la matricuula")
            return
       
        # Agregar el nuevo alumno
        self.actualiza(id,nombre,edad, email,curp,matricula)
    
        # Limpiar los campos de entrada
        self.entrada_id.delete(0, END)
        self.entrada_nombre.delete(0, END)
        self.entrada_edad.delete(0, END)
        self.entrada_email.delete(0, END)
        self.entrada_curp.delete(0, END)
        self.entrada_matricula.delete(0, END) 
    
    def actualiza(self,id,nombre, edad, email,curp,matricula):
        try:
            iid =int(id)
            cursor = self.db.cursor()
            sentencia = "UPDATE alumnos SET id=%s, nombre=%s, edad=%s, email=%s, curp=%s, matricula=%s WHERE id=%s"
            datos = (iid, nombre, edad, email, curp, matricula, iid)
            cursor.execute(sentencia,datos)
            self.db.commit()
            cursor.close()
        except ValueError:
            messagebox.showerror("Llena correctamente","Los datos que pusiste estan mal escritos o no cumplen los criterios")
            return
    def eliminar_alumno(self):
        try:
           id=int(self.entrada_id.get()) 
           self.elimina(id)
           self.entrada_id.delete(0,END)
        except ValueError:
            messagebox.showerror("ERROR","INGRESE UN DATO EN LA ID:")
            return
    def validr_edad(self,new_value):
        if len(new_value) <= 3 :
            return True
        else:
            return False    
    def validr_nombre(self,new_value):
        if len(new_value) <= 10 :
            return True
        else:
            return False 
    def validr_curp(self,new_value):
        if len(new_value) <= 18:
            return True
        else:
            return False    
    def validar_matri(self,new_value):
        if len(new_value) <= 10 :
            return True
        else:
            return False      
    def validr_id(self,new_value):
        if len(new_value) <= 3 :
            return True
        else:
            return False    
    def validr_email(self,new_value):
        if len(new_value) <= 30 :
            return True
        else:
            return False    
    
    
    
    
    
    
    
    
    
    def wigets(self):
        ventana=Frame()
        vet=Frame()
        Label(ventana, text="Id:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_id = Entry(ventana)
        self.entrada_id.grid(row=0, column=1, padx=5, pady=5)
        vcmd1 = (ventana.register(self.validr_id), '%P')
        self.entrada_id.config(validate='key',validatecommand=vcmd1)     
        Label(ventana, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_nombre = Entry(ventana)
        self.entrada_nombre.grid(row=1, column=1, padx=5, pady=5)
        vcmd = (ventana.register(self.validr_nombre), '%P')
        self.entrada_nombre.config(validate='key',validatecommand=vcmd)
        Label(ventana, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
        self.entrada_edad = Entry(ventana)
        self.entrada_edad.grid(row=2, column=1, padx=5, pady=5)
        vcm = (ventana.register(self.validr_edad), '%P')
        self.entrada_edad.config(validate='key',validatecommand=vcm)
        Label(ventana, text="Email:").grid(row=3, column=0, padx=5, pady=5)
        self.entrada_email = Entry(ventana)
        self.entrada_email.grid(row=3, column=1, padx=5, pady=5)
        ve = (ventana.register(self.validr_email), '%P')
        self.entrada_email.config(validate='key',validatecommand=ve)
        Label(ventana, text="Curp :").grid(row=4, column=0, padx=5, pady=5)
        self.entrada_curp = Entry(ventana)
        self.entrada_curp.grid(row=4, column=1, padx=5, pady=5)
        c = (ventana.register(self.validr_curp), '%P')
        self.entrada_curp.config(validate='key',validatecommand=c)
        Label(ventana, text="Matricula:").grid(row=5, column=0, padx=5, pady=5)
        self.entrada_matricula = Entry(ventana)
        d = (ventana.register(self.validar_matri), '%P')
        self.entrada_matricula.config(validate='key',validatecommand=d)
        self.entrada_matricula.grid(row=5, column=1, padx=5, pady=5)
        Label(ventana, text="@gmail.com").grid(row=3, column=2, padx=5, pady=5)
        # Crear los botones para agregar, actualizar y eliminar alumnos
        Button(ventana, text="Agregar alumno", command=self.agregar_alumno).grid(row=7, column=1, padx=5, pady=5)
        Button(ventana, text="Actualizar alumno", command=self.actualizar_alumno).grid(row=8, column=1, padx=5, pady=5)
        Button(ventana, text="Eliminar alumno", command=self.eliminar_alumno).grid(row=9, column=1, padx=5, pady=5)
        Button(ventana, text="visualizar tabla", command=self.mostrarP).grid(row=10, column=1, padx=15, pady=5)
        Button(ventana, text="Limpiar", command=self.limpiar).grid(row=11, column=1, padx=15, pady=5)

        self.table = ttk.Treeview(vet)
        self.table.config(show='headings')
        self.table.place(x=0,y=0,height=400,width=400)

# Definir columnas

        self.table['columns'] = ('id', 'nombre','edad', 'email', 'curp','matricula')

# Formatear columnas
        self.table.column('#0', width=0,stretch=tk.NO)
        self.table.column('id', anchor=tk.CENTER, width=30)
        self.table.column('nombre', anchor=tk.W, width=50)
        self.table.column('edad', anchor=tk.W, width=50)
        self.table.column('email', anchor=tk.CENTER, width=50)
        self.table.column('curp', anchor=tk.CENTER, width=50)
        self.table.column('matricula', anchor=tk.CENTER, width=60)

# Agregar encabezado
        self.table.heading('#0', text='', anchor=tk.W)
        self.table.heading('id', text='id', anchor=tk.CENTER)
        self.table.heading('nombre', text='nombre', anchor=tk.W)
        self.table.heading('edad', text='edad', anchor=tk.W)
        self.table.heading('email', text='email', anchor=tk.CENTER)
        self.table.heading('curp', text='curp', anchor=tk.W)
        self.table.heading('matricula', text='matricula', anchor=tk.CENTER)
 # Ajustar tamaño de la tabla
        ventana.config(width=200,height=500)
        vet.config(width=900,height=1300)
        ventana.place(x=0,y=0)
        vet.place(x=200,y=0)
    def inserta(self,nombre, edad, email,curp,matricula):
        curursor = self.db.cursor()
        sentencia='''INSERT INTO alumnos (nombre,edad,email,curp,matricula) VALUES ('{}','{}','{}','{}','{}')'''.format(nombre, edad, email,curp,matricula)
        curursor.execute(sentencia)
        self.db.commit()    
        curursor.close()
    def elimina(self,id):
        cur = self.db.cursor()
        sentencia='''DELETE FROM alumnos WHERE id = {}'''.format(id)
        cur.execute(sentencia)
        self.db.commit()    
        cur.close()
    def mostrar(self):
        cursor = self.db.cursor()
        sentencia = "SELECT * FROM alumnos" 
        cursor.execute(sentencia)
        registro = cursor.fetchall()
        return registro
    def validar_edad(self,edad):
            try:
                edad_int = int(edad)
                return 1 <= edad_int <= 100
            except ValueError:
                return False
    def validar_matricula(self,edad):
            if len(edad)!=10:
                return False
            else :
                return bool(re.match("^[0-9]+[0-9]$",edad))
    def validar_nombre(self,nombre):
            return bool(re.match(r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z])$", nombre))
    def validar_email(self,email):
        chars = list(email)
        va=None
        vass=[]
        ty=None
        varg=len(chars)
        for i in range(0,varg):
            if re.match(r"@",chars[i]):
                vass=email.split("@")
                if len(vass[1])<=0:
                    ty=False
                elif len(vass[0])<10:
                    ty=False
                else:
                    ty=True
                    tt=len(vass[0])
                    for i in range(0,tt):
                        if re.match(r"[a-zA-Z1-9_-]",chars[i]):
                            pass
                        else:
                            ty=False
                        if  re.match(r"^gmail.com$",vass[1]):
                            va=True
                        elif re.match(r"^hotmail.com$",vass[1]):
                            va=True 
                        elif re.match(r"^outlook.com$",vass[1]):
                             va=True
                        else:
                            va=False
            
        if va==True and ty==True:
            return True
        else:
            return False
    def validar_curp(self,curp):
        contar=0
        so=list(curp)
        cha=["0","1","2","3","4","5","6","7","8","9"]
        for y in range(0,len(so)):
            for i in range(0,len(cha)):
                if so[y]==cha[i]:
                    contar=contar+1
        if contar>3 and contar<10 and len(curp)==18:
            return bool(re.match("^[A-Z0-9]+[A-Z0-9]$",curp))
        else:
            return False
            
        
    def agregar_alumno(self):
        self.table.get_children()
        nombre =self.entrada_nombre.get()
        if self.validar_nombre(nombre)==False:
            messagebox.showerror("error el nombre es invalido","ingrese solo letras             ")
            return
        edad =self.entrada_edad.get()
        if self.validar_edad(edad)==False:
            messagebox.showerror("La edad es invalida","has agregado una dato que es invalido \n solo agrega una edad de menor a 99 años")
            return
        email =self.entrada_email.get()
        if self.validar_email(email)==False:
            messagebox.showerror("tienes el gmail mal escrito","agrega el gmail correcto      ")
            return
        curp=self.entrada_curp.get()
        if self.validar_curp(curp)==False:
            messagebox.showerror("tienes el CURP mal escrito","DEBES DE POBNER BIEN LA CURP         \nojo las curps deben tener 18 caracteres\n(letras MAYUSCULAS Y de 4 a 9 numeros)")
            return
        
        matricula=self.entrada_matricula.get()
        if self.validar_matricula(matricula)==False:
            messagebox.showerror("Error al agregar la matricula","agrega solo numeros para la matricula \nson 10 digitos en la matricuula")
            return
        vas=""
        datos=(vas,nombre, edad, email,curp,matricula)
        if nombre and edad and email and curp and matricula!=' ':
         self.table.insert('',0,text=vas,values=datos)
         self.inserta(nombre,edad, email,curp,matricula)
         self.entrada_nombre.delete(0, END)
         self.entrada_edad.delete(0, END)
         self.entrada_email.delete(0, END)
         self.entrada_curp.delete(0, END)
         self.entrada_matricula.delete(0, END) 
    def limpiar(self):
         self.entrada_id .delete(0, END)
         self.entrada_nombre.delete(0, END)
         self.entrada_edad.delete(0, END)
         self.entrada_email.delete(0, END)
         self.entrada_curp.delete(0, END)
         self.entrada_matricula.delete(0, END)                	  	  	
    def mostrarP(self):
        self.table.delete(*self.table.get_children())
        registro = self.mostrar()
        i = -1
        for dato in registro: # type: ignore 
            i= i+1                       
            self.table.insert('',i, text = registro[i][1:1], values=registro[i][0:6]) # type: ignore
    
    

root=tk.Tk()
root.title("......")
root.geometry("602x400")
root.resizable(False,False)
van=proveedor(root) 
van.mainloop()
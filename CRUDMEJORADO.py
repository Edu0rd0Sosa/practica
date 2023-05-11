import tkinter as tk
from tkinter import Label,Frame,ttk,Button,Entry,END
import mysql.connector
from tkinter import messagebox
import re
class proveedor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        try:
          self.db = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="escuela")
        except mysql.connector.Error as e:
            messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
            exit()
       
        print(self.validar_email("mynamnesoaverra@gmail.com"))
        self.wigets()
    def validar_email(self,email):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(expresion_regular,email) is not None

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
        
        if self.validar_email(email)==False:
            messagebox.showerror("gmail esta mal","No cumples con los requisitos \n ejemplo: mynamesoaverra@gmail.com")
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
        id=self.entrada_id.get()
        if id=="":
            messagebox.showerror("ERROR","INGRESE UN DATO EN LA ID:")
            return  
        self.elimina(id)
    def wigets(self):
        ventana=Frame()
        vet=Frame()
        Label(ventana, text="Id:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_id = Entry(ventana)
        self.entrada_id.grid(row=0, column=1, padx=5, pady=5)
        
        Label(ventana, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_nombre = Entry(ventana)
        self.entrada_nombre.grid(row=1, column=1, padx=5, pady=5)
        
        Label(ventana, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
        self.entrada_edad = Entry(ventana)
        self.entrada_edad.grid(row=2, column=1, padx=5, pady=5)
        
        Label(ventana, text="Email:").grid(row=3, column=0, padx=5, pady=5)
        self.entrada_email = Entry(ventana)
        self.entrada_email.grid(row=3, column=1, padx=5, pady=5)
        
        Label(ventana, text="Curp :").grid(row=4, column=0, padx=5, pady=5)
        self.entrada_curp = Entry(ventana)
        self.entrada_curp.grid(row=4, column=1, padx=5, pady=5)
        
        Label(ventana, text="Matricula:").grid(row=5, column=0, padx=5, pady=5)
        self.entrada_matricula = Entry(ventana)
        self.entrada_matricula.grid(row=5, column=1, padx=5, pady=5)
        Label(ventana, text="@gmail.com").grid(row=3, column=2, padx=5, pady=5)
        # Crear los botones para agregar, actualizar y eliminar alumnos
        Button(ventana, text="Agregar alumno", command=self.agregar_alumno).grid(row=7, column=1, padx=5, pady=5)
        Button(ventana, text="Actualizar alumno", command=self.actualizar_alumno).grid(row=8, column=1, padx=5, pady=5)
        Button(ventana, text="Eliminar alumno", command=self.eliminar_alumno).grid(row=9, column=1, padx=5, pady=5)
        Button(ventana, text="visualizar tabla", command=self.mostrarP).grid(row=10, column=1, padx=15, pady=5)

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
    def agregar_alumno(self):
        self.table.get_children()
        nombre =self.entrada_nombre.get()
        edad =self.entrada_edad.get()
        email =self.entrada_email.get()
        curp=self.entrada_curp.get()
        matricula=self.entrada_matricula.get()
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
    def mostrarP(self):
        self.table.delete(*self.table.get_children())
        registro = self.mostrar()
        i = -1
        for dato in registro:
            i= i+1                       
            self.table.insert('',i, text = registro[i][1:1], values=registro[i][0:6]) # type: ignore
    
    

root=tk.Tk()
root.title("......")
root.geometry("602x400")
root.resizable(False,False)
van=proveedor(root) 
van.mainloop()
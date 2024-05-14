class cliente:
    def __init__(self, nombre, email, telefono, direccion):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
    
    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"Email actualizado a: {self.email}")
    
    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print(f"Teléfono actualizado a: {self.telefono}")
    
    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"Dirección actualizada a: {self.direccion}")

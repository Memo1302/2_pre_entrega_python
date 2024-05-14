from Clientes import cliente

def main():
    # Crear un cliente
    cliente1 = cliente("Nina Ramos", "nina@gmail.com", "2234-558121", "Zanni 1185")

    # Mostrar la información del cliente
    cliente1.mostrar_informacion()

    # Actualizar el email del cliente
    cliente1.actualizar_email("nina@gmail.com")

    # Actualizar el teléfono del cliente
    cliente1.actualizar_telefono("2234-558121")

    # Actualizar la dirección del cliente
    cliente1.actualizar_direccion("Zanni 1185")

    # Mostrar la información actualizada del cliente
    cliente1.mostrar_informacion()

if __name__ == "__main__":
    main()

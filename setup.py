from Clientes import setup, find_packages

setup(
    name="crear_cliente",
    version="0.1",
    packages=find_packages(),
    description="Paquete para crear clientes en una página de compras",
    author="Ramos Emiliano Alberto",
    author_email="emilianomemo@gmail.com",
    url="https://github.com/tu_usuario/mi_paquete_cliente",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

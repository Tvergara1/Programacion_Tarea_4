class Cliente:
    def __init__(self, nombre, email):
        self.set_nombre(nombre)
        self.set_email(email)

    def set_nombre(self, nombre):
        if not nombre or len(nombre) < 2:
            raise ValueError("Nombre inválido")
        self.__nombre = nombre

    def set_email(self, email):
        if "@" not in email:
            raise ValueError("Email inválido")
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email
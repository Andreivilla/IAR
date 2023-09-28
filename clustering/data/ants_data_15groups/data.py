class Data:
    def __init__(self, name, x=None, y=None):
        self.name = name
        self.x = x
        self.y = y

    #get e setter
        # Getter para o atributo 'name'
    def get_name(self):
        return self.name

    # Setter para o atributo 'name'
    def set_name(self, new_name):
        self.name = new_name

    # Getter para o atributo 'x'
    def get_x(self):
        return self.x

    # Setter para o atributo 'x'
    def set_x(self, new_x):
        self.x = new_x

    # Getter para o atributo 'y'
    def get_y(self):
        return self.y

    # Setter para o atributo 'y'
    def set_y(self, new_y):
        self.y = new_y


    def __str__(self):
        # Retorna uma representação de string dos valores da instância
        return self.name#f"Name: {self.name}, x: {self.x}, y: {self.y}"


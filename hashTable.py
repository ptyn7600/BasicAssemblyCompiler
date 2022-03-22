class hashTable:
    table = {}
    s_register = {"avail": [0, 1, 2, 3, 4, 5, 6, 7], "used": []}
    t_register = {"avail": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "used": []}

    def __init__(self):
        pass

    def add_variable(self, var_name, var_type, var_const):
        register = self.t_register["avail"].pop(0)
        self.t_register["used"].append(register)
        register = "$t" + str(register)
        self.table[var_name] = [var_type, var_const, register]

    def get_type(self, name):
        return self.table[name][0]

    def get_value(self, name):
        return self.table[name][1]

    def get_register(self, name):
        return self.table[name][2]

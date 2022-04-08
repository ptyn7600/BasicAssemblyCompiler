class hashTable:
    table = {}
    table_reg_name = {}
    s_register = {"avail": [0, 1, 2, 3, 4, 5, 6, 7], "used": []}
    t_register = {"avail": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "used": []}

    def __init__(self):
        pass

    def add_argument(self, var_name, var_type, var_const):
        register = self.s_register["avail"].pop(0)
        self.s_register["used"].append(register)
        register = "$s" + str(register)
        self.table[var_name] = [var_type, var_const, register]
        self.table_reg_name[register] = var_name
        return register

    def add_variable(self, var_name, var_type, var_const):
        register = self.t_register["avail"].pop(0)
        self.t_register["used"].append(register)
        register = "$t" + str(register)
        self.table[var_name] = [var_type, var_const, register]
        self.table_reg_name[register] = var_name
        return register

    # def update_variable(self, var_name, var_const):
    #     self.table[var_name][1] = var_const

    def get_type(self, name):
        return self.table[name][0]

    def get_value_from_name(self, name):
        return self.table[name][1]

    def get_value_from_register(self, register):
        if (register.isdigit()):
            return register
        return self.table[self.get_name_from_register(register)][1]

    def get_register(self, name):
        return self.table[name][2]

    def get_name_from_register(self, register):
        return self.table_reg_name[register]

    def isName(self, name):
        print("check name " + name)
        print(name in self.table)
        return (name in self.table)

    def isRegister(self, register):
        print("check register " + register)
        print(register in self.table_reg_name)
        return (register in self.table_reg_name)

    def printTable(self):
        print(self.table)
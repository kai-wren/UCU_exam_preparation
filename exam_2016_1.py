class Boolean: 

    def and_meth(self, bool_param):
        return 'Undefined'

class True_class(Boolean):
    def and_meth(self, bool_param):
        if (bool_param == True):
            return True
        else:
            return False

class False_class(Boolean):
    def and_meth(self, bool_param):
        if (bool_param == False):
            return True
        else:
            return False

t = True_class()
f = False_class()
test_bool = False
print(t.and_meth(test_bool))
print(f.and_meth(test_bool))
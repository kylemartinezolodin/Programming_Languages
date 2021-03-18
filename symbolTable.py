import sys
from lexer import TokenType

class SymbolTable:
    def __init__(self, parser):
        self.parser = parser
        self.table = list()

    def doesNotExist(self, identifier):
        for x in self.table:
            if x.identity == identifier:
                return False
        return True
    
    def lookup(self, identity):
        for x in self.table:
            if x.identity == identity:
                return x
        self.abort("Lookup Error, identifier \"" +identity +"\" does not exist")
        

    def insert(self, symb):
        if self.doesNotExist(symb):
            self.table.append(symb)
            return True
        else:
            return False

    def update(self, identifier, value):
        if self.doesNotExist(identifier):
            return None
        else:
            for x in self.table:
                if x.identity == identifier:
                    x.value = value
    
    def getdatatype(self, identifier):
        return self.lookup(identifier).dataType

    def setdatatype(self, identifier, dataType):
        self.lookup(identifier).dataType = dataType

    def abort(self, message):
        sys.exit("Symbol-Table error @ line " +str(self.parser.curLine) +", col " +str(self.parser.curCol) +"\n" + message)


class Symbol:
    def __init__(self, identity, dataType = None, value = None):
        self.identity = identity
        self._dataType = dataType
        self._value = value

    def getDataType(self):
        return self._dataType

    def setDataType(self, symboType):
        #print(self.value, symboType)
        if self._value != None:
            if symboType == TokenType.STRING and type(self.value) != str:
                self.abort("Value assigned must be a STRING")
            elif symboType == TokenType.CHAR and type(self.value) != str:
                self.abort("Value assigned must be a CHAR")
            elif symboType == TokenType.INT and type(self.value) != int:
                if type(self.value) == float:
                    self.value = int(self.value)
                else:
                    self.abort("Value assigned must be a INT")
            elif symboType == TokenType.FLOAT and type(self.value) != float:
                if type(self.value) == int:
                    self.value = float(self.value)
                else:
                    self.abort("Value assigned must be a FLOAT")
            elif symboType == TokenType.BOOL and type(self.value) != bool:
                self.abort("Value assigned must be a BOOL")
                
        self._dataType = symboType

    dataType = property(getDataType, setDataType) # property() PYTHON BUILT FUNCTION READ MORE: https://www.geeksforgeeks.org/getter-and-setter-in-python/


    def getValue(self):
        return self._value
        
    def setValue(self, val):
        if self._dataType != None:
            if type(val) == str and len(val) == 1  and self.dataType != TokenType.CHAR and len(val) != 1:
                self.abort("Assigned value must be a "+ str(self.dataType)[10:])
            elif type(val) == str and len(val) != 1  and self.dataType != TokenType.STRING:
                self.abort("Assigned value must be a "+ str(self.dataType)[10:])
            elif type(val) == int and self.dataType != TokenType.INT:
                self.abort("Assigned value must be a " + str(self.dataType)[10:])
            elif type(val) == float and self.dataType != TokenType.FLOAT:
                self.abort("Assigned value must be a " + str(self.dataType)[10:])
            elif type(val) == bool and self.dataType != TokenType.BOOL:
                self.abort("Assigned value must be a "+ str(self.dataType)[10:])

        self._value = val

    value = property(getValue, setValue) # property() PYTHON BUILT FUNCTION READ MORE: https://www.geeksforgeeks.org/getter-and-setter-in-python/
        
    # @property # A PHTON PROPERTY-GETTER DECORATOR, READ MORE: https://www.geeksforgeeks.org/getter-and-setter-in-python/
    # def dataType(self):
    #     return self._dataType

    # @dataType.setter # A PHTON PROPERTY-SETTER DECORATOR, READ MORE: https://www.geeksforgeeks.org/getter-and-setter-in-python/
    # def dataType(self, symboType):
    #     if self._value != None:
    #         pass

    # @property  # A PHTON PROPERTY-GETTER DECORATOR, READ MORE: https://www.geeksforgeeks.org/getter-and-setter-in-python/
    # def value(self):
    #     return self._value

    # @value.setter # A PHTON PROPERTY-SETTER DECORATOR, READ MORE: https://www.geeksforgeeks.org/getter-and-setter-in-python/
    # def value(self, val):
    #     if self._value != None:
    #         pass
    
    def abort(self, message):
        sys.exit("Symbol error for \"" +self.identity +"\" identifier \n" + message)

    


class constructor:
    def __init__(self,name):
        self.baseq ="""for $s in ("""+name+")\n"
        self.returnq = """return"""

'''Multiband Query Type'''
class multiBand(constructor):
    def __init__(self,name1,name2):
        self.returntype= ""
        self.baseq ="""for $s in ("""+name1+"""),
            $d in ("""+name2+")"
        self.returnq = """
        return
            encode(
                """
        self.addencodestruct()
    def addencodestruct(self):
        str1 = input("Please enter the struct: ")
        str2 = input("Please enter the encoding type: ")
        self.returntype = str2
        self.returnq += str1 + ",\n\"" + str2 + "\"\n)"
    def returntypefunc(self):
        return self.returntype
    def getquery(self):
        return self.baseq + self.returnq
    
'''Induced Operation Query Type'''
class inducedOperation(constructor):
    def __init__(self,name):
        self.returntype= ""
        self.baseq ="""for $s in ("""+name+")\n"
        
        self.returnq=   """return
        encode
                switch
                    """
        self.addencodetype()
    def addencodetype(self):
        str1 = input("Please enter the switch statement: ")
        str2 = input("Please enter the encoding type: ")
        self.returntype = str2
        self.returnq +=  str1 +"," +"\n"+'\"'+str2 + '\"'+"\n)"
    def returntypefunc(self):
        return self.returntype
    def getquery(self):
        return self.baseq + self.returnq
    
'''Coverage Filtering Query Type'''
class coverageFiltering(constructor):
    def __init__(self,name):
        self.returntype = ""
        self.baseq ="""for $s in ("""+name+")\n"
        self.returnq = """return"""
        self.addwhere()
    def addwhere(self):
        str1 = input("Please enter the where condition: ")
        str2 = input("Please enter the return value: ")
        self.returntype = str2
        self.where = """where """ + str1+"\n"
    def returntypefunc(self):
        return self.returntype
    def getquery(self):
        return self.baseq + self.where + self.returnq + self.returntype

'''Coverage Subsetting Query Type'''
class coverageSubsetting:
    def __init__(self,name):
        self.returntype =""
        self.baseq ="""for $c in ("""+name+")"
        self.query ="""$c"""
        self.returnq = """
        return
            encode(
                """
        self.setsubsetting()
    def setsubsetting(self):
        str1 = input("Please enter the Latitiute slice: ")
        str2 = input("Please enter the Longitute slice: ")
        str3 = input("Please enter the date: ")
        str4 = input("Please enter the date second subset: ")
        str5 = input("Please enter the encoding type: ")
        self.returntype = str5
        self.query += "[ Lat(" +str1+ "), Long( " + str2 +"), ansi(\""+str3+"\" : \""+str4+"\") ]"
        self.returnq += self.query + ",\n\"" + self.returntype + "\"\n)"
    def returntypefunc(self):
        return self.returntype
    def getquery(self):
        return self.baseq + self.returnq

'''Coverage Condensor Query Type'''
class coverageCondensor(constructor):
    def __init__(self,name):
        self.returntype = ""
        self.baseq ="""for $c in ("""+name+")\n"
        self.query =""""""
        self.returnq = """return """
        self.optype()
    def optype(self):
        str1 = input("Please enter the operation type: ")
        str2 = input("Please enter the Latitiute slice: ")
        str3 = input("Please enter the Longitute slice: ")
        str4 = input("Please enter the date: ")
        str5 = input("Please enter the date second subset: ")
        self.query += "($c[ Lat(" +str2+ "), Long( " +str3+ "), ansi(\""+str4+"\" : \""+str5+"\")])"
        self.returnq += "\n" + "    "+str1 +self.query
    def returntypefunc(self):
        return self.returntype
    def getquery(self):
        return self.baseq + self.returnq

'''Coverage Constrcutor Query Type'''
class coverageConstructor(constructor):
    def __init__(self,name):
        self.name = """coverage """+name+"""\n"""
        self.xover = """over    $px x in """
        self.yover = """        $py y in """
        self.values= """values  """
        self.addxcvrg()
        self.addycvrg()
        self.addvalues()
    def addxcvrg(self):
        str1 = input("Please enter the extent of your coverage on x axis: (Please enter imageCrsDomain if any) ")
        str1+=""",\n"""
        self.xover += str1
    def addycvrg(self):
        str1 = input("Please enter the extent of your coverage on y axis:  (Please enter imageCrsDomain if any) ")
        str1+="""\n"""
        self.yover += str1
    def addvalues(self):
        str1= input("Please enter the value type: ")
        str1 = "("+str1 +")"
        str2 = input("Please enter the operation to be performed on values: ")
        self.values = self.values + str1 + "(" + str2 + ")"

    def getquery(self):
        return self.name+self.xover+self.yover+self.values
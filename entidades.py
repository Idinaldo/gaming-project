class Game:
    def __init__(self, nome='', dev='', desc=''):
        self.__nome = nome
        self.__dev = dev
        self.__desc = desc

    def setNome(self, nome): 
        self.__nome = nome
    def getNome(self): 
        return self.__nome
    
    def setDev(self, dev): 
        self.__dev = dev
    def getDev(self): 
        return self.__dev
    
    def setDesc(self, desc): 
        self.__desc = desc
    def getDesc(self): 
        return self.__desc


        
class Sivitas:

    def __init__(self):
        self.__asal = ""
        self.__email = ""

    # set & get asal universitas
    def setAsalUniv(self, asal):
        self.__asal = asal

    def getAsalUniv(self):
        return self.__asal

    # set & get email
    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    # output
    def printSivitas(self):
        print("Asal Universitas     : " + self.getAsalUniv())
        print("Email Universitas    : " + self.getEmail())

from Human import Human
from Sivitas import Sivitas


class Dosen(Human):

    def __init__(self):
        self.__nip = ""
        self.__fakultas = ""
        self.__pendidikan = ""
        self.__keahlian = ""

        self.sivitas = Sivitas()  # composite sivitas

# setter and getter#
    def setNip(self, nip):
        # mengeset nilai nip Dosen
        self.__nip = nip

    def getNip(self):
        # mengembalikan nilai nip Dosen
        return self.__nip

    def setFakultas(self, fakultas):
        # mengeset nilai fakultas Dosen
        self.__fakultas = fakultas

    def getFakultas(self):
        # mengembalikan nilai fakultas Dosen
        return self.__fakultas

    def setPendidikan(self, pendidikan):
        # mengeset nilai pendidikan Dosen
        self.__pendidikan = pendidikan

    def getPendidikan(self):
        # mengembalikan nilai pendidikan Dosen
        return self.__pendidikan

    def setKeahlian(self, keahlian):
        # mengeset nilai keahlian Dosen
        self.__keahlian = keahlian

    def getKeahlian(self):
        # mengembalikan nilai keahlian Dosen
        return self.__keahlian

    def setNip(self, nip):
        # mengeset nilai nip Dosen
        self.__nip = nip

    def getNip(self):
        # mengembalikan nilai nip Dosen
        return self.__nip

# composite setter and getter

    def setSivitas(self, sivitas):
        self.sivitas = sivitas

    def getSivitas(self):
        return self.sivitas

# output
    def printDosen(self):
        print("NIP              : " + self.getNip())
        print("Fakultas         : " + self.getFakultas())
        print("Pendidikan       : " + self.getPendidikan())
        print("Keahlian         : " + self.getKeahlian())

        self.sivitas.printSivitas()

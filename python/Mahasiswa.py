from Human import Human
from Prodi import Prodi
from Sivitas import Sivitas


class Mahasiswa(Human):

    def __init__(self):
        self.__nim = ""
        self.__fakultas = ""

        self.prodi = Prodi()  # composite prodi
        self.sivitas = Sivitas()  # composite sivitas

 # setter and getter#

    def setFakultas(self, fakultas):
        # mengeset nilai fakultas Mahasiswa
        self.__fakultas = fakultas

    def getFakultas(self):
        # mengembalikan nilai fakultas mahasiswa
        return self.__fakultas

    def setNim(self, nim):
        # mengeset nilai nim Mahasiswa
        self.__nim = nim

    def getNim(self):
        # mengembalikan nilai nim mahasiswa
        return self.__nim

# composite setter and getter
    def setProdi(self, prodi):
        self.prodi = prodi

    def getProdi(self):
        return self.prodi

    def setSivitas(self, sivitas):
        self.sivitas = sivitas

    def getSivitas(self):
        return self.sivitas


# print


    def printMahasiswa(self):
        print("NIM                 : " + self.getNim())
        print("Fakultas            : " + self.getFakultas())

        self.prodi.printProdi()
        self.sivitas.printSivitas()

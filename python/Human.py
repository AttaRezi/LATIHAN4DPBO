class Human:
    # private attr
    __nik = ""
    __nama = ""
    __gender = ""

    def __init__(self, nik, nama, gender):
        self.__nik = nik
        self.__nama = nama
        self.__gender = gender

        # setter and getter#

    def setNama(self, nama):
        # mengeset nilai nama Mahasiswa
        self.__nama = nama

    def getNama(self):
        # mengembalikan nilai nama mahasiswa
        return self.__nama

    def setNik(self, nik):
        # mengeset nilai nik Mahasiswa
        self.__nik = nik

    def getNik(self):
        # mengembalikan nilai nik mahasiswa
        return self.__nik

    def setGender(self, gender):
        # mengeset nilai gender Mahasiswa
        self.__gender = gender

    def getGender(self):
        # mengembalikkan nilai gender mahasiswa
        return self.__gender

    def printPerson(self):
        # menampilkan data untuk attribut manusia
        print("NIK                 : " + self.getNik())
        print("Nama                : " + self.getNama())
        print("Jenis Kelamin       : " + self.getGender())

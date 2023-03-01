from Course import Course


class Prodi:

    def __init__(self):
        self.__namaProdi = ""
        self.__kode = ""
        self.course = Course()  # composite course

#setter and getter
    def setProdi(self, prodi):
        # mengeset nilai prodi Mahasiswa
        self.__namaProdi = prodi

    def getProdi(self):
        # mengembalikan nilai prodi mahasiswa
        return self.__namaProdi

    def setKode(self, kode):
        # mengeset nilai kode Mahasiswa
        self.__kode = kode

    def getKode(self):
        # mengembalikan nilai kode mahasiswa
        return self.__kode

# composite course ke prodi
    def set_Course(self, course):
        self.course = course

    def get_Course(self):
        return self.course


# output

    def printProdi(self):
        print("Prodi yang diambil   : " + self.getProdi())
        print("Kode Prodi           : " + self.getKode())

        self.course.printCourse()

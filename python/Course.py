class Course:

    def __init__(self):
        self.__namaMK = ""

    def setCourse(self, course):
        # mengeset nilai Course Mahasiswa
        self.__namaMK = course

    def getCourse(self):
        # mengembalikan nilai Course mahasiswa
        return self.__namaMK

    def printCourse(self):
        print("Matkul yang diambil  : " + self.getCourse())

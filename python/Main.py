from Human import Human
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from Sivitas import Sivitas
from Prodi import Prodi
from Course import Course


# set 1 orang mahasiswa#

# set data kependudukan
Mahasiswa1 = Mahasiswa()
Mahasiswa1.setNik("120948203574")
Mahasiswa1.setNama("Atta Arrezie Kurnia")
Mahasiswa1.setGender("Laki laki")
# set data pelajar
Mahasiswa1.setNim("2006836")
Mahasiswa1.setFakultas("FPMIPA")

# set prodi mahasiswa hasil composite
p1 = Prodi()
p1.setProdi("Ilmu Komputer")
p1.setKode("1001")

# set course
listCourse = []
c1 = Course()
listCourse.append(c1.setCourse("Alpro1"))
listCourse.append(c1.setCourse("Alpro2"))
p1.set_Course(c1)

# set data sivitas
s1 = Sivitas()
s1.setAsalUniv("UPI")
s1.setEmail("atta@upi.edu")

# masukkan ke mahasiswa
Mahasiswa1.setProdi(p1)
Mahasiswa1.setSivitas(s1)


# set data dosen 1#

# set data kependudukan
Dosen1 = Dosen()
Dosen1.setNik("34023850130")
Dosen1.setNama("Bima Putra  Setiabudi, M.Pd")
Dosen1.setGender("Laki laki")
# set data dosen
Dosen1.setNip("2006836")
Dosen1.setFakultas("FPMIPA")
Dosen1.setPendidikan("Magister Pendidikan Ilmu Komputer")
Dosen1.setKeahlian("Software Engineer")

# set data sivitas
sd1 = Sivitas()
sd1.setAsalUniv("UPI")
sd1.setEmail("bima@upi.edu")

Dosen1.setSivitas(sd1)

# output#
print("=======================================")
print("      Informasi Mahasiswa 1")
print("=======================================")

Mahasiswa1.printPerson()
Mahasiswa1.printMahasiswa()

print("")

print("=======================================")
print("      Informasi Dosen 1")
print("=======================================")

Dosen1.printPerson()
Dosen1.printDosen()

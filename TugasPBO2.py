class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama#Inisialisasi atribut nama dengan nilai parameter nama
        self.nim = nim #Inisialisasi atribut nim dengan nilai parameter nim
        self.jurusan = jurusan #Inisialisasi atribut jurusan dengan nilai parameter jurusan   
    def tampilkan_info(self):
        print("Nama: ", self.nama)#Menampilkan nilai dari atribut nama
        print("NIM: ", self.nim)#Menampilkan nilai atribut nim
        print("Jurusan: ", self.jurusan)#menampilkan nilai dari atribut jurusan

class Jurusan:
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan#Inisialisasi atribut nama_jurusan dengan nilai parameter nama_jurusan
        self.daftar_mahasiswa = []
    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan :", self.nama_jurusan) #Menambahkan objek mahasiswa ke dalam atribut daftar_mahasiswa   
        for mahasiswa in self.daftar_mahasiswa:#Menampilkan nama jurusan dari universitas
            print("Nama: ", mahasiswa.nama)
            print("NIM: ", mahasiswa.nim)
            print()

class Universitas:
    def __init__(self, nama_universitas):#Inmemasukkan nilai atribut nama_universitas dengan nilai parameter nama_universitas
        self.nama_universitas = nama_universitas
        self.daftar_jurusan = []
    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)
    def tampilkan_daftar_jurusan(self):#Inisialisasi atribut daftar_jurusan dengan list kosong   
        print("Daftar Jurusan di Universitas :", self.nama_universitas) #membuat supaya dapat menampilkan nama universitas
        for jurusan in self.daftar_jurusan:
            print(jurusan.nama_jurusan)

universitas_xyz = Universitas("XYZ University")
jurusan_ti = Jurusan("Teknik Informatika")#Membuat jurusan dari universitas dengan nama jurusan "Teknik Informatika"
jurusan_te = Jurusan("Teknik Elektro")#membuat data dari jurusan lain
jurusan_tm = Jurusan("Teknik Mesin")
universitas_xyz.tambah_jurusan(jurusan_ti)
universitas_xyz.tambah_jurusan(jurusan_te)
universitas_xyz.tambah_jurusan(jurusan_tm)
while True:
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    universitas_xyz.tampilkan_daftar_jurusan()
    nama_jurusan_pilihan = input("Masukkan nama jurusan pilihan mahasiswa: ")
    jurusan_pilihan = None
    for jurusan in universitas_xyz.daftar_jurusan:
        if jurusan.nama_jurusan == nama_jurusan_pilihan:
            jurusan_pilihan = jurusan
            break
    if jurusan_pilihan is not None:
        mahasiswa = Mahasiswa(nama, nim, jurusan_pilihan.nama_jurusan)
        jurusan_pilihan.tambah_mahasiswa(mahasiswa)
        print("Mahasiswa berhasil ditambahkan.")#supaya data dapat ditambahkan mahasiswa wajib membuat data sesuai dengan daftar jurusan 
        #dan harus membuat data sesuai dengan bentuknya kapital apa tidak
    else:
        print("Jurusan tidak ditemukan.")
    lanjutkan = input("Tambahkan mahasiswa lagi? (tambah/berhenti) ")#nantinya data akan ditampilkan ketika mahasiswa memilih berhenti
    #data tersebut dapat diisi terus menerus lalu jika mahasiswa berhenti untuk menambahkan maka data dari daftar mahasiswa yang telah dimasukkan
    #akan tampil daftar mahasiswa Teknik Informatika
    if lanjutkan.lower() != "tambah":
        break

# Menampilkan daftar jurusan dan mahasiswa
universitas_xyz.tampilkan_daftar_jurusan()
for jurusan in universitas_xyz.daftar_jurusan:
    jurusan.tampilkan_daftar_mahasiswa()

class Mahasiswa:
   
    def __init__(self, nama, nim, jurusan):
        self.nama = nama  #Inisialisasi atribut nama dengan nilai parameter nama
        self.nim = nim  #Inisialisasi atribut nim dengan nilai parameter nim
        self.jurusan = jurusan  #Inisialisasi atribut jurusan dengan nilai parameter jurusan   
    def tampilkan_info(self):
        print("Nama: ", self.nama)  #Menampilkan nilai dari atribut nama
        print("NIM: ", self.nim)  #Menampilkan nilai atribut nim
        print("Jurusan: ", self.jurusan)  #Menampilkan nilai atribut jurusan

class Jurusan:
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan  #Inisialisasi atribut nama_jurusan dengan nilai parameter nama_jurusan
        self.daftar_mahasiswa = []  #Inisialisasi atribut daftar_mahasiswa dengan list kosong
    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)  #Menambahkan objek mahasiswa ke dalam atribut daftar_mahasiswa   
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan :", self.nama_jurusan)  #Menampilkan nama jurusan dari universitas
        for mahasiswa in self.daftar_mahasiswa:  #Melakukan iterasi untuk setiap objek mahasiswa dalam daftar_mahasiswa
            print("Nama: ", mahasiswa.nama)  #Menampilkan nama mahasiswa
            print("NIM: ", mahasiswa.nim)  #Menampilkan nim mahasiswa
            print()

class Universitas:
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas  #Inmemasukkan nilai atribut nama_universitas dengan nilai parameter nama_universitas
        self.daftar_jurusan = []  #Inisialisasi atribut daftar_jurusan dengan list kosong   
    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)  #menambah objek atribut jurusan ke dalam atribut daftar_jurusan    
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas :", self.nama_universitas)  #membuat supaya dapat menampilkan nama universitas
        for jurusan in self.daftar_jurusan:  #Melakukan iterasi untuk setiap objek jurusan dalam daftar_jurusan
            print(jurusan.nama_jurusan)  #Menampilkan nama jurusan

while True:
    universitas_xyz = Universitas("XYZ University") #Membuat objek universitas_xyz dengan nama universitas "XYZ University"kevi
    jurusan_ti = Jurusan("-Teknik Informatika")#Membuat jurusan dari universitas dengan nama jurusan "Teknik Informatika"
    jurusan_te = Jurusan ("-Teknik Elektro")#membuat data dari jurusan lain
    jurusan_tm = Jurusan("-Teknik Mesin")
    universitas_xyz.tambah_jurusan(jurusan_ti)#Menambahkan objek jurusan_ti ke dalam atribut daftar_jurusan objek universitas_xyz
    universitas_xyz.tambah_jurusan(jurusan_te)
    universitas_xyz.tambah_jurusan(jurusan_tm)
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    mahasiswa_nama = Mahasiswa(nama, nim, jurusan_ti.nama_jurusan)#Membuat data diri
    jurusan_ti.tambah_mahasiswa(mahasiswa_nama)
    universitas_xyz.tampilkan_daftar_jurusan()
    jurusan_ti.tampilkan_daftar_mahasiswa()
    lanjutkan = input("Tambahkan mahasiswa lagi? (lanjut/berhenti) ")
    if lanjutkan.lower() != "lanjut":
        break

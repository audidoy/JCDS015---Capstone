# Student Grade List (Daftar Nilai Siswa)
  ## For Capstone Project Modul 1 - JCDS015 - 

Program ini dibuat untuk dapat **mengelola dan mengakses daftar nilai siswa**, dengan catatan pengolahan data nilai/fungsi utama guru **hanya dapat diakses** diakses oleh **guru** dengan **profesi sebagai wali kelas**. 
Program memiliki fitur **cancel input** membatalkan proses untuk setiap kali program meminta input dan membawa user kembali ke menu sebelumnya.

Program ini dapat digunakan oleh dua user:
* Guru: Wali Kelas
* Murid

Untuk menggunakan program ini, pastikan anda telah menginstall modul berikut di perangkat anda:
    
    pip install tabulate
    pip install regex

Berikut adalah kolom dalam database di program ini:

**Database_teacher**
| Nama Kolom | Tipe data | Range | Deskripsi |
|------------|-----------|-------|-----------|
| NIP | str | - | Nomor Induk Pegawai|
| Nama | Str | - | Nama Lengkap|
| Kota | Str | - | Alamat |
| Profesi | Str | - | Status sebagai pengajar|
| Password| Str | atleast: 1 Uppercase, 1 lowercase, 1 symbol, 1 number | Nomor Induk Pegawai|
| Pertanyaan | Str |min 4 char with no symbol | Pertanyaan untuk lupa password|
| Jawaban | Str | min 4 char with no symbol | Jawaban untuk lupa password|

**Database_Student**
| Nama Kolom | Tipe data | format | Range | Deskripsi |
|------------|-----------|------- |-------|-----------|
| Kode | Int | min 1 char |  - | No. penginputan data siswa ke database|
| NIS | Str | 12 char | ST20XX010900Y, XX = 2 digit akhir tahun pendaftaran, Y = identifier siswa | Nomor Induk Siswa|
| Nama | Str | - | - | Nama Lengkap|
| J Kel | Str | Laki-laki/Perempuan| - | Jenis Kelamin |
| Alamat | Str | min 4 char| - | Alamat Siswa |
| IPA | int | 0-100| - | Nilai IPA |
| IPS | int | 0-100| - | Nilai IPS |
| MTK | int | 0-100| - | Nilai MTK |
| Avg | float | 0-100| - | Nilai Rata-Rata|
| Stat |Str | 0-100| - | Satus Kenaikan Kelas |

## Log-in Menu: Interface awal saat menjalankan program
  #### 1.	Masuk sebagai guru
  * Pada bagian ini, akan dilakukan validsi user terlebih dahulu.
  * Akan dilakukan pengecekan apakah NIP terdata, kemudian apakah password akun yang dimasukkan sesuai atau tidak dengan database, dan pengecekan profesi guru ‘Wali Kelas’ atau tidak.
  * Terdapat fitur ‘lupa password’ yang bisa digunakan oleh user. Jika user menggunakan fitur lupa password, maka akan dikeluarkan pertanyaan yang terdata, dan user diminta untuk memasukkan jawaban. 
  #### 2. Masuk sebagai siswa
  Validasi hanya dilakukan menggunakan NIS siswa
  #### 3.	Keluar
  Fitur ini akan mengeluarkan user dari program

## Teacher Main Menu
Anda akan masuk dan kedalam teacher main menu jika telah tervalidasi sebagai guru: wali kelas saat log-in, dan dapat mengakses beberapa sub menu dibawah ini:
### 1. Read data saya
Program hanya akan menampilkan data milik user saja sesuai dengan NIP yang dimasukkan saat login.
### 2. Update Data Saya
 * sub menu ini di desain untuk memiliki fungsi yang hanya dapat mengubah data user berupa: Password, Pertanyaan dam Jawaban.
 * Untuk data lain tidak dapat diubah, perubahan data tersebut hanya boleh dilakukan oleh tim Tata Usaha.
 * Setiap kali dilakukan perubahan data oleh user, akan dilakukan pengecekan nilai input terlebih dahulu. Jika nilai input sama dengan nilai sebelumnya pada database_teacher, maka akan dikeluarkan pesan bahwa data yang dimasukkan sama dengan data sebelumnya, dan tersedia pilihan mau melakukan perubahan kembali atau tidak.
### 3. Tampilkan Data Siswa
* Sub menu ini akan menampilkan data nilai siswa
* Pada tampilan awal sub menu ini akan ditampilkan seluruh data siswa yang ada didalam database. Didalam menu ini terdapat 3 pilihan tampilan yaitu: 1) urutkan berdasarkan NIS, 2) Urutkan dari nilai tertinggi, 3) filter siswa dengan status tidak naik kelas. Jika siswa dengan status tidak naik kelas tidak tersedia, maka program akan menunjukkan data tidak tersedia.
* Jika data siswa tidak tersedia didalam database_student, maka akan dikeluarkan pemberitahuan bahwa fungsi ini tidak dapat digunakan.
### 4. Tambah Data Siswa
* Sub menu ini dapat menambahkan data siswa kedalam data base yang ada.
* User akan diminta untuk memasukkan data kesetiap kolom yang ada kecuali
   * kode
   * Avg
   * Stat
* Ketiga kolom diatas akan mengenerate nilai sendiri saat user selesai memasukkan data yang diminta.
* Data yang diisikan tidak boleh kosong dan NIS tidak boleh berisi duplikat dari data yang sudah ada.
### 5. Ubah Data Siswa
* Sub menu ini dapat mengubah/ memperbarui data siswa yang ada. User akan diminta untuk memilih kode siswa yang ingin dirubah datanya, dan nomor dari opsi kolom yang diberikan. Kode tersebut harus tersedia didalam database yang ada. Jika data yang dirubah adalah nilai siswa, maka data kolom Avg dan Stat otomatis akan diperbaharui pula.
* Jika data siswa tidak tersedia didalam database_student, maka sub menu ini akan menampilkan pesan bahwa tidak ada data tersedia dan sub menu tidak dapat digunakan.
### 6. Hapus Data Siswa
* Sub menu ini memiliki fungsi untuk menghapus seluruh rangkaian data siswa dan hanya dapat dijalankan jika terdapat data siswa didalam databaase_student. Fungsi ini memiliki fitur untuk menghapus 1) berdasarkan kode, 2) berdasarkan NIS, 3) seluruh data siswa. User akan diminta untuk memasukkan Kode ataupun NIS, dan data Kode ataupun NIS tersebut harus tersedia didalam database program agar dapat menjalankan fitur ini.
* Jika data siswa tidak tersedia didalam database_student, maka sub menu ini akan menampilkan pesan bahwa tidak ada data tersedia dan sub menu tidak dapat digunakan.
### 7. Cari Data Siswa
*	Sub menu ini memiliki fungsi untuk menampilkan data siswa dengan pencarian.
*	Jika data siswa tidak tersedia didalam database_student, maka sub menu ini akan menampilkan pesan bahwa tidak ada data tersedia dan sub menu tidak dapat digunakan.
* Diberikan beberapa pilihan yaitu:
    * **Berdasarkan NIS**.
      User akan diminta untuk memasukkan NIS siswa yang terdata secara lengkap.
    * **Berdasarkan Nama Lengkap**
      User akan diminta untuk memasukkan Nama Lengkap siswa yang terdata
    * **Berdasarkan Keyword**
      Fitur ini dapat digunakan untuk mencari data siswa hanya dengan kata kunci yang terbagi atas beberapa opsi pencarian yaitu:
      * NIS
      * NAMA
      * ALAMAT
      * Jenis Kelamin.
* User akan diminta untuk memasukkan input sesuai dengan opsi yang dipilih oleh user.
### 8. Keluar
Sub menu ini akan membuat user keluar dari teacher_main_menu, dan kembali ke interface awal untuk login.

## Student Main Menu
Anda akan masuk kedalam **student main menu** jika telah **tervalidasi sebagai siswa** menggunakan NIS yang terdata didalam database_student
### 1. Read my data:
Sub menu ini akan menampilkan hanya data user, sesuai dengan NIS yang diinputkan.
### 2. Help Desk
Sub menu ini hanya akan menampilkan data tim terkait yang dapat dihubungi oleh user melalui e-mail.
### 3. Keluar
Sub menu ini akan membuat user keluar dari student main menu, dan kembali ke interface awal untuk login

## Notes 
Terdapat beberapa fungsi yang digunakan untuk memvalidasi input dari user yang dapat anda lihat setelah beberapa 










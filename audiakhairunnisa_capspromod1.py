# the moduls need to be installed on ur computer whenever u try to run this program:
# run this on your terinal
  #   pip regex
  #   pip install tabulate

from tabulate import tabulate
import regex as re
import time

database_teacher = [
    {'NIP': 'TH001', 
     'NAMA': 'Putri A.', 
     'KOTA': 'Jakarta', 
     'PROFESI': 'Wali Kelas',
     'PASS':'apa',
     'QUEST':'makanan favorite?',
     'JAWABAN':'sushi'},

    {'NIP': 'TH002',
     'NAMA': 'Syahrul F', 
     'KOTA': 'Makasar', 
     'PROFESI': 'Guru IPS',
     'PASS':'kue',
     'QUEST':'panggilan anda waktu kecil?', 
     'JAWABAN':'dodid'},
]

database_student = [
    {'KODE': 1,
     'NIS': 'ST20210109001',
     'NAMA': 'Putri Risya A.',
     'J KEL': 'perempuan', 
     'ALAMAT': 'Bali',
     'IPA':89, 
     'IPS':90, 
     'MTK':85, 
     'AVG': 88, 
     'STAT':'Naik'},
     
    {'KODE': 2,
     'NIS': 'ST20210109002', 
     'NAMA': 'Irma Yani S.', 
     'J KEL':'perempuan', 
     'ALAMAT': 'Jakarta', 
     'IPA':81, 
     'IPS':96,
     'MTK':60,
     'AVG':79,
     'STAT':'Naik'},

    {'KODE': 3,
     'NIS': 'ST20220109003', 
     'NAMA': 'Risya P.', 
     'J KEL':'perempuan', 
     'ALAMAT': 'Jakarta',
     'IPA':77, 
     'IPS':88, 
     'MTK':90, 
     'AVG':85,
     'STAT':'Naik'},

    {'KODE': 4,
     'NIS': 'ST20210109009', 
     'NAMA': 'Reynaldi S.', 
     'J KEL':'laki-laki', 
     'ALAMAT': 'Jakarta',
     'IPA':72, 
     'IPS':59, 
     'MTK':53, 
     'AVG': 61.33,
     'STAT':'Tidak Naik'},

    {'KODE': 5,
     'NIS': 'ST20210109005', 
     'NAMA': 'Reynald P.', 
     'J KEL':'laki-laki', 
     'ALAMAT': 'Jakarta',
     'IPA':53, 
     'IPS':59, 
     'MTK':72, 
     'AVG': 61.33,
     'STAT':'Tidak Naik'}
]

database_answer_password = ['lupapassword','forgetpassword', 'forgotpassword',]
subjects = ['IPA', 'IPS', 'MTK']
input_yes = ['ya','iya','yes','y']
input_no = ['no','not','nah','n','tidak']
input_for_cancel = ['batal','Batal', 'cancel', 'Cancel']

#################################### short Funct
def print_data(data):
  print('## Data siswa saat ini ##')
  print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))

def input_lainya(prompt, current_value='null'):
    while True:
        inputan_lain = input(prompt).strip()
        if inputan_lain in input_for_cancel:
            return inputan_lain
        inputan_lain_new = inputan_lain.replace(' ', '').replace('.','').replace(',','').replace('-','')
        if inputan_lain == current_value:
            print('\nData yang dimasukkan sama dengan yang sebelumnya')
            return current_value

        elif inputan_lain_new.isalpha() or inputan_lain_new.isalnum():
            if len(inputan_lain) < 4 :
                print(
                    '''Input tidak valid. Masukkan:
                          1. minimal 4 karakter
                          2. tidak hanya berisikan angka
                          3. tidak mengandung simbol ''')
                continue
            else:
                if current_value == 'null':
                    return inputan_lain
                else:
                  print('Data berhasil diupdate')
                  return inputan_lain
        else:
            print('Input yang dimasukkan tidak valid. \nPastikan input anda tidak menggunakan simbol')

def input_password(prompt, current_value):
    symbols = '''!@#$%^&*()-_=+[]{}|;:'\",.<>?/'''
    while True:
        inputan_password = input(prompt)
        if inputan_password in input_for_cancel:
          return inputan_password
        if inputan_password == current_value:
          print('Password yang anda masukkan sama dengan yang sebelumnya')
          if not ask_again('\nApakah anda ingin mengubah password kembali? '):
            return current_value
        elif (any(c.isdigit() for c in inputan_password) and
              any(c.islower() for c in inputan_password) and
              any(c.isupper() for c in inputan_password) and
              any(c in symbols for c in inputan_password) ):
                print('Data Password anda berhasil di update!')
                return inputan_password
        else:
            print('\nPassword Anda tidak kuat.\nPastikan untuk menggunakan kombinasi huruf besar, huruf kecil, angka, dan simbol.')

def input_nis(prompt, data):
    while True:
        print("Format NIS =  ST20XX010900Y\nDimana XX adalah 2 digit tahun siswa terdaftar(21-24), dan Y identifier siswa")
        inputan_nis = input(prompt).upper().strip()
        if inputan_nis.lower() in input_for_cancel:
          return False
        if re.fullmatch(r"\bST202[1-4]0109\d{3}\b", inputan_nis):
            if any(value['NIS'] == inputan_nis for value in data):
                print('NIS sudah terdata untuk siswa lain.\nPeriksa kembali NIS siswa')
            else:
                return inputan_nis
        else:
            print('Input yang dimasukkan tidak valid.\nPastikan format NIS benar')

def input_numerik(prompt):
    while True:
      inputan_num = input(prompt).strip()
      if inputan_num in input_for_cancel:
        return inputan_num
        
      if inputan_num.isdigit():
          inputan_num = int(inputan_num)
          if 0 <= inputan_num <= 100:
            return inputan_num
          else:
              print('Input tidak valid. Masukkan angka antara 0 dan 100.\n')
      else:
          print('Input tidak valid. Masukkan angka.\n')

def input_string(prompt):
    while True:
        inputan_string = input(prompt).strip()
        if inputan_string in input_for_cancel:
            return inputan_string
        if inputan_string.replace(' ', '').replace('-', '').replace('.','').isalpha and len(inputan_string) >= 3:
            return inputan_string
        else:
            print('Input yang dimasukkan tidak valid.\nPastikan input lebih dari 3 karakter!')

def input_jk(prompt):
    while True:
      inputan_jk = input_string(prompt).strip()
      if inputan_jk.lower() in input_for_cancel:
          return inputan_jk
      inputan_jk_new = inputan_jk.replace(' ','').replace('-','').lower()
      if inputan_jk_new == 'lakilaki':
         return 'Laki-Laki'
      elif inputan_jk_new == 'perempuan':
          return 'Perempuan'
      else:
          print('Input yang dimasukkan tidak valid')

def input_cancel(val):
    if val in input_for_cancel:
        print('Proses dibatalkan')
        time.sleep(1)
        return True
    return False

############################### auto create funct
def avg(student):
    total_nilai = sum(student[subject] for subject in subjects)
    rata_rata = total_nilai / len(subjects)
    return round(rata_rata,2)

def create_new_code():
    if not database_student:
       kode_baru = 1
       return kode_baru
    kode_baru = max(user['KODE'] for user in database_student) + 1
    return kode_baru

def creat_status(student):
    rata_rata = avg(student)
    SB65 = sum(1 for subject in subjects if student[subject] < 65)
    if SB65 >= 2  or rata_rata < 65:
        return 'Tidak Naik'
    return 'Naik'

def ask_again(prompt):
  while True:
    inputan = input(prompt).strip()
    if inputan.lower() in input_yes:
      return True
    elif inputan.lower() in input_no:
      return False
    else:
      print('Input tidak valid. Silakan masukkan ya atau tidak')

################################################ start program

def prog_start():
  while True:

    print ('''
   ======================================================
  |        Academic Support Khavidien High School        |
  |              Mohon Verifikasi Diri Anda              |
   ======================================================

                    1. Masuk Sebagai Guru
                    2. Masuk Sebagai Siswa
                    3. Keluar Program ''')

    result = validate_user('\nMasukkan pilihan jawaban anda: ')
    if result == 'exit':
      return

# validating user
def validate_user(prompt):
  while True:
    input_valus = input_numerik(prompt)
    if input_valus == 1:
        nip, is_valid = valid_user_teacher()
        if not is_valid:
          time.sleep(3)
          return
        else:
          if not teacher_main_menu(nip):
            return 'return'
    elif input_valus == 2:
        nis, is_valid = valid_user_student()
        if not is_valid:
          time.sleep(3)
          return
        else:
          student_main_menu('masukkan pilihan anda: ', nis, database_student)
          return 'return'
    elif input_valus == 3:
        return 'exit'
    else:
        print('Input yang dimasukkan tidak valid')

# validating user = teacher
def valid_user_teacher():
    kesempatan = 3
    print('''
             ############# Anda Hanya memiliki 3 kesempatan! ############
            Jika lupa password tulis 'lupa password' pada bagian password\n''')
    for i in range(4):
        print(" *Untuk kembali ke menu login user, ketik 'batal' ")
        nip = input('Masukkan NIP anda: ').upper().strip()
        if input_cancel(nip):
            return False, False
        password = input('masukkan password anda: ')
        if input_cancel(password):
            return False, False
        value = find_teacher(nip, database_teacher)
        if value:
            if value['PASS'] == password:
                if value['PROFESI'] != 'Wali Kelas':
                  print('Maaf laman ini tidak tersedia untuk anda. \nAnda akan kembali ke menu utama secara otomatis')
                  return nip, False
                return nip, True
            elif password.replace(' ', '').lower() in database_answer_password:
                if not question_of_forgot_password(nip, 'Masukkan jawaban anda: '):
                    break
                if value['PROFESI'] != 'Wali Kelas':
                    print('Maaf laman ini tidak tersedia untuk anda. \nAnda akan kembali ke menu utama secara otomatis')
                    return nip, False
                print('\nSELAMAT! Anda berhasil masuk ke menu utama')
                return nip, True
            else:
                if kesempatan >= 1:
                    kesempatan -= 1
                    print('Password yang anda masukkan salah\n')
                    print(f'Attempts remaining: {kesempatan}')
                else:
                    print('Anda telah melakukan 3 kali salah percobaan.\nAnda akan keluar dari menu ini secara otomatis\nHubungi Tim IT untuk bantuan lebih lanjut')
                    break
        else:
            if kesempatan > 1:
                kesempatan -= 1
                print('NIP yang anda masukan salah/ tidak terdata.\nPeriksa kembali NIP yang anda masukkan\n')
                print(f'Attempts remaining: {kesempatan}')
            else:
                print('''Maaf anda tidak dapat mengakses laman ini untuk beberapa saat.\nSilahkan hubungi tim IT untuk bantuan lebih lanjut''')
                return nip, False
    return None, False

# finding the user
def find_teacher(nip, database):
    for value in database:
        if value['NIP'] == nip:
            return value
    return None

# validating user is teacher thru questions
def question_of_forgot_password(nip, prompt):
    count = 3
    value = find_teacher(nip, database_teacher)
    if value:
        while count >= 1:
            print('\n')
            print(value['QUEST'])
            print("*Untuk membatalkan dan kembali ke menu sebelumnya ketik 'batal'")
            answer = input(prompt).strip()
            if input_cancel(answer):
                return False
            if answer == value['JAWABAN']:
                password = value['PASS']
                return nip, True
            else:
                count -= 1
                print("Jawaban salah.\n")
                print(f'attempt remaining: {count}')
        print("Anda telah mencoba 3 kali. Silakan coba lagi nanti.")
    else:
      print('NIP tidak ditemukan')

    return None, False

################################## teacher main menu

def teacher_main_menu(nip):
    while True:
      print('''
=================================================
        MENU UTAMA LAMAN AKADEMIK WALIKELAS
=================================================
            ========================
            |      Data Saya       |
            ========================
            1. Tampilkan Data Saya
            2. Ubah Data Saya
            ========================
            |      Data siswa      |
            ========================
            3. Tampilkan Data Siswa
            4. Tambah Data Siswa
            5. Ubah Data Siswa
            6. Hapus Data Siswa
            7. Cari Data Siswa
            8. Keluar
''')
      inputan = input_numerik('Masukkan Menu: ')
      if inputan == 1:
          print('''\n## Data Guru ##\n''')
          read_teacher_data(nip, database_teacher)
      elif inputan == 2:
          update_data(2, nip, database_teacher)
      elif inputan == 3:
          read_op('Masukkan opsi tampilan lain yang anda inginkan: ',database_student) ############
      elif inputan == 4:
          create_data_student(database_student)
      elif inputan == 5:
          update_data(5, nip, database_student)
      elif inputan == 6:
          delete_data('Masukkan pilihan anda: ',database_student)
      elif inputan == 7:
          search_student(database_student)
      elif inputan == 8:
          break  # keluar
      else:
          print('menu tidak ada')

# -------------- 1 read teacher data
def read_teacher_data(nip, data):
      value = find_teacher(nip, database_teacher)
      if value:
        print(tabulate([value], headers='keys', tablefmt='pretty'))
        while True:
          if ask_again("Ketik 'ya' untuk kembali ke menu utama "):
            return
      else:
        print('NIP tidak ditemukan')

# ------------------2 update teacher data
def update_data(inputan, nip, data):
    if inputan == 2:
      value = find_teacher(nip, database_teacher)
      while True:
        if value:
          print('### Data anda saat ini ###')
          print(tabulate([value], headers='keys', tablefmt='pretty'))
          while True:
            print('\nAnda hanya dapat merubah data Password, Pertanyaan, dan Jawaban')
            print('''
            ==================================
            | Data apa yang ingin anda ubah? |
            ==================================
                    1. Password
                    2. Pertanyaan
                    3. Jawaban
                    4. Kembali ''')
            kolom = input_numerik('\nPilih nomor data yang ingin anda ubah: ')
            if input_cancel(kolom):
              break
            if kolom <= 4 and kolom > 0:
              if kolom == 1:
                  print("*Untuk membatalkan ketik 'batal'")
                  nilai = input_password('Masukkan password baru: ', value['PASS'])
                  if input_cancel(nilai):
                    break
                  value['PASS'] = nilai
              elif kolom == 2:
                  print("*Untuk membatalkan ketik 'batal'")
                  nilai = input_lainya('Masukkan pertanyaan baru: ', value['QUEST'])
                  if input_cancel(nilai):
                    break
                  value['QUEST'] = nilai
              elif kolom == 3:
                  print("*Untuk membatalkan ketik 'batal'")
                  nilai = input_lainya('Masukkan jawaban baru: ',value['JAWABAN'])
                  if input_cancel(nilai):
                    break
                  value['JAWABAN'] = nilai
              elif kolom == 4:
                  return
              print(f'\nData anda saat ini\n')
              print(tabulate([value], headers='keys', tablefmt='pretty'))
              break
            else:
                print('input anda tidak valid')
                continue
        else:
            print('NIP tidak ditemukan')
        if not ask_again('\nApakah anda ingin mengubah data kembali? '):
                  break
        
# --------------- 5 update student data    
    elif inputan == 5:
      while True:
        if not data:
          print('Fitur tidak dapat digunakan karena tidak ada data siswa yang tersedia. \nAnda akan kembali ke menu utama secara otomatis')
          time.sleep(4)
          return

        print_data(data)
        print('\n')
        while True:
            print("*Untuk membatalkan ketik 'batal'")
            row = input_numerik("Masukkan kode siswa yang ingin diubah data: ")
            if input_cancel(row):
              return
            row = row -1
            if row < 0 or row >= len(data):
                print("Kode siswa tidak valid. Silakan masukkan kode siswa yang valid.")
                break
            print('''
                  ========================================
                  | Data siswa apa yang ingin anda ubah? |
                  ========================================
                            1. NIS
                            2. Nama
                            3. Jenis Kelamin
                            4. Alamat
                            5. Nilai IPA
                            6. Nilai IPS
                            7. Nilai MTK
                            8. Kembali
                            ''')
            print("*Untuk membatalkan ketik 'batal'")
            kolom = input_numerik('\nPilih nomor data yang ingin anda ubah: ')
            if input_cancel(kolom):
              break
            if kolom <= 8 and kolom > 0:
              if kolom == 1 :
                  value = input_nis('masukkan NIS baru: ',data)
                  if not value:
                    break
                  data[row]['NIS'] = value
              elif kolom == 2:
                  value = input_string('masukkan Nama baru: ').title()
                  if input_cancel(value):
                    break
                  data[row]['NAMA'] = value
              elif kolom == 3:
                  value = input_jk('masukkan data jenis kelamin baru: ').title()
                  if input_cancel(value.lower()):
                    break
                  data[row]['J KEL'] = value
              elif kolom == 4:
                  value = input_lainya('masukkan alamat baru: ').title()
                  if input_cancel(value.lower()):
                    break
                  data[row]['ALAMAT'] = value
              elif kolom == 5 :
                  value = input_numerik('masukkan nilai IPA yang baru: ')
                  if input_cancel(value):
                    break
                  data[row]['IPA'] = value
              elif kolom == 6:
                  value = input_numerik('masukkan nilai IPS yang baru: ')
                  if input_cancel(value):
                    break
                  data[row]['IPS'] = value
              elif kolom == 7:
                  value = input_numerik('masukkan nilai MTK yang baru: ')
                  if input_cancel(value):
                    break
                  data[row]['MTK'] = value
              elif kolom == 8:
                  return
              if not input_cancel(value):
                  print('\nSelamat, data berhasil di update')
            else:
              print('input anda tidak valid')
              continue

            data[row]['AVG'] = avg(data[row])
            data[row]['STAT'] = creat_status(data[row])

            print_data(data)
            break
        if not ask_again('\nApakah anda ingin mengubah data kembali? '):
            break

# --------------- 3 print student data
def read_op(prompt, data):
  if not data:
    print('Fitur tidak dapat digunakan karena tidak ada data siswa yang tersedia. \nAnda akan kembali ke menu utama secara otomatis')
    time.sleep(4)
    return

  print(''' ### DEFAULT TABLE VIEW ### ''')
  print_data(data)
  while True:
    print('''
            ==================================
            |       Opsi tampilan lain       |
            ==================================
            1. Urutkan berdasarkan NIS
            2. Urutkan dari rata-rata tertinggi
            3. Tampilkan siswa tidak naik kelas
            4. Return
  ''')
    input_ro = input_numerik(prompt)
    if input_ro == 1:
      sorted_student('NIS', data)
    elif input_ro == 2:
      sorted_student('AVG', data)
    elif input_ro == 3:
      filtering_student(data)
    elif input_ro == 4:
      return
    else:
      print('Input tidak valid')
    if not ask_again('Apakah anda ingin melihat opsi tampilan lain?: '):
      return

def sorted_student(parameter, data):
    if not data:
      print('Fitur tidak dapat digunakan karena tidak ada data siswa yang tersedia. \nAnda akan kembali ke menu utama secara otomatis')
      time.sleep(4)
      return
    if parameter == 'AVG':
        sorted_data = sorted(data, key=lambda x: x[parameter], reverse=True)
    else:
        sorted_data = sorted(data, key=lambda x: x[parameter])
    print(f'### Data siswa diurutkan berdasarkan {parameter} ###')
    print_data(sorted_data)

def filtering_student(data):
    if not data:
      print('Fitur tidak dapat digunakan karena tidak ada data siswa yang tersedia. \nAnda akan kembali ke menu utama secara otomatis')
      time.sleep(4)
      return
    tidak_naik = list(filter(lambda value: value['STAT'] == 'Tidak Naik', data))
    if tidak_naik:
        print("\nData siswa yang tidak naik kelas:")
        print('## Data Siswa Tidak Naik ##')
        print_data(tidak_naik)
    else:
        print("\nTidak ada siswa yang tidak naik kelas.")

# ---------------------- 4 Add/ create student data
# create data
def create_data_student(data=None):
  if data is None:
    data = database_student
  while True:
    print("untuk membatalkan ketik 'batal'")
    kode = create_new_code()
    while True:    
      nis  = input_nis('Masukkan NIS: ',data)
      if not nis:
        print('Proses dibatalkan')
        time.sleep(1)
        break
      nama = input_string('Masukkan nama siswa: ').title()
      if input_cancel(nama):
        break
      jk = input_jk('Masukkan Jenis Kelamin siswa: ')
      if input_cancel(jk):
        break
      alamat = input_lainya('Masukkan alamat siswa: ').title()
      if input_cancel(alamat):
        break
      IPA = input_numerik('Masukkan nilai IPA: ')
      if input_cancel(IPA):
        break
      IPS = input_numerik('Masukkan nilai IPS: ')
      if input_cancel(IPS):
        break
      MTK = input_numerik('Masukkan nilai MTK: ')
      if input_cancel(MTK):
        break
      student = {'IPA': IPA, 'IPS': IPS, 'MTK': MTK}
      rata2 = avg(student)
      status = creat_status(student)

      data_baru = {'KODE': kode, 'NIS': nis, 'NAMA': nama, 'J KEL': jk, 
                   'ALAMAT': alamat, 'IPA': IPA, 'IPS': IPS, 'MTK': MTK, 
                   'AVG': rata2, 'STAT': status}
      data.append(data_baru)

      print(f'\ndata berhasil ditambahkan ke database')
      print_data(data)
      break

    if not ask_again('\nMasih ingin menambah data? '):
        print('Kembali ke menu utama')
        time.sleep(1)
        break

# ----------------------------- 6 delet student data
# delet data
def delete_data(prompt,data):
  while True:
    if not data:
      print('Fitur tidak dapat digunakan karena tidak ada data siswa yang tersedia. \nAnda akan kembali ke menu utama secara otomatis')
      time.sleep(4)
      return
    while True:
      print_data(data)
      print('''
              ==========================
              |    Hapus Data Siswa:   |
              ==========================
              1. Hapus berdasarkan Kode
              2. Hapus berdasarkan NIS
              3. Hapus seluruh data
              4. Return

      ### WARNING! ###
      Proses ini adalah penghapusan data siswa secara PERMANEN
      Fitur restore data saat ini belum tersedia
      ''')
      input_del = input_numerik(prompt)
      if input_cancel(input_del):
        break
      if input_del == 3:
        if ask_again('Apakah Anda yakin ingin menghapus semua data siswa? (ya/tidak): '):
            data.clear()
            print('\nSemua data siswa telah dihapus.\nAnda akan kembali ke menu utama secara otomatis')
            time.sleep(2)
            return
      elif input_del == 1:
        value = delete_by('KODE', database_student)
        if input_cancel(value):
            break
        break
      elif input_del == 2:
        value = delete_by('NIS', database_student)
        if input_cancel(value):
            break
        break
      elif input_del == 4:
        return
      else:
          print('menu tersebut tidak tersedia')

    if not ask_again('\nApakah anda ingin menghapus data kembali? '):
      return

def delete_by(x, data):
  while True:
    print("*Untuk membatalkan perintah ketik 'batal'")
    value = input(f'Masukkan {x} siswa yang ingin dihapus: ').strip()
    if input_cancel(value):
      return value
    if x == 'NIS' :
      if not re.fullmatch(r"\bST202[1-4]0109\d{3}\b", value):
        print('NIS yang anda masukkan tidak sesuai')
        continue
    elif x == "KODE":
      try:
        value = int(value)
      except ValueError:
        print('Kode yang anda masukkan tidak sesuai')
        continue

    if any(student[x] == value for student in data):
        student_to_delete = next(student for student in data if student[x] == value)
        nama = student_to_delete['NAMA']
        print(f'Anda akan menghapus data siswa dengan {x} = {value} atas nama = {nama}')
        if ask_again('Apakah Anda yakin ingin menghapus data ini? (ya/tidak): '):
            data[:] = [student for student in data if student[x] != value]
            for i, student in enumerate(data, start=1):
                student['KODE'] = i
            print(f'Data siswa atas nama = {nama} telah dihapus\n.')
            print_data(data)
            return
        else:
            print('Proses dibatalkan.')
            return
    else:
      print(f'Data siswa dengan {x} {value} tidak dapat ditemukan ')

# ------------------- 7 search
#searched student
def search_student(data):
    if not data:
      print('Tidak ada data siswa yang tersedia. \nAnda akan kembali ke menu utama secara otomatis')
      time.sleep(2)
      return

    while True:
      print('''
          ==========================
          |    Cari Data Siswa:    |
          ==========================
          1. Berdasarkan NIS
          2. Berdasarkan Nama Lengkap
          3. Berdasarkan Keyword
          4. Return
          ''')

      inputan = input_numerik('\nMasukkan pilihan anda: ')
      if input_cancel(inputan):
        break
      while True:
        if inputan == 1:
          print("*Untuk membatalkan proses, ketik 'batal'")
          nis = input('Masukkan NIS siswa: ').upper().strip()
          if input_cancel(nis):
            break
          if re.fullmatch(r"\bST202[1-4]0109\d{3}\b", nis):
            value = [student for student in data if student['NIS'] == nis]
            if value:
              print(f'Data siswa dengan NIS {nis} ditemukan:')
              print(tabulate(value, headers='keys', tablefmt='pretty'))
              break
            else:
              print(f'Tidak ada data siswa dengan NIS {nis}.')
          else: print('Input NIS tidak sesuai')
        elif inputan == 2:
          print("*Untuk membatalkan proses, ketik 'batal'")
          name = input_string('Masukkan nama lengkap siswa: ').title().strip()
          if input_cancel(name.lower()):
            break
          result = [value for value in data if value['NAMA'].replace(' ','').replace('.','').replace(',','').lower() == name.replace(' ','').replace('.','').replace(',','').lower()]
          if result:
            print(f'Data siswa dengan nama {name} ditemukan:')
            print(tabulate(result, headers='keys', tablefmt='pretty'))
            break
          else:
            print(f'Tidak ada data siswa dengan nama {name}.')
        elif inputan == 3:
            search_by('Masukkan kategori yang ingin dicari: ', database_student)
            break
        elif inputan == 4:
          break
        else:
          print('Pilihan yang dimasukkan tidak valid.')
      if not ask_again('\nApakah anda ingin mencari data kembali? '):
        return

def search_by(prompt, data):
  if not data:
    print('Fitur tidak dapat digunakan karena tidak ada data siswa yang tersedia. \nAnda akan kembali ke menu utama secara otomatis')
    time.sleep(4)
    return
  while True:
    while True:
      print("*Untuk membatalkan proses, ketik 'batal'")
      print('''
            ==========================
            |    Kategori keyword:   |
            ==========================
            1. NIS
            2. Nama
            3. Alamat
            4. Jenis Kelamin
            5. Return
      ''')
      acuan = input_numerik(prompt)
      if input_cancel(acuan):
        return
      if acuan in [1,2,3,4,5]:
          print("*Untuk membatalkan proses ketik 'batal'")
          keyword = input_string('Masukkan kata kunci: ').title().strip()
          if input_cancel(keyword):
            return
          if acuan == 1:
            x = 'NIS'
          elif acuan == 2:
            x = 'NAMA'
          elif acuan == 3:
            x = 'ALAMAT'
          elif acuan == 4:
            x = 'J KEL'
            if keyword.replace(' ','').replace('-','').lower() == 'lakilaki':
              keyword = 'Laki-laki'
            elif keyword.replace(' ','').replace('-','').lower() == 'perempuan':
              keyword = 'Perempuan'
          elif acuan == 5:
            return
          result = [value for value in data if keyword.lower() in value[x].lower()]
          if result:
              print(f'Data siswa dengan kata kunci {keyword} ditemukan:')
              print(tabulate(result, headers='keys', tablefmt='pretty'))
              return
          else:
              print(f'Tidak ada {x} siswa dengan kata kunci {keyword}')
              return
      else:
        print('Input tidak valid. Masukkan menu dengan benar')

################################# login as student

# validating user student
def valid_user_student():
    count = 0
    while True:
      print('\n')
      print("*Untuk kembali ke laman login ketik 'batal'")
      nis = input('Masukkan NIS anda: ').upper().strip()
      if input_cancel(nis):
          return nis, False

      if re.fullmatch(r"\bST202[1-4]0109\d{3}\b", nis):
          for student in database_student:
            if student['NIS'] == nis:
              return nis, True
          print('NIS tidak terdaftar. Pastikan NIS yang Anda masukkan benar.')
          count += 1
      else:
        print('Format NIS salah.\nPastikan format NIS yang anda masukkan benar')
        count += 1

      if count>= 2:
          if not ask_again('\nApakah anda masih ingin masuk kelaman ini? '):
              return nis, False

################################### student main menu
def student_main_menu(prompt,nis,data):
    print('Selamat datang, siswa!')
    while True:
        print('''\n
            =========================
            |    Menu Utama Siswa   |
            =========================
              1. Tampilkan data saya
              2. Help Desk
              3. Keluar\n''')

        input_smm = input_numerik(prompt)
        if input_smm == 1:
            read_student_data(nis, data)
        elif input_smm == 2:
            help_desk()
        elif input_smm == 3:
            return False
        else:
            print('Input tidak valid')

# ---------------- 1 read
#read data for student
def read_student_data(nis, data): # ini dr menu student buat baca student
    for student in data:
      if student['NIS'] == nis:
        print(tabulate([student], headers='keys', tablefmt='pretty'))
        break
      else:
        print('Data siswa tidak ditemukan.')
    while True:
      if ask_again('Ketik "ya" untuk kembali ke menu utama '):
       return

# ------------- 2 Help desk
def help_desk():
  print('''
              Help Desk

        1. Tata Usaha : op_team@khavidien.ac.id
        2. Akademik   : acamedic_op@khavidien.ac.id
        3. IT         : it_op@khavidien.ac.id
        ''')
  while True:
    if ask_again("ketik 'ya' untuk kembali ke menu utama "):
      return
    else:
      print('Input yang dimasukkan salah')

prog_start()
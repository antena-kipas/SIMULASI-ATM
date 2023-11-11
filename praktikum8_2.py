Database = {
    'akun1' : {
        'nama': "Luqman",
        'pin' : '123456',
        'saldo': 50000
    },
    'akun2': {
        'saldo': 5000000,
        'pin': '311005', 
        'nama':"hasan"
    },
    'akun3' : {
        'saldo': 5000000,
        'pin': '678910', 
        'nama':"fauzi"
    }
}

handler = ''
handler1 = ''
handler2 = ''
handler3 = ''


def tampilan_login():
    print('-'*30)
    print('\n\nsilahkan pilih menu anda')
    print('-'*24)
    print('a. Cek saldo')
    print('b. Pengambilan Dana')
    print('c. Ganti PIN')
    print('d.Keluar')


def cek_saldo(akun):
    if akun == 1:
        print('\n\n(menu saldo)')
        print('-'*12)
        print('\n\nnama: ', Database['akun1']['nama'])
        print('saldo anda :', Database['akun1']['saldo'])
    elif akun == 2:
        print('\n\n(menu saldo)')
        print('-'*12)
        print('\n\nnama: ', Database['akun2']['nama'])
        print('saldo anda : ',Database['akun2']['saldo'])
    elif akun == 3:
        print('\n\n(menu saldo)')
        print('-'*12)
        print('\n\nnama :', Database['akun3']['nama'])
        print('saldo anda : ',Database['akun3']['saldo'])


    print('\n\nmenu pilihan')
    print('-'*12)
    print('a. kembali ke menu sebelumnya')
    print('b. keluar')
    masukan_pilihan_saldo = input('\n\nSilahkan Masukan pilhian anda: ').lower()

    if masukan_pilihan_saldo == 'a':
        tampilan_login()
        menu(akun)
    elif masukan_pilihan_saldo == 'b':
        print('selamat anda telah berhasil keluar')
    else:
        print('pilihan anda tidak di dalam list pilihan')
        cek_saldo(akun)
        
def pengambilan_uang(akun):
    if akun == 1:
        print('\n\n(menu saldo)')
        print('-'*12)
        print('\n\nnama: ', Database['akun1']['nama'])
        print('saldo anda :', Database['akun1']['saldo'])
    elif akun == 2:
        print('\n\n(menu saldo)')
        print('-'*12)
        print('\n\nnama: ', Database['akun2']['nama'])
        print('saldo anda : ',Database['akun2']['saldo'])
    elif akun == 3:
        print('\n\n(menu saldo)')
        print('-'*12)
        print('\n\nnama :', Database['akun3']['nama'])
        print('saldo anda : ',Database['akun3']['saldo'])
    print('\n\na). ketik a untuk ke menu sebelumnya')
    print('b). ketik b untuk keluar')

    masukan_nilai = input('Masukan nilai yang anda ingin tarik: ').lower()
    if akun == 1 :
        
        if masukan_nilai == 'a':
            tampilan_login()
            menu(akun)
        elif masukan_nilai == 'b':
            print('selamat anda telah berhasil keluar')
        else:
            try:
                masukan_nilai = int(masukan_nilai)
                if masukan_nilai < Database['akun1']['saldo']:
                    saldo_sisa = Database['akun1']['saldo'] - masukan_nilai
                    Database['akun1']['saldo'] = saldo_sisa
                    print('penarikan telah berhasil')
                    print('-'*24)
                    print('\nsaldo anda tersisa: ', Database['akun1']['saldo'] )
                    print('anda telah keluar')
                elif masukan_nilai > Database['akun1']['saldo']:
                    print('Saldo anda tidak mencukupi')
                    pengambilan_uang(akun)
            except ValueError:
                    print("Format yang anda masukan salah\nmasukan format dengan benar!")
                    pengambilan_uang(akun)


    elif akun == 2 :
        if masukan_nilai == 'a':
            tampilan_login()
            menu(akun)
        elif masukan_nilai == 'b':
            print('selamat anda telah berhasil keluar')
        else:
            try: 
                masukan_nilai = int(masukan_nilai)
                if masukan_nilai < Database['akun2']['saldo']:
                    saldo_sisa = Database['akun2']['saldo'] - masukan_nilai
                    Database['akun2']['saldo'] = saldo_sisa
                    print('penarikan telah berhasil')
                    print('-'*24)
                    print('\nsaldo anda tersisa: ', Database['akun2']['saldo'] )
                    print('anda telah keluar')
                elif masukan_nilai > Database['akun2']['saldo']:
                    print('Saldo anda tidak mencukupi')
                    pengambilan_uang(akun)
            except ValueError:
                print('Format yang anda masukan salah\nmasukan format dengan benar!')
                pengambilan_uang(akun)
    
    elif akun == 3:
        if masukan_nilai == 'a':
            tampilan_login()
            menu(akun)
        elif masukan_nilai == 'b':
            print('selamat anda telah berhasil keluar')
        else:
            try: 
                masukan_nilai = int(masukan_nilai)
                if masukan_nilai < Database['akun3']['saldo']:
                    saldo_sisa = Database['akun3']['saldo'] - masukan_nilai
                    Database['akun3']['saldo'] = saldo_sisa
                    print('penarikan telah berhasil')
                    print('-'*24)
                    print('\nsaldo anda tersisa: ', Database['akun3']['saldo'] )
                    print('anda telah keluar')
                elif masukan_nilai > Database['akun3']['saldo']:
                    print('Saldo anda tidak mencukupi')
                    pengambilan_uang(akun)
            except ValueError:
                print('Format yang anda masukan salah\nmasukan format dengan benar!')
                pengambilan_uang(akun)

def ganti_pin(pengikat):
    if pengikat == 1: 
        

def login():
    masukan_nama = input('\n\nMasukan nama: ')
    masukan_pin = input('Masukan PIN: ')
    if masukan_pin == Database['akun1']['pin'] and masukan_nama == Database['akun1']['nama']:
        print('\n\nselamat anda berhasil login')
        print('halo',Database['akun1']['nama'])
        tampilan_login()
        handler1 = 1
        return handler1
    elif masukan_pin == Database['akun2']['pin'] and masukan_nama == Database['akun2']['nama']:
        print('\n\nselamat anda berhasil login')
        print('halo',Database['akun2']['nama'])
        tampilan_login()
        handler2 = 2
        return handler2
    elif masukan_pin == Database['akun3']['pin'] and masukan_nama ==  Database['akun3']['nama']:
        print('\n\nselamat anda berhasil login')
        print('halo',Database['akun3']['nama'])
        tampilan_login()
        handler3 = 3
        return handler3
        
    else:
        print('PIN ATAU USERNAME ANDA SALAH')
        print('ANDA TELAH KELUAR')
        



    

def menu(handling):
    masukan_pilihan = input('masukan pilihan anda: ').lower()
    if masukan_pilihan == 'a' :
        cek_saldo(handling)
    elif masukan_pilihan == 'b':
        pengambilan_uang(handling)
    elif masukan_pilihan == 'c':
        #ganti_pin(handling)
        print('c')
    elif masukan_pilihan == 'd':
        print('selamat anda berhasil keluar')
    else:
        print('pilihan anda tidak ada di dalam list')
        print('silahkan pilih dengan benar')
        tampilan_login()
        menu(handling)

def main():
    handler = login()
    
    if handler == True:
        menu(handler)

main()







    
        





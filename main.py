# -- encoding: utf-8 --
# CODED BY MARTIN SUDEVI
import os,sys
P = print
Oc = os.system
while True:
    P("")
    P("")
    c = input("A)dd, E)dit, D)elete, S)earch, L)ist, Q)uit: ")
    if c.lower() == 'q':
        break
    elif c.lower() == 'l':
        i = open('database.txt','r').read().splitlines()
        P(" ╔═════════════════════════════════════╗")
        P(" ╠════════════DAFTAR KONTAK ═══════════╣")
        P(" ╠══════════════════╦══════════════════╣")
        P(" ║      NAMA        ║       NOMOR      ║")
        P(" ╠══════════════════╬══════════════════╬")
        for l in i:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nomor : ','') = l1.strip().split('|')
                P((' ║ ')+(na[:15]).ljust(17,'.')+('║ ')+(no).ljust(17)+('║ '))
        P(" ╚══════════════════╩══════════════════╩═══════╩═══════╩═══════╩═══════╝")
    elif c.lower() == 's':
        cari = input(' Mencari : ')
        i = open('database.txt','r').read().splitlines()
        P(" ╔═════════════════════════════════════╗")
        P(" ╠════════════DAFTAR KONTAK ═══════════╣")
        P(" ╠══════════════════╦══════════════════╣")
        P(" ║      NAMA        ║       NOMOR      ║")
        P(" ╠══════════════════╬══════════════════╬")
        for l in i:
            if l == '':
                pass
            elif cari in l:
                l1 = l.replace('Nama : ','').replace('Nomor : ','') = l1.strip().split('|')
                P((' ║ ')+(na).ljust(17)+('║ ')+(no).ljust(17)+('║ '))
        P(" ╚══════════════════╩══════════════════╩═══════╩═══════╩═══════╩═══════╝")
    elif c.lower() == 'd':
        u = open('database.txt','r').read().splitlines()
        target = input(' Masukan Nama : ')
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nomor : ','') = l1.strip().split('|')
                if str(na) == str(target):
                    P('BERHASIL MENGHAPUS Data %s'%(target))
                    pass
                else:
                    nm.append(str(l)+'\n')
        new = open('database.txt','w')
        new.write(str(nm))
        new.close()
        new = open('database.txt','r').read().splitlines()
        new1 = open('database.txt','w')
        new1.close()
        new2 = open('database.txt','a')
        for i in new:
            i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n",'')
            new2.write(i2)
        new2.close()
    elif c.lower() == 'e':
        u = open('database.txt','r').read().splitlines()
        target = input(' Masukan Nama : ')
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nomor : ','')
                na,no = l1.strip().split('|')
                if na == target:
                    P(' Mengedit Data %s'%(target))
                    while (True):
                        nama = input(" Nama : ")
                        if nama == '':
                            P(' Masukan dengan Nama Dengan Benar')
                        else:
                            break
                    while (True):
                        try:
                            nomor  = int(input(" Nomor  : "))
                            if nomor == '':
                                P(' Masukan Nomor dengan Angka')
                        except ValueError:
                            P(' Masukan Nomor dengan Angka')
                        else:
                            break
                    akhir = round((float(nomor) * 0)
                    edit  =('Nama : '+nama+'|Nomor : '+str(nomor)+'\n')
                    nm.append(edit+'\n')
                else:
                    nm.append(str(l)+'\n')
        new = open('database.txt','w')
        new.write(str(nm))
        new.close()
        new = open('database.txt','r').read().splitlines()
        new1 = open('database.txt','w')
        new1.close()
        new2 = open('database.txt','a')
        for i in new:
            i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n","\n")
            new2.write(i2+'\n')
        new2.close()
    elif c.lower() == 'a':
        i = open('database.txt','a')
        P(" Tambah Kontak")
        while (True):
            nama = input(" Nama : ")
            if nama == '':
                P(' Masukan dengan Nama Dengan Benar')
            else:
                break
        while (True):
            try:
                nomor  = int(input(" NOMOR  : "))
                if nomor == '':
                    P(' Masukan Nomor dengan Angka')
            except ValueError:
                P(' Masukan Nomor dengan Angka')
            else:
                break
        akhir = round((float(nomor) * 0)
        i.write('\nNama : '+nama+'|Nomor : '+str(nomor)+'\n')
        i.close()
        Oc("clear")
    else:
        P("Pilih menu yang tersedia")

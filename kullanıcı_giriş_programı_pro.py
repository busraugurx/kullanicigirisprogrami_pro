print("****KULLANICI GİRİŞ PROGRAMI****")
sys_kullanıcı_adı="busraugur"
sys_parola="12345"
giriş_hakkı= 3

while True:
    kullanıcı_adı=input("KULLANICI ADINIZI GİRİNİZ: ")
    kullanıcı_parola=input("KULLANICI PAROLANIZI GİRİNİZ: ")
    if(sys_parola != kullanıcı_parola and sys_kullanıcı_adı==kullanıcı_adı):
        parola_hatırlatma = int(input("ŞİFRENİZİ UNUTTUYSANIZ 1'E BASIN: "))
        print("ŞİFRENİZE DAİR BİR İPUCU GELİYOR...")
        if(parola_hatırlatma == 1 ):
            print("PAROLANIZ 5 KARAKTERDEN OLUŞMAKTADIR VE 1 İLE BAŞLAMAKTADIR. HARF VEYA NOKTALAMA İŞARETİ İÇERMEMEKTEDİR...")
            giriş_hakkı+=1
            continue
    elif(kullanıcı_adı==sys_kullanıcı_adı and kullanıcı_parola!=sys_parola):
        print("PAROLAYI YANLIŞ GİRDİNİZ...")
        giriş_hakkı-=1
    elif(kullanıcı_adı!=sys_kullanıcı_adı and kullanıcı_parola!=sys_parola):
        print("KULLANICI ADINI VE PAROLAYI YANLIŞ GİRDİNİZ...")
        giriş_hakkı-=1
    elif(kullanıcı_adı != sys_kullanıcı_adı and kullanıcı_parola == sys_parola):
            print("KULLANICI ADINI HATALI GİRDİNİZ...")
    else:
        print("SİSTEME BAŞARILI BİR ŞEKİLDE GİRİŞ YAPILDI...")
        break
    if(giriş_hakkı==0):
        print("GİRİŞ HAKKINIZ BİTTİ...")
        break



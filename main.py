##1-masala
# s = input("Xarid summasini kiriting: ")

# if s.isdigit():
#     summa = int(s)

#     if summa < 50000:
#         print("Chegirma yo'q")
#     elif summa < 100000:
#         print("5% chegirma")
#     elif summa < 200000:
#         print("10% chegirma")
#     else:
#         print("15% chegirma")


##2-masala
# color = input("Svetoforning rangini kiriting (qizil, sariq, yashil): ")
# yol = input("Yo'l tirbandmi? (ha/yo'q): ")

# if color == "qizil":
#     print("To'xtang!")
# elif color == "sariq":
#     print("Tayyorlaning")
# elif color == "yashil" and yol == "yo'q":
#     print("Yuring")
# elif color == "yashil" and yol == "ha":
#     print("Kuting")


##3-masala
# vaqt = int(input("Vaqtni kiriting:"))

# if 6 >= {vaqt} <= 12:
#     print("Ertalabgi dori")
# elif 12 >= {vaqt} <= 18:
#     print("Kunduzgi dori")
# elif 18 > {vaqt} <=24:
#     print("Kechki dori")
# else:
#     print("Hozir dori ichish kerak emas!")


##4-masala
# temp = int(input("Hozirgi haroratni kiriting: "))

# if temp < 0:
#     print("Qalin palto, qo‘lqop kiying")
# elif temp < 15:
#     print("Jaket kiying")
# elif temp < 25:
#     print("Futbolka yetarli")
# else:
#     print("Yengil kiyim, soyabon oling")


##5-masala
# sinf = int(input("Sinfni kiritiing:"))
# sumka_vesi = int(input("Sumka o'g'irligini kiriting: "))

# if 1 < {sinf} <= 4 and {sumka_vesi} > 2:
#     print("Og'ir, kamaytiring!")
# elif 5 >= {sinf} < 9 and {sumka_vesi} > 4:
#     print("Og'ir, kamaytiring")
# else:
#     print("Norlam")


##6-masala
# yosh = input("Bemor yoshini kiriting: ")
# halot = input("Bemor holatini kiriting: (og'ir/oddiy): ")

# if yosh < 10 or yosh > 70:
#     print("Zudlik bilan!")
# elif halot == "og'ir":
#     print("1-soat ichida")
# else:
#     print("3-soat ichida")


##7-masala
# kun = input("Kun nomini kiriting (masalan: Dushanba, Seshanba.....): ").lower
# masofa = float(input("Masofani kiriting (km): "))

# ish_kuni = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma']
# dam_kuni = ['shanba', 'yakshanba']

# if kun == dam_kuni:
#     if masofa > 10:
#         print(f"Summa: {(3600 * masofa) * 0.9} Sizga masofa 10kmdan oshganligi sababli 10% chegirma beriladi.")
#     else:
#         print(f"Summa: {3600  * masofa} so'm.")
# elif kun == ish_kuni:
#     if masofa > 10:
#         print(f"Summa: {(3600 * masofa) * 0.9} Sizga masofa 10kmdan oshganligi sababli 10% chegirma beriladi.")
#     else:
#         print(f"Summa: {3000 * masofa} so'm.")
# else:
#     print("Qiymat xato kiritildi!")

##Copied, but not from AI


##8-masala
# rain = int(input("Yomg'ir yog'ish ehtimolini kiriting: "))
# temperature = int(input("Havo haroratini kiriting: "))

# if rain >= 70:
#     print("Uyda qoling")
# elif rain < 70 and temperature < 5:
#     print("Juda sovuq, sayr qilish tavsiya etilmaydi")
# else:
#     print("Ajoyib kun, sayrga boring!")

##O'zim yazganman!!!!!


##9-masala
# salary = int(input("Maoshni kiriting: "))
# cost = int(input("Xarajatlarni kiriting: "))
# if cost > salary:
#     print("Xavfli! Xarajatlarni kamaytiring")
# elif salary == cost:
#     print("Aynan yetarli")
# else:
#     print("Ajoyib! Tejamkorlik qilyapsiz")

##O'zim ishladim!!!


##10-masala
# velosiped = input('Velosiped turini kiriting ("shahar" yoki "sport"): ')
# vaqt = int(input("Ijaraga olingan vaqtni kiriting: "))

# city = ["shahar", "shaxar"]

# if  velosiped == city: ## yoki if velosiped in city:
#     print()

##.........



##11-masala
# olma_vesi = int(input("Olma vaznini kiriting: "))
# olma_korinishi = input("Olma ko'rinishini kiriting (yaxshi/yomon): ")

# if olma_korinishi == "yomon":
#     print("Past sifat")
# elif olma_vesi < 100:
#     print("Rad etiladi!")
# elif olma_vesi >= 200:
#     print("Premium")
# else:
#     print("Standart")


##O'zim yazdim kodi!!!


##12-masala
# summa = int(input("Xarid summasini kiriting: "))
# soat = int(input("Hozirgi soatni kiriting (0-23): "))

# if summa >= 100000 and 18 <= soat <= 22:
#     print("15% chegirma")
# elif summa >= 50000 and 10 <= soat < 18:
#     print("10% chegirma")
# else:
#     print("Chegirma yo'q")


##13-Masala
tur = input("Kitob turi (ilmiy/badiiy): ").lower()
kun = int(input("Kunlar soni: "))
narx = 2000 if tur == "ilmiy" else 1000
umumiy = narx * kun
if kun > 14:
    umumiy *= 0.7
elif kun > 7:
    umumiy *= 0.8
print(f"Yakuniy narx: {int(umumiy)} so'm")


##14-Masala
mashq = input("Mashq turi (kardio/og‘irlik): ").lower()
tajriba = int(input("Tajriba yili: "))
if mashq == "kardio" and tajriba < 1:
    print("20 daqiqa yengil")
elif mashq == "og‘irlik" and tajriba >= 2:
    print("60 daqiqa intensiv")
else:
    print("30 daqiqa o‘rtacha")


##15-Masala
dastur = input("Dastur nomi: ").lower()
soat = int(input("Hozirgi soat (0–23): "))
if dastur == "yangiliklar" and 18 <= soat <= 20:
    print("Tomosha qiling")
elif dastur == "serial" and 20 <= soat <= 22:
    print("Qayta ko‘ring")
else:
    print("Boshqa ko‘rsatuv tanlang")


##16-Masala
tur = input("Skuter turi (elektr/oddiy): ").lower()
masofa = float(input("Masofa (km): "))
narx = 2000 if tur == "elektr" else 1000
umumiy = narx * masofa
if masofa >= 10:
    umumiy *= 0.85
print(f"Yakuniy narx: {int(umumiy)} so'm")


##17-Masala
muammo = input("Muammo turi (dasturiy/uskunaviy): ").lower()
if muammo == "dasturiy":
    print("50 000 so'm")
else:
    qism = int(input("Qism narxi: "))
    if qism > 100000:
        print("150 000 so'm")
    else:
        print("80 000 so'm")


##18-Masala
iflos = int(input("Ifloslanish darajasi (%): "))
shamol = float(input("Shamol tezligi (km/soat): "))
if iflos > 50 and shamol < 5:
    print("Maska kiying")
elif iflos <= 50 and shamol >= 10:
    print("Sof havo")
else:
    print("Oddiy holat")


##19-Masala
tur = input("Kurs turi (akvarel/yog‘li): ").lower()
oy = int(input("Davomiylik (oy): "))
narx = 200000 if tur == "akvarel" else 300000
umumiy = narx * oy
if oy >= 3:
    umumiy *= 0.9
print(f"Yakuniy narx: {int(umumiy)} so'm")


##20-Masala
tur = input("Qulf turi (elektron/mexanik): ").lower()
yosh = int(input("Qulf yoshi (yil): "))
if tur == "elektron" and yosh < 2:
    print("Yuqori xavfsizlik")
elif tur == "mexanik" and yosh < 5:
    print("O‘rtacha xavfsizlik")
else:
    print("Past xavfsizlik")


##21-Masala
hudud = input("Hudud (shahar markazi/shahar cheti/boshqa): ").lower()
xonalar = int(input("Xonalar soni: "))
if hudud == "shahar markazi" and xonalar == 3:
    print("5 000 000 so'm")
elif hudud == "shahar cheti" and xonalar == 2:
    print("3 000 000 so'm")
else:
    print("2 000 000 so'm")


##22-Masala
quvvat = int(input("Quvvat (%): "))
masofa = float(input("Masofa (km): "))
if quvvat < 20 and masofa > 5:
    print("Zaryadlang")
elif quvvat < 50 and masofa < 3:
    print("Ehtiyot bo‘ling")
else:
    print("Yaxshi holat")


##23-Masala
ruxsat = int(input("Kamera ruxsati (MP): "))
yoruglik = input("Yorug‘lik darajasi (yaxshi/o‘rtacha/yomon): ").lower()
if ruxsat >= 12 and yoruglik == "yaxshi":
    print("Yuqori sifat")
elif 8 <= ruxsat < 12 and yoruglik == "o‘rtacha":
    print("O‘rtacha sifat")
else:
    print("Past sifat")


##24-Masala
masofa = float(input("Masofa (km): "))
obhavo = input("Ob-havo (yaxshi/o‘rtacha/yomon): ").lower()
if masofa < 5 and obhavo == "yaxshi":
    print("Piyoda")
elif masofa < 20 and obhavo == "o‘rtacha":
    print("Velosiped")
else:
    print("Avtobus")


##25-Masala
email = input("Email manzili: ")
if len(email) >= 10 and email.endswith("@gmail.com"):
    print("Qabul qilindi")
elif len(email) < 10 and email.endswith("@yahoo.com"):
    print("Qisqa email")
else:
    print("Noto‘g‘ri email")


##26-Masala
ovqat = input("Ovqat turi (salat/go‘sht): ").lower()
porsiya = int(input("Porsiya (g): "))
asosiy = (porsiya / 100) * (50 if ovqat == "salat" else 200)
if porsiya >= 300:
    asosiy *= 1.1
print(f"Yakuniy kaloriya: {int(asosiy)} kkal")


##27-Masala
summa = float(input("Kredit summasi (mln so‘m): "))
muddat = int(input("Muddat (yil): "))
if summa < 10 and muddat == 1:
    print("12%")
elif summa >= 10 and muddat == 2:
    print("10%")
else:
    print("15%")


##28-Masala
sinf = input("Sinf (biznes/ekonom): ").lower()
masofa = int(input("Masofa (km): "))
if sinf == "biznes" and masofa < 1000:
    asosiy = 1000000
elif sinf == "ekonom" and masofa < 1000:
    asosiy = 500000
else:
    asosiy = 1000000 if sinf == "biznes" else 500000
if masofa >= 1000:
    asosiy *= 1.2
print(f"Yakuniy narx: {int(asosiy)} so'm")


##29-Masala
tur = input("Mahsulot turi (lo‘shon/krem): ").lower()
oy = int(input("Ochilgandan o‘tgan oylar soni: "))
if tur == "lo‘shon" and oy >= 6:
    print("Ishlatish mumkin emas")
elif tur == "krem" and oy >= 12:
    print("Ishlatish mumkin emas")
else:
    print("Xavfsiz ishlatishingiz mumkin")


##30-Masala
tur = input("Kiyim turi (bolalar/kattalar): ").lower()
if tur == "bolalar":
    print("2 kun")
else:
    olcham = input("O‘lcham (S/M/L/XL): ").upper()
    if olcham in ["S", "M"]:
        print("4 kun")
    else:
        print("6 kun")


##31-Masala
qavat = int(input("Qavatlar soni: "))
meva = input("Meva (ha/yo‘q): ").lower()
shok = input("Shokolad (ha/yo‘q): ").lower()
narx = 100000 + (qavat - 1) * 50000
if meva == "ha":
    narx += 20000
if shok == "ha":
    narx += 30000
print(f"Yakuniy narx: {narx} so'm")


##32-Masala
maton = input("Maton turi (paxta/sintetik): ").lower()
iflos = input("Ifloslik darajasi (yengil/og‘ir): ").lower()
if maton == "paxta" and iflos == "yengil":
    print("Rejim 1")
elif maton == "sintetik" and iflos == "og‘ir":
    print("Rejim 3")
else:
    print("Rejim 2")


##33-Masala
nom = input("Kitob nomi: ").lower()
if "sir" in nom or "jinoyat" in nom:
    print("Detektiv")
elif "sevgi" in nom or "romantika" in nom:
    print("Romantik")
elif "kosmos" in nom or "kelajak" in nom:
    print("Fantastik")
else:
    print("Boshqa")


##34-Masala
tur = input("Chipta turi (VIP/oddiy): ").lower()
yosh = int(input("Yosh: "))
if tur == "vip" and yosh > 60:
    print("50 000 so'm")
elif tur == "oddiy" and yosh < 18:
    print("20 000 so'm")
else:
    print("30 000 so'm")


##35-Masala
kun = input("Kun nomi: ").lower()
soat = int(input("Soat (0–23): "))
ish_kunlari = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma"]
dam_kunlari = ["shanba", "yakshanba"]
if kun in ish_kunlari and 9 <= soat <= 18:
    print("Ochiq")
elif kun in dam_kunlari and 10 <= soat <= 16:
    print("Ochiq")
else:
    print("Yopiq")



##36-Masala
tur = input("Xizmat turi (soch olish/bo‘yash): ").lower()
soch_uzunligi = input("Soch uzunligi (qisqa/o‘rta/uzun): ").lower()
if tur == "soch olish":
    if soch_uzunligi == "qisqa":
        print("20 000 so'm")
    elif soch_uzunligi == "o‘rta":
        print("25 000 so'm")
    else:
        print("30 000 so'm")
elif tur == "bo‘yash":
    if soch_uzunligi == "qisqa":
        print("40 000 so'm")
    elif soch_uzunligi == "o‘rta":
        print("60 000 so'm")
    else:
        print("80 000 so'm")
else:
    print("Noto‘g‘ri xizmat turi")


##37-Masala
yil = int(input("Mashina yili: "))
yoqilgi = input("Yoqilg‘i turi (benzin/dizel/elektr): ").lower()
if yil >= 2020 and yoqilgi == "elektr":
    print("Ko‘rikdan o‘tgan")
elif yil < 2020 and yoqilgi == "benzin":
    print("Yengil ta’mir kerak")
else:
    print("To‘liq ko‘rikdan o‘tkazish kerak")


##38-Masala
tur = input("Ichimlik turi (suv/sharbat/qahva): ").lower()
hajm = int(input("Hajm (ml): "))
if tur == "suv":
    narx = hajm * 2
elif tur == "sharbat":
    narx = hajm * 3
else:
    narx = hajm * 4
if hajm >= 1000:
    narx *= 0.9
print(f"Yakuniy narx: {int(narx)} so'm")


##39-Masala
janr = input("Janr (fantastika/komediya/drama): ").lower()
yosh = int(input("Yosh: "))
if janr == "fantastika":
    narx = 40000
elif janr == "komediya":
    narx = 35000
else:
    narx = 30000
if yosh < 18:
    narx *= 0.8
elif yosh > 60:
    narx *= 0.7
print(f"Chipta narxi: {int(narx)} so'm")


##40-Masala
ball = int(input("Ball: "))
fan = input("Fan (matematika/fizika/ingliz tili): ").lower()
if ball >= 86:
    daraja = "A"
elif 71 <= ball < 86:
    daraja = "B"
elif 56 <= ball < 71:
    daraja = "C"
else:
    daraja = "F"
print(f"Natija: {daraja}")
if fan == "matematika" and daraja == "A":
    print("Mukofot beriladi")
elif fan == "fizika" and daraja in ["A", "B"]:
    print("Tabriklaymiz, o‘tdingiz")
else:
    print("Yana tayyorlaning")



# 41. 🧍‍♂️ BMI (tana massasi indeksi) hisoblash
vazn = float(input("Vazningiz (kg): "))
boy = float(input("Bo‘yingiz (m): "))
bmi = vazn / (boy ** 2)
print(f"BMI: {bmi:.1f}")
if bmi < 18.5:
    print("Ozgin")
elif 18.5 <= bmi < 25:
    print("Me’yorda")
elif 25 <= bmi < 30:
    print("Ortiqcha vazn")
else:
    print("Semizlik")


# 42. ⏰ Ish jadvali aniqlash
kun = input("Hafta kuni: ").lower()
soat = int(input("Soat (0–23): "))
ish_kunlari = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma"]
if kun in ish_kunlari and 9 <= soat < 18:
    print("Ish vaqti")
elif kun in ["shanba"] and 10 <= soat < 15:
    print("Qisqa ish kuni")
else:
    print("Dam olish")


# 43. 💰 Soliq hisoblash
daromad = float(input("Daromadingiz (so'm): "))
if daromad <= 1000000:
    soliq = daromad * 0.05
elif daromad <= 5000000:
    soliq = daromad * 0.1
else:
    soliq = daromad * 0.15
print(f"Soliq: {int(soliq)} so'm")


# 44. 🚴 Velosiped tezligi baholash
masofa = float(input("Masofa (km): "))
vaqt = float(input("Vaqt (soat): "))
tezlik = masofa / vaqt
print(f"O‘rtacha tezlik: {tezlik:.1f} km/soat")
if tezlik < 10:
    print("Sekin")
elif tezlik <= 20:
    print("O‘rtacha")
else:
    print("Tez")


# 45. 🎓 Talaba bahosi
ism = input("Ism: ")
ball = int(input("Ball (0–100): "))
if ball >= 90:
    baho = 5
elif ball >= 75:
    baho = 4
elif ball >= 60:
    baho = 3
else:
    baho = 2
print(f"{ism}ning bahosi: {baho}")


# 46. 📦 Yuk tashish narxi
vazn = float(input("Yuk og‘irligi (kg): "))
masofa = float(input("Masofa (km): "))
if vazn <= 5:
    narx = masofa * 1000
elif vazn <= 20:
    narx = masofa * 1500
else:
    narx = masofa * 2000
if masofa > 100:
    narx *= 0.9
print(f"Yakuniy narx: {int(narx)} so'm")


# 47. 🏖️ Dam olish turi tanlash
byudjet = int(input("Byudjet (so'm): "))
kunlar = int(input("Kunlar soni: "))
if byudjet >= 5000000 and kunlar >= 7:
    print("Chet el safari")
elif byudjet >= 2000000 and kunlar >= 3:
    print("Ichki turizm")
else:
    print("Uyda dam oling")


# 48. 🔋 Telefon zaryad tekshiruvi
zaryad = int(input("Zaryad (%): "))
if zaryad < 10:
    print("Zaryad past, tarmoqga ulang")
elif zaryad <= 80:
    print("Yaxshi holatda")
else:
    print("To‘liq zaryad")


# 49. 🎧 Musiqa janrini aniqlash
nom = input("Qo‘shiq nomi: ").lower()
if "love" in nom or "heart" in nom:
    print("Romantik janr")
elif "dance" in nom or "party" in nom:
    print("Raqs janr")
elif "sad" in nom or "cry" in nom:
    print("Lirik janr")
else:
    print("Boshqa janr")


# 50. 🕹️ O‘yin bosqichini aniqlash
ball = int(input("Toplagan ball: "))
if ball < 100:
    print("1-bosqich")
elif ball < 500:
    print("2-bosqich")
elif ball < 1000:
    print("3-bosqich")
else:
    print("Professional daraja")

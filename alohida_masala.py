jins = input("Jinsingizni kiriting (erkak yoki ayol):").lower()
yosh = input("Yoshingizni kiriting: ")

if jins == "erkak" or jins == "ayol" and 0 <= yosh <= 120:
    if jins == "erkak":
        n_y_e = int(yosh) - 60
        if yosh >= 60:
            print(f"Bobo - Siz nafaqa yoshidasiz")
            if n_y_e == 0:
                 print(f"Siz bu yil nafaqaga chiqdingiz!")
            else:
                 print(f"Siz {n_y_e} yildan beri nafaqadasiz")
        else:
            print("Hurmatli foydalanuvchi siz nafaqa yoshida emassiz")
    else:
        if yosh >= 55:
            n_y_a = int(yosh) - 55
            print(f"Buvi - Siz nafaqa yoshidasiz")
            if n_y_a == 0:
                 print(f"Siz bu yil nafaqaga chiqdingiz!")
            else:
                 print(f"Siz {n_y_a} yildan beri nafaqadasiz")
        else:
            print("Hurmatli foydalanuvchi siz nafaqa yoshida emassiz")
else:
    print("Ma’lumotlar noto’g’ri kiritildi")
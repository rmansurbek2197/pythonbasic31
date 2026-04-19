def unli_harflarni_ajratish(matn):
    unli_harflar = []
    for harf in matn:
        if harf.lower() in 'aeiou':
            unli_harflar.append(harf)
    return unli_harflar

def asosiy_funktsiya():
    matn = input("Matn kiriting: ")
    unli_harflar = unli_harflarni_ajratish(matn)
    print("Unli harflar: ", unli_harflar)
    takrorlash = input("Boshqa matn kiritsizmi? (ha/yo'q): ")
    if takrorlash.lower() == 'ha':
        asosiy_funktsiya()
    else:
        print("Dastur tugadi")

def boshlash():
    print("Unli harflarni ajratish dasturi")
    asosiy_funktsiya()

def dastur_haqida():
    print("Bu dastur foydalanuvchi kiritgan matndan faqat unli harflarni ajratib alohida ro'yxatga yig'adi")

def yordam():
    print("Dasturda quyidagi buyruqlar mavjud:")
    print("1. Matn kiriting")
    print("2. Unli harflarni ajratish")
    print("3. Boshqa matn kiritsizmi?")

def xato():
    print("Xato! Iltimos, to'g'ri buyruq kiriting")

def asosiy_menu():
    while True:
        print("1. Dasturni boshlash")
        print("2. Dastur haqida")
        print("3. Yordam")
        tanlov = input("Tanlovni kiriting: ")
        if tanlov == '1':
            boshlash()
        elif tanlov == '2':
            dastur_haqida()
        elif tanlov == '3':
            yordam()
        else:
            xato()

asosiy_menu()
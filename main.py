import write

import gen as generate

name, gender = generate.name()

phone_num = generate.phone_number()

date_ob = generate.date_of_birth()

card_num, card_brand, card_type, cvv_num, exp_date, bank = generate.card()

ss_num = generate.social_security()

info = f"""
Bilgiler Üretildi:

--- Kişi Bilgisi ---
İsim Soyisim: {name}
Cinsiyet: {gender}
Doğum Tarihi: {date_ob}
Telefon Numarası: {phone_num}
Sosyal Güvenlik Numarası: {ss_num}

--- Kart Bilgileri ---
Kart Numarası: {card_num}
Kart Markası: {card_brand}
Kart Tipi: {card_type}
Skt: {exp_date}
Cvv: {cvv_num}
Banka: {bank}
"""


print(info)

while True:

    choice = input("\nBunun Bir .txt Dosyasında Olmasını İster Misiniz (E/H)?")

    if choice.upper() == "E":

        write.gen_info(info)

        print("Dosya Başarıyla Kaydedildi!")

        break
    
    elif choice.upper() == "H":
        
        break
    
    else:
        print("\nGeçersiz Giriş!")
        
        continue

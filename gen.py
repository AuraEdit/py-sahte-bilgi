import names

from time import strftime as time

from random import randint as rand

from random import choice as choose

def name():

    genders = ["Erkek", "Kız"]

    gender = choose(genders)

    first_name = names.get_first_name(gender)

    last_name = names.get_last_name()
    
    name = f"{first_name}, {last_name}"

    return name, gender

def phone_number():

    phone_num = f"+{rand(0,300)} ({rand(1,9)}{rand(0,9)}{rand(0,9)}) {rand(1,9)}{rand(0,9)}{rand(0,9)} {rand(1,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)}"
    
    return phone_num

def date_of_birth():

    year = rand(1950,2010)

    month = rand(1,12)

    if month <= 9:
        month = "0" + str(month)

    else:
        pass

    day = rand(1,31)

    if day <= 9:
        day = "0" + str(day)

    else:
        pass
    
    return f"{month}/{day}/{year}"

def card():

    card_num = f"{rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)}"
    
    card_types = ["Debit", "Credit"]

    card_brand_type = ["Visa", "Mastercard", "Troy", "American Express"]

    banks = ["HalkBank", "VakıfBank", "ZiraatBank","AkBank", "AnadoluBank", "FibaBank", "ŞekerBank"]

    bank = choose(banks)

    experation_month = rand(1,12)

    if experation_month <= 9:
        experation_month = "0" + str(experation_month)

    else:
        pass

    experation_year = int(time('%Y')) + rand(1,10)

    experation_date = f"{experation_month}/{experation_year}"

    card_brand = choose(card_brand_type)

    card_type = choose(card_types)
    
    if card_brand == card_brand_type[0] or card_brand == card_brand_type[1]:
        cvv_num = f"{rand(0,9)}{rand(0,9)}{rand(0,9)}"

    elif card_brand == card_brand_type[2] or card_brand == card_brand_type[3]:
        cvv_num = f"{rand(0,9)}{rand(0,9)}{rand(0,9)}{rand(0,9)}"
    
    else:
        pass

    return card_num, card_brand, card_type, cvv_num, experation_date, bank

def social_security():


    ss_num = f"{rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)} {rand(0,9)}{rand(0,9)}{rand(0,9)}"
    
    return ss_num

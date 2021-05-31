def person():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    birth_year = input('Введите год рождения: ')
    city = input('Введите город проживания: ')
    mail = input('Введите адрес электронной почты: ')
    phone = input('Введите номер телефона: ')
    return (f"name - {name}, surname - {surname}, birth_year - {birth_year}, city - {city}, mail - {mail}, phone - {phone}")

info = person()
print(info)

#Done
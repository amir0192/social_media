from database.models import User
from datetime import datetime
from database import get_db

# регистрация пользователя
def register_user_db(name, email, phone_number, password, user_city):
    # генератор подключений где некст помогает сгенерировать, пишем в начале функциях во всех базах данных
    db = next(get_db())

    new_user = User(name=name, email=email, phone_number=phone_number,
                    password=password, user_city=user_city, reg_date=datetime.now())

# добавляем в базу
    db.add(new_user)
# сохраняем в базе
    db.commit()

    return new_user.id
# поверка на наличие в базе пользователя
def check_user_data_db(phone_number, email):
    db = next(get_db())

# Поверка данных на наличие записи в базе
    checker = db.query(User).filtr_by(phone_number=phone_number, email=email).first()
# если есть совпадения
    if checker:
        return False
# если нет совпадений
    return True

# поверка пароля пользователя при входе в аккаунт
def check_user_password_db(email, password):
    db = next(db())
# пробуем найти пользователя
    checker = db.query(User).filter_by(email=email).first()
# если нашел такой меил, проверяем правильность пароля
    if checker:
# начинаем сверку пароля
        if checker.password == password:
            return checker.id
        else:
            return 'неверный пароль'
# если не находит данные в базе
    return 'неверная почта'
# информация пользователя
def profile_info_db(user_id):
    db = next(get_db())
# находим пользователя через id
    exact_user = db.query(User).filtr_by(id=user_id).first()
# если нашел пользователя, передаю всю информацию про него
    if exact_user:
        return exact_user.email, \
            exact_user.phone_number, \
            exact_user.id, \
            exact_user.name, \
            exact_user.reg_date, \
            exact_user.user_city

    return 'пользователь не найден'
# изменения данных пользователя
def change_user_data(user_id, change_info, new_data):
    db = next(get_db)
# найти пользователя в базе
    exact_user = db.query(User).filter_by(id=user_id).first()
    if exact_user:
# поверка того, какую информацию хочет изменить пользователь
        if change_info == 'email':
            exact_user.email = new_data
        elif change_info == 'number':
            exact_user.phone_number = new_data
        elif change_info == 'name':
            exact_user.name = new_data
        elif change_info == 'city':
            exact_user.user_city = new_data
        elif change_info == 'password':
            exact_user.password = new_data
# сохраняем в базе данных
        db.commit()
        return 'данные успешно изменены'
# а если не находим в базе пользователя
    return 'не найден'
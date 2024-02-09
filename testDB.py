#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.model.user_business import UserBusiness
from somniiaMonitor.model.sleeper import Sleeper
from somniiaMonitor.model.user import User


def main_user():
    user = User()
    user.set_name("Matteo")
    user.set_surname("Ferreri")
    user.set_birth_date("1990-06-27")
    user.set_gender("M")
    user.set_tax_id("FRRMTT90H27E506Q")

    user_business: UserBusiness = UserBusiness.get_instance()
    response = user_business.save_user(user)
    print(f"After Save -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")
        user = response.get_object()

    old_name = user.get_name()
    new_name = "Pollo"

    user.set_name(new_name)
    response = user_business.update_user(user)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    user = user_business.get_user(user.get_tax_id())
    if user.get_name() == old_name:
        print(f"New Name : {user.get_name()}")

    response = user_business.delete_user(user)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    user = user_business.get_user(user.get_tax_id())
    if user is None:
        print("User does not exist")
    else:
        print(f"user: {user}")


def main_sleeper():
    sleeper = Sleeper()
    sleeper.set_name("Matteo")
    sleeper.set_surname("Ferreri")
    sleeper.set_birth_date("1990-06-27")
    sleeper.set_gender("M")
    sleeper.set_tax_id("FRRMTT90H27E506Q")

    user_business: UserBusiness = UserBusiness.get_instance()
    response = user_business.save_sleeper(sleeper)
    print(f"After Save -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")
        sleeper = response.get_object()

    old_name = sleeper.get_name()
    new_name = "Pollo"
    sleeper.set_name(new_name)
    response = user_business.update_sleeper(sleeper)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    sleeper = user_business.get_sleeper(sleeper.get_tax_id())
    if sleeper.get_name() == old_name:
        print(f"New Name : {sleeper.get_name()}")

    response = user_business.delete_sleeper(sleeper)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    sleeper = user_business.get_sleeper(sleeper.get_tax_id())
    if sleeper is None:
        print("User does not exist")
    else:
        print(f"user: {sleeper}")


def main_doctor():
    user = User()
    user.set_name("Matteo")
    user.set_surname("Ferreri")
    user.set_birth_date("1990-06-27")
    user.set_gender("M")
    user.set_tax_id("FRRMTT90H27E506Q")

    user_business: UserBusiness = UserBusiness.get_instance()
    response = user_business.save_user(user)
    print(f"After Save -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    old_name = user.get_name()
    new_name = "Pollo"

    user.set_name(new_name)
    response = user_business.update_user(user)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    user = user_business.get_user(user.get_tax_id())
    if user.get_name() == old_name:
        print(f"New Name : {user.get_name()}")

    response = user_business.delete_user(user)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    user = user_business.get_user(user.get_tax_id())
    if user is None:
        print("User does not exist")
    else:
        print(f"user: {user}")


if __name__ == "__main__":
    # main_user()
    main_sleeper()
    # main_doctor()

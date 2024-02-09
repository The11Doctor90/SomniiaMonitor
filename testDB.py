#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.model.user_business import UserBusiness
from somniiaMonitor.model.doctor import Doctor
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


def main_doctor():
    doctor = Doctor()
    doctor.set_name("Matteo")
    doctor.set_surname("Ferreri")
    doctor.set_birth_date("1990-06-27")
    doctor.set_gender("M")
    doctor.set_tax_id("FRRMTT90H27E506Q")
    doctor.set_register_code("prova")

    user_business: UserBusiness = UserBusiness.get_instance()
    response = user_business.save_doctor(doctor)
    print(f"After Save -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")
        doctor = user_business.get_doctor(doctor.get_tax_id())

    old_name = doctor.get_name()
    new_name = "Pollo"

    doctor.set_name(new_name)
    response = user_business.update_doctor(doctor)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    doctor = user_business.get_doctor(doctor.get_tax_id())
    if doctor.get_name() == old_name:
        print(f"New Name : {doctor.get_name()}")

    response = user_business.delete_user(doctor)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    doctor = user_business.get_user(doctor.get_tax_id())
    if doctor is None:
        print("User does not exist")
    else:
        print(f"user: {doctor}")


if __name__ == "__main__":
    # main_user()
    main_doctor()

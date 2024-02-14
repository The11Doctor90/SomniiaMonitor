#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.model.contact_business import ContactBusiness
from somniiaMonitor.business.model.user_business import UserBusiness
from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.doctor import Doctor
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
    if user.get_name() != old_name:
        print(f"New Name : {user.get_name()}")

    response = user_business.delete_user(user)
    print(f"After Remove -> result = {response.get_row_count()} message: {response.get_message()}")
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
    if sleeper.get_name() != old_name:
        print(f"New Name : {sleeper.get_name()}")

    response = user_business.delete_user(sleeper)
    print(f"After Remove -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    sleeper = user_business.get_sleeper(sleeper.get_tax_id())
    if sleeper is None:
        print("User does not exist")
    else:
        print(f"user: {sleeper}")


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
        doctor = response.get_object()

    # print(doctor.to_string())
    # old_name = doctor.get_name()
    # new_name = "Pollo"
    #
    # doctor.set_name(new_name)
    # response = user_business.update_doctor(doctor)
    # print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    # if response.get_row_count() > 0:
    #     print(f"User Saved: {response.get_object()}")
    #
    # doctor = user_business.get_doctor(doctor.get_tax_id())
    # if doctor.get_name() == old_name:
    #     print(f"New Name : {doctor.get_name()}")
    #
    # response = user_business.delete_user(doctor)
    # print(f"After Remove -> result = {response.get_row_count()} message: {response.get_message()}")
    # if response.get_row_count() > 0:
    #     print(f"User Saved: {response.get_object()}")
    #
    # doctor = user_business.get_user(doctor.get_tax_id())
    # if doctor is None:
    #     print("User does not exist")
    # else:
    #     print(f"user: {doctor}")


def main_address():
    doctor = Doctor()
    doctor.set_name("Matteo")
    doctor.set_surname("Ferreri")
    doctor.set_birth_date("1990-06-27")
    doctor.set_gender("M")
    doctor.set_tax_id("FRRMTT90H27E506Q")
    doctor.set_register_code("prova")
    doctor.set_password("pass")

    contact = Contact()
    contact.set_address("Via pinco Pala")
    contact.set_email("mf@g.it")
    contact.set_phone("3202950")
    contact.set_number("5")
    contact.set_city("Lecce")
    contact.set_province("LE")
    contact.set_zip_code("73100")
    contact.set_country("Italy")

    user_business: UserBusiness = UserBusiness.get_instance()
    response = user_business.save_doctor(doctor)
    if response.get_row_count() > 0:
        doctor = response.get_object()

    contact.set_user_id(doctor.get_user_id())
    contact_business: ContactBusiness = ContactBusiness.get_instance()
    response = contact_business.save_contact(contact)
    if response.get_row_count() > 0:
        contact = response.get_object()

    doctor.set_contact_id(contact.get_contact_id())
    response = user_business.update_doctor(doctor)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    doctor = user_business.get_doctor(doctor.get_tax_id())
    print(f"New Name : {doctor.get_contact_id()}")

    response = user_business.delete_user(doctor)
    print(f"After Remove -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    doctor = user_business.get_user(doctor.get_tax_id())
    if doctor is None:
        print("User does not exist")
    else:
        print(f"user: {doctor}")


def saveDoctor():
    doctor = Doctor()
    doctor.set_name("Fady")
    doctor.set_surname("Mena")
    doctor.set_birth_date("1997-05-24")
    doctor.set_gender("M")
    doctor.set_tax_id("codice fiscale fady")
    doctor.set_register_code("prova")
    doctor.set_password("pass")

    contact = Contact()
    contact.set_address("Via pinco Pala")
    contact.set_email("mf@g.it")
    contact.set_phone("3202950")
    contact.set_number("5")
    contact.set_city("Lecce")
    contact.set_province("LE")
    contact.set_zip_code("73100")
    contact.set_country("Italy")

    user_business: UserBusiness = UserBusiness.get_instance()
    response = user_business.save_doctor(doctor)
    if response.get_row_count() > 0:
        doctor = response.get_object()

    contact.set_user_id(doctor.get_user_id())
    contact_business: ContactBusiness = ContactBusiness.get_instance()
    response = contact_business.save_contact(contact)
    if response.get_row_count() > 0:
        contact = response.get_object()

    doctor.set_contact_id(contact.get_contact_id())
    response = user_business.update_doctor(doctor)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    doctor = user_business.get_doctor(doctor.get_tax_id())
    print(f"New Name : {doctor.get_contact_id()}")

    # response = user_business.delete_user(doctor)
    # print(f"After Remove -> result = {response.get_row_count()} message: {response.get_message()}")
    # if response.get_row_count() > 0:
    #     print(f"User Saved: {response.get_object()}")
    #
    # doctor = user_business.get_user(doctor.get_tax_id())
    # if doctor is None:
    #     print("User does not exist")
    # else:
    #     print(f"user: {doctor}")


def saveSle():
    sleeper = Sleeper()
    sleeper.set_name("Matteo")
    sleeper.set_surname("Ferreri")
    sleeper.set_birth_date("1990-06-27")
    sleeper.set_gender("M")
    sleeper.set_tax_id("FRRMTT90H27E506Q")
    sleeper.set_password("passsa")

    contact = Contact()
    contact.set_address("Via pinco Pala")
    contact.set_email("gino@")
    contact.set_phone("3202950")
    contact.set_number("5")
    contact.set_city("Lecce")
    contact.set_province("LE")
    contact.set_zip_code("73100")
    contact.set_country("Italy")

    user_business: UserBusiness = UserBusiness.get_instance()
    response = user_business.save_sleeper(sleeper)
    if response.get_row_count() > 0:
        sleeper = response.get_object()

    contact.set_user_id(sleeper.get_user_id())
    contact_business: ContactBusiness = ContactBusiness.get_instance()
    response = contact_business.save_contact(contact)
    if response.get_row_count() > 0:
        contact = response.get_object()

    sleeper.set_contact_id(contact.get_contact_id())
    response = user_business.update_sleeper(sleeper)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    sleeper = user_business.get_sleeper(sleeper.get_tax_id())
    print(f"New Name : {sleeper.get_contact_id()}")

    # response = user_business.delete_user(sleeper)
    # print(f"After Remove -> result = {response.get_row_count()} message: {response.get_message()}")
    # if response.get_row_count() > 0:
    #     print(f"User Saved: {response.get_object()}")
    #
    # sleeper = user_business.get_user(sleeper.get_tax_id())
    # if sleeper is None:
    #     print("User does not exist")
    # else:
    #     print(f"user: {sleeper}")


if __name__ == "__main__":
    # main_user()
    # main_sleeper()
    # main_doctor()
    # main_address()
    saveDoctor()
    saveSle()

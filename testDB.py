#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.dao.user_dao import UserDAO
from somniiaMonitor.dao.user_dao_impl import UserDAOImpl
from somniiaMonitor.model.user import User


def main():
    user = User()
    user.set_name("Matteo")
    user.set_surname("Ferreri")
    user.set_birth_date("1990-06-27")
    user.set_gender("M")
    user.set_tax_id("FRRMTT90H27E506Q")

    user_dao: UserDAO = UserDAOImpl().get_instance()
    row_count = user_dao.add_user(user)
    print(f"add: {row_count}")
    row_count = user_dao.find_all_users()
    print(f"find: {len(row_count)}")
    print(f"users: {row_count}")
    user.set_name("Pollo")
    row_count = user_dao.update_user(user)
    print(f"update: {row_count}")
    user.set_name("")
    print(f"name_1 (vuoto): {user.get_name()}")
    user = user_dao.find_user_by_tax_id("FRRMTT90H27E506Q")
    print(f"name_2: {user.get_name()}")
    row_count = user_dao.delete_user(user)
    print(f"delete: {row_count}")
    user = user_dao.find_user_by_tax_id("FRRMTT90H27E506Q")
    if user is None:
        print("User does not exist")
    else:
        print(f"user: {user}")


if __name__ == "__main__":
    main()


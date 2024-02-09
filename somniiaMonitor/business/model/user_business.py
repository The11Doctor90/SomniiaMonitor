#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.doctor_dao import DoctorDAO
from somniiaMonitor.dao.doctor_dao_impl import DoctorDAOImpl
from somniiaMonitor.dao.user_dao import UserDAO
from somniiaMonitor.dao.user_dao_impl import UserDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.doctor import Doctor
from somniiaMonitor.model.user import User


class UserBusiness:
    __instance = None

    def __init__(self):
        if UserBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            UserBusiness.__instance = self

    @staticmethod
    def get_instance():
        if UserBusiness.__instance is None:
            UserBusiness()
        return UserBusiness.__instance

    @staticmethod
    def get_user(tax_id: str) -> User:
        user_dao: UserDAO = UserDAOImpl.get_instance()
        user: User = user_dao.find_user_by_tax_id(tax_id)
        return user

    @staticmethod
    def get_doctor(tax_id: str) -> Doctor:
        doctor_dao: DoctorDAO = DoctorDAOImpl.get_instance()
        doctor: Doctor = doctor_dao.find_doctor_by_tax_id(tax_id)
        return doctor

    @staticmethod
    def user_exist(tax_id: str) -> bool:
        user_dao: UserDAO = UserDAOImpl.get_instance()
        return user_dao.user_exist(tax_id)

    def save_user(self, user: User) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        if user.has_empty_field():
            response.set_message("signin_empty_error")
            return response

        if self.user_exist(user.get_tax_id()):
            response.set_message(f"signin_exist_error \n {user.get_tax_id()}")
            return response

        user_dao: UserDAO = UserDAOImpl.get_instance()
        result = user_dao.add_user(user)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        user = user_dao.find_user_by_tax_id(user.get_tax_id())
        response.set_object(user)
        response.set_row_count(result)
        return response


    def save_doctor(self, doctor: Doctor) -> ActionResponse:
        response = self.save_user(doctor)
        if response.get_row_count() == 0:
            return response
        user: User = response.get_object()
        doctor.set_user_id(user.get_user_id())
        doctor_dao: DoctorDAO = DoctorDAOImpl.get_instance()
        if doctor.get_supervisor_id() is None:
            result = doctor_dao.add_doctor(doctor)
        else:
            result = doctor_dao.add_doctor_with_supervisor(doctor)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        doctor = doctor_dao.find_doctor_by_tax_id(doctor.get_doctor_id())
        response.set_object(doctor)
        response.set_row_count(result)
        return response

    @staticmethod
    def update_user(user: User) -> ActionResponse:
        user_dao: UserDAO = UserDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = user_dao.update_user(user)

        if result == 0:
            response.set_message("update_failure")
            return response

        response.set_message("signin_successful")
        user = user_dao.find_user_by_tax_id(user.get_tax_id())
        response.set_object(user)
        response.set_row_count(result)
        return response

    def update_doctor(self, doctor: Doctor) -> ActionResponse:
        doctor_dao: DoctorDAO = DoctorDAOImpl.get_instance()
        old_doctor = doctor_dao.find_doctor_by_tax_id(doctor.get_tax_id())
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = 0
        if self.doctor_have_same_data(doctor, old_doctor):
            response.set_message("update error: No change detected")
            response.set_row_count(result)
            return response

        response = self.update_user(doctor)
        result = response.get_row_count()
        if result == 0:
            response.set_message("update_failure")
            return response

        response.set_message("signin_successful")
        doctor = doctor_dao.find_doctor_by_tax_id(doctor.get_tax_id())
        response.set_object(doctor)
        response.set_row_count(result)
        return response

    @staticmethod
    def delete_user(user: User):
        user_dao: UserDAO = UserDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = user_dao.delete_user(user)
        if result == 0:
            response.set_message("remove_failure this_user")
            return response

        response.set_message("remove_successful")
        response.set_row_count(result)
        return response

    @staticmethod
    def users_have_same_data(user: User, other_user: User) -> bool:
        return (user.get_user_id() == other_user.get_user_id() and
                user.get_name() == other_user.get_name() and
                user.get_surname() == other_user.get_surname() and
                user.get_tax_id() == other_user.get_tax_id() and
                user.get_birth_date() == other_user.get_birth_date() and
                user.get_gender() == other_user.get_gender())

    def doctor_have_same_data(self, doctor: Doctor, other_doctor: Doctor) -> bool:
        return (self.users_have_same_data(doctor, other_doctor) and
                doctor.get_register_code() == other_doctor.get_register_code() and
                doctor.get_supervisor_id() == other_doctor.get_supervisor_id())




"""

    
public boolean userCan(User user, UserPrivilege privilege){
        IUserDAO userDAO = (IUserDAO) dao.getDAO(DAO.DAOList.USER);
        if (UserPrivilege.MANAGE_SHOP.equals(privilege)){
            return userDAO.managerExist(user);
        }
        if (UserPrivilege.ADMIN_SYSTEM.equals(privilege)){
            return userDAO.administratorExist(user);
        }
        return false;
    }
    
public ActionResponse update(User user){
        //1. memorizza i vecchi dati dell'utente
        User oldUser = getUser(user.getCode());

        ActionResponse response = new ActionResponse();
        response.setMessage(LANGUAGE.readLang("undefined_error"));

        CommandManager commandManager = new CommandManager();
        int result = 0;

        //2. controlla se i nuovi dati sull'identità dell'utente siano uguali ai precedenti
        //   se sono diversi allora aggiorna l'identità dell'utente
        if (user.getIdentity().compareTo(oldUser.getIdentity()) != 0) {
            result = commandManager.update(dao.getDAO(DAO.DAOList.IDENTITY), user.getIdentity(), oldUser.getIdentity());
            if (result == 0){
                commandManager.undoAll();
                response.setMessage(LANGUAGE.readLang("update_failure"));
                return response;
            }
        } else {
            result = 1;
        }

        //3. controlla se i nuovi dati sull'indirizzo dell'utente siano uguali ai precedenti;
        //   se sono diversi allora aggiorna l'indirizzo dell'utente
        if (user.getResidence().compareTo(oldUser.getResidence()) != 0) {
            result = commandManager.update(dao.getDAO(DAO.DAOList.RESIDENCE), user.getResidence(), oldUser.getResidence());
            if (result == 0){
                commandManager.undoAll();
                response.setMessage(LANGUAGE.readLang("update_failure"));
                return response;
            }
        } else {
            result = 1;
        }

        //4. controlla se lo status dell'utente è uguale al precedente;
        //   se sono diversi allora aggiorna lo storeCode
        if (!user.getStatus().equals(oldUser.getStatus())) {
            result = commandManager.update(dao.getDAO(DAO.DAOList.STATUS), user, oldUser);
            if (result == 0) {
                commandManager.undoAll();
                response.setMessage(LANGUAGE.readLang("update_failure"));
                return response;
            }
        } else {
        result = 1;
        }

        //5. controlla se il punto vendita di registrazione è uguale al precedente;
        //   se sono diversi allora aggiorna lo storeCode
        if (user.getStoreCode() == oldUser.getStoreCode()) {
            if (user.getStoreCode() != oldUser.getStoreCode()) {
                result = commandManager.update(dao.getDAO(DAO.DAOList.CUSTOMER), user, oldUser);
                if (result == 0){
                    commandManager.undoAll();
                    response.setMessage(LANGUAGE.readLang("update_failure"));
                    return response;
                }

                //6. controlla se l'utente aveva delle prenotazioni nel punto vendita precedente;
                //   se le aveva cambia il punto vendita di ricezione
                List<Reservation> reservations = ReservationBusiness.getInstance().getAll(user.getCode());
                if (!reservations.isEmpty()){
                    for (Reservation r : reservations){
                        r.setStoreCode(user.getStoreCode());
                        response = ReservationBusiness.getInstance().update(r);
                        commandManager.addCommand(response.getCommandManager());
                        result = response.getRowCount();
                        if (result == 0){
                            commandManager.undoAll();
                            response.setMessage(LANGUAGE.readLang("remove_failure"));
                            return response;
                        }
                    }
                }
            }
        } else {
            result = 1;
        }

        //7. l'aggiornamento è riuscito
        response.setCommandManager(commandManager);
        response.setMessage(LANGUAGE.readLang("update_successful"));
        response.setRowCount(result);
        return response;
        

public ActionResponse remove(User user){
    ActionResponse response = new ActionResponse();
    response.setMessage(LANGUAGE.readLang("undefined_error"));

    CommandManager commandManager = new CommandManager();
    int result;
    //1. se l'utente ha delle prenotazioni rimuovile
    response = ReservationBusiness.getInstance().removeAll(user.getCode());
    commandManager.addCommand(response.getCommandManager());
    result = response.getRowCount();
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure"));
        return response;
    }

    //2. se l'utente ha definito delle liste d'acquisto rimuovile
    response = WishlistBusiness.getInstance().removeAll(user.getCode());
    commandManager.addCommand(response.getCommandManager());
    result = response.getRowCount();
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure"));
        return response;
    }

    //3. se l'utente lasciato dei feedback rimuovili
    response = FeedbackBusiness.getInstance().removeAll(user.getCode());
    commandManager.addCommand(response.getCommandManager());
    result = response.getRowCount();
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure"));
        return response;
    }

    //4. se l'utente ha fatto acquisti rimuovili
    response = PurchaseBusiness.getInstance().removeAll(user.getCode());
    commandManager.addCommand(response.getCommandManager());
    result = response.getRowCount();
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure"));
        return response;
    }

    //5. rimuovi status e data di registrazione dell'utente
    result = commandManager.delete(dao.getDAO(DAO.DAOList.STATUS), user);
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure") + LANGUAGE.readLang("this_user"));
        return response;
    }

    //6. rimuovi l'utente dai clienti
    result = commandManager.delete(dao.getDAO(DAO.DAOList.CUSTOMER), user);
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure") + LANGUAGE.readLang("this_user"));
        return response;
    }

    //7. rimuovi l'indirizzo dell'utente
    result = commandManager.delete(dao.getDAO(DAO.DAOList.RESIDENCE), user.getResidence());
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure") + LANGUAGE.readLang("this_user"));
        return response;
    }

    //8. rimuovi la password
    result = commandManager.delete(dao.getDAO(DAO.DAOList.PASSWORD), ((IPasswordDAO) dao.getDAO(DAO.DAOList.PASSWORD)).findByEmail(user.getIdentity().getEmail()));
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure") + LANGUAGE.readLang("this_user"));
        return response;
    }

    //9. se l'utente è un manager rimuovi l'utente dai managar
    if (userCan(user, UserPrivilege.MANAGE_SHOP)){
        //1. Rimuovi tutti i commenti ai feedback
        response = FeedbackBusiness.getInstance().removeAllAnswer(user.getCode());
        commandManager.addCommand(response.getCommandManager());

        //2. rimuovi il manager
        result = commandManager.delete(dao.getDAO(DAO.DAOList.MANAGER), user);
        if (result == 0){
            commandManager.undoAll();
            response.setMessage(LANGUAGE.readLang("remove_failure") + LANGUAGE.readLang("this_manager"));
            return response;
        }
    }

    //10. rimuovi l'identità dell'utente
    result = commandManager.delete(dao.getDAO(DAO.DAOList.IDENTITY), user.getIdentity());
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure") + LANGUAGE.readLang("this_user"));
        return response;
    }

    //11. rimuovi l'utente
    result = commandManager.delete(dao.getDAO(DAO.DAOList.USER), user);
    if (result == 0){
        commandManager.undoAll();
        response.setMessage(LANGUAGE.readLang("remove_failure") + LANGUAGE.readLang("this_user"));
        return response;
    }

    //12. rimozione terminata
    response.setCommandManager(commandManager);
    response.setMessage(LANGUAGE.readLang("remove_successful"));
    response.setRowCount(result);
    return response;
}        

    
public User getUser(int userCode){
        IUserDAO userDAO = (IUserDAO) dao.getDAO(DAO.DAOList.USER);
        IIdentityDAO identityDAO = (IIdentityDAO) dao.getDAO(DAO.DAOList.IDENTITY);
        IResidenceDAO residenceDAO = (IResidenceDAO) dao.getDAO(DAO.DAOList.RESIDENCE);
        IStatusDAO statusDAO = (IStatusDAO) dao.getDAO(DAO.DAOList.STATUS);

        User user = userDAO.findByCode(userCode);
        if (user == null){
            return null;
        }
        user.setIdentity(identityDAO.findById(userCode));
        user.setResidence(residenceDAO.findByCode(userCode));
        user.setSeniority(statusDAO.findSeniority(userCode));
        user.setStatus(UserStatus.valueOf(statusDAO.findMood(userCode)));

        if (!userCan(user, UserPrivilege.ADMIN_SYSTEM)) {
            ICustomerDAO customerDAO = (ICustomerDAO) dao.getDAO(DAO.DAOList.CUSTOMER);
            user.setStoreCode(customerDAO.findByCode(userCode));
        }

        return user;
    }
"""

import json
from datetime import datetime
import random

DB_PATH = "db/users.json"

def read_user(email:str = None):
    with open(DB_PATH, "r") as file:
        users = json.load(file) #read all content in the data_base.
        if email is not None:
            user_search = list(filter(lambda user:user["email"] == email, users)) #Search for user
            user = user_search[0] if user_search != [] else {} #verify if user is found
            return user

        return users


def read_beneficiary(acNo:int = None):
    with open(DB_PATH, "r") as file:
        users = json.load(file) #read all content in the data_base.
        if acNo is not None:
            user_search = list(filter(lambda user:user["account_number"] == acNo, users)) #Search for user
            user = user_search[0] if user_search != [] else {} #verify if user is found
            return user

        return users

def create_user(fname, lname, email, mobile_number, password, pin):
    users = read_user()
    user = read_user(email)
    if user == {}:
        user_dict = {
            "email" : email,
            "mobile_number" : mobile_number,
            "password" : password,
            "account_name" : fname + " " + lname,
            "account_number" : random.randint(1111111111,9999999999),
            "account_balance" : 0,
            "transact_pin" : pin,
            "created at" : str(datetime.now()),
            "is active" : "False"
        }
        users.append(user_dict) #add to dictionary

        with open(DB_PATH, "w") as file:
            json.dump(users, file)
            return True
    return False


def login(email, password):
    users = read_user()
    user = read_user(email)
    if user == {}:
        return False
    else:
        if user["password"] == password:
            users.remove(user)
            user["is active"] = "True"
            users.append(user)
            with open(DB_PATH, "w") as file:
                json.dump(users, file)
            return True

def logout(email):
    users = read_user()
    user = read_user(email)
    if user["is active"] == "True":
        users.remove(user)
        user["is active"] = "False"
        users.append(user)
        with open(DB_PATH, "w") as file:
            json.dump(users, file)
        return True
    else:
        return False



def depositNow(email, amount, pin):
    users = read_user()
    user = read_user(email)
    if user["transact_pin"] == pin:
        users.remove(user)
        user["account_balance"] =  user["account_balance"] + amount
        users.append(user) #add to users

        with open(DB_PATH, "w") as file:
            json.dump(users, file)
        return True
    return False


def withdrawNow(email, amount, pin):
    users = read_user()
    user = read_user(email)
    if user["transact_pin"] == pin:
        if user["account_balance"] - amount < 0:
            return False
        else:
            users.remove(user)
            user["account_balance"] = user["account_balance"] - amount
            users.append(user) #add to users

            with open(DB_PATH, "w") as file:
                json.dump(users, file)
            return True
    return False


def transferNow(email, acNo, amount, pin):
    users = read_user()
    user = read_user(email)
    if user["transact_pin"] == pin:
        users.remove(user)
        user["account_balance"] = user["account_balance"] - amount
        users.append(user)
        
        with open(DB_PATH, "w") as file:
            json.dump(users, file)
        
        
        userss = read_beneficiary()
        userr = read_beneficiary(acNo)
        userss.remove(userr)
        userr["account_balance"] =  userr["account_balance"] + amount
        userss.append(userr) #add to users

        with open(DB_PATH, "w") as file:
            json.dump(userss, file)

        return True

    return False



# def reset_pass(pin, pass1):
    
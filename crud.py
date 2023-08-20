from bson import ObjectId
import json

def format(db_object):
    # remove the _id field from the object
    db_object.pop('_id', None)
    return json.dumps(db_object)


def add_user( db, user: dict):
    try:
        db.users.insert_one( user)
    except:
        print( "Failed to add user")
        raise Exception( "Failed to add user")
    
    return True

def get_user( db, user_id: str):
    try:
        user = db.users.find_one( { "_id": user_id })
    except:
        print( "Failed to get user")
        raise Exception( "Failed to get user")
    
    return user

def get_user_by_username(db, username: str):
    try:
        user = db.users.find_one( { "username": username })
    except:
        print( "Failed to get user")
        raise Exception( "Failed to get user")
    
    return user

def get_all_users( db):
    try:
        users = db.users.find()
    except:
        print( "Failed to get users")
        raise Exception( "Failed to get users")
    
    return users

def update_user( db, user_id: str, user: dict):
    try:
        db.users.update_one( { "_id": user_id }, { "$set": user })
    except:
        print( "Failed to update user")
        raise Exception( "Failed to update user")
    
    return True

def update_user_by_username( db, username: str, user: dict):
    try:
        db.users.update_one( { "username": username }, { "$set": user })
    except:
        print( "Failed to update user")
        raise Exception( "Failed to update user")
    
    return True

def delete_user( db, user_id: str):
    try:
        db.users.delete_one( { "_id": user_id })
    except:
        print( "Failed to delete user")
        raise Exception( "Failed to delete user")
    
    return True

def get_fashion(db, object_id: int):

    object_id = int(object_id)

    try:
        fashion = db.fashion.find_one( { 'id': object_id })
    except:
        print( "Failed to get fashion")
        raise Exception( "Failed to get fashion")
    
    return format(fashion)

def get_multiple_fashion(db, user_ids: list):
    try:
        fashion = db.fashion.find( { "id": { "$in": user_ids }})
    except:
        print( "Failed to get fashion")
        raise Exception( "Failed to get fashion")
    
    f_list = []

    for doc in fashion:

        f_list.append( format(doc) )
    
    return f_list

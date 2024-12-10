from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re ### Regular expresion
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions
from flask_app.models import user

DB = 'thoughts_schema'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') #### Regular expresion for jus letters
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') #######regular expresion just for numbers

class Thought:
    
    def __init__( self , data ):
        self.id = data['id']
        self.thought = data['thought']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.user_id = data['user_id']
        self.validationx = 'No'
        self.owner_user = ''
        self.users = []
        self.likes_counter = 0
    
    @classmethod
    def get_thought_with_likes(cls,data):
        query = "select * from thoughts left join users on  thoughts.user_id=users.id;"
        results= connectToMySQL(DB).query_db(query,data)
        all_thoughts = []
        counter = 0
        for row_from_db in results:
            thought = (cls(row_from_db))
            users_data ={
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": "NA",
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
                }
            thought.owner_user=user.User(users_data)
            data['thought_id'] = thought.id
            query = "select * from thoughts left join likes on thoughts.id=likes.thought_id left join users on likes.user_id=users.id where thoughts.id=%(thought_id)s"
            results= connectToMySQL(DB).query_db(query,data)
            for row_from_db2 in results:
                users_data ={
                    "id": row_from_db["users.id"],
                    "first_name": row_from_db["first_name"],
                    "last_name": row_from_db["last_name"],
                    "email": row_from_db["email"],
                    "password": "NA",
                    "created_at": row_from_db["users.created_at"],
                    "updated_at": row_from_db["users.updated_at"]
                    }
                if row_from_db2["users.id"] is None:
                    pass
                elif row_from_db2["users.id"]==data['id']:
                    thought.validationx = "Yes"
                    thought.users.append(user.User(users_data))
                else:
                    thought.users.append(user.User(users_data))
            thought.likes_counter = len(thought.users)
            all_thoughts.append(thought)
            print(all_thoughts)
        return all_thoughts


    @classmethod
    def save(cls,data):
        query = "INSERT INTO thoughts (thought, updated_at, created_at, user_id) VALUES (%(new_thought)s,now(),now(), %(user_id)s);"
        connectToMySQL(DB).query_db( query, data )

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if len(data['new_thought']) <5:
            flash("The name of the recipe should have at least 5 characters")
            is_valid= False
        if data['new_thought'] =="Post a thought here":
            flash("Please type a thought")
            is_valid= False
        if data['new_thought'] =='':
            flash("Please type a thought")
            is_valid= False
        return is_valid    

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM likes WHERE thought_id = %(id)s;"
        connectToMySQL(DB).query_db(query,data)
        query = "DELETE FROM thoughts WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def destroy_like(cls,data):
        query = "DELETE FROM likes WHERE thought_id = %(thought_id)s and user_id= %(user_id)s;"
        connectToMySQL(DB).query_db(query,data)

    @classmethod
    def user_like(cls,data):
        query = "select count(*) as count from likes where user_id=%(user_id)s and thought_id=%(thought_id)s;"
        validator = connectToMySQL(DB).query_db( query, data )
        if validator[0]['count']==0:
            query = "INSERT INTO likes (user_id,thought_id) VALUES (%(user_id)s,%(thought_id)s);"
            return connectToMySQL(DB).query_db( query, data )
        else:
            return False

    @classmethod
    def counter_likes(cls,data):
        query = "select count(*) as counter from thoughts join likes on likes.thought_id=thoughts.id  where thoughts.id=%(thought_id)s;"
        return connectToMySQL(DB).query_db( query, data )
    




"""This module defines tests for the user class and its methods"""
import unittest
from app.users.models import User 
from app.database import Database
import json
from app import create_app,app_config
from flask_restful import Resource

class Test_Questions(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        database= Database() 
        database.databaseconnections()
        database.create_tables()
        self.client = self.app.test_client
        

    def tearDown(self):
        """
        Method to droP tables after the test is run
        """
        
        database= Database()
        database.databaseconnections()
        database.delete_test_tables()

    def register_user(self, username="naome", email="naome@test.com", password="password"):
        """This helper method helps register a test user."""
        user_data = {
            'username':username,
            'email': email,
            'password': password
        }
        return self.client().post('/api/v1/auth/signup', data=user_data)

    

    def login_user(self, email="naome@test.com", password="password"):
        """This helper method helps log in a test user."""
        user_data = {
            'email': email,
            'password': password
        }
        return self.client().post('/api/v1/auth/login', data=user_data)

    def test_register_valid_details(self):
        """ Tests creating a new user with valid details """
        test_user = {
            'username': 'naome',
            'email': 'naome@gmail.com',
            'password': 'naome'
        }
        response = self.client().post('/api/v1/auth/signup',
                                    data=json.dumps(test_user),
                                    content_type='application/json')
        self.assertIn('You registered successfully. Please login.',
                      str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_register_existing_user(self):
        """ Tests creating a user with existing email """
        self.register_user()
        response = self.register_user()
        self.assertEqual(response.status_code, 409)
        self.assertIn("The user already exists", str(response.data))


    def test_registration_with_empty_user_name(self):
        """ Test for empty username validation """
        

        response = self.client().post(
            "/api/v1/auth/signup",
            content_type='application/json',
            data=json.dumps(dict(username=" ", email="naome@email.com", password="naome"),)
        )
        reply = json.loads(response.data)
        self.assertEquals(reply.get("message"), "username  feild is required")
        self.assertEquals(response.status_code, 400)
    

    def test_user_login_successful(self):
        """ Test for successful login """
        response2 = self.client().post("/api/v1/auth/signup",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="naome", email="naome@email.com", password="naome"),)
                                 )

        response = self.client().post(
            "/api/v1/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="naome", password="naome"))
        )
        reply = json.loads(response.data)

        self.assertEquals(response.status_code, 200)

    def test_registration_with_wrong_username_format(self):
        """ Test for empty contact validation """

        response = self.client().post(
            "/api/auth/signup",
            content_type='application/json',
            data=json.dumps(dict(username="@@@@@", email="naome@email.com", password="naome"),)
        )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "wrong username format entered, Please try again")
        self.assertEquals(response.status_code, 400)

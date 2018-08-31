"""This module defines tests for the user class and its methods"""
import unittest
from app.users.models import User 
from .test_data import Database
import json
from app import create_app,app_config
from flask_restful import Resource

class Test_Questions(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client
        

    def register_user(self, username="naome", email="naome@test.com", password="password"):
        """This helper method helps register a test user."""
        user_data = {
            'username':username,
            'email': email,
            'password': password
        }
        return self.client().post('/api/v1/auth/register', data=user_data)

    def login_user(self, email="naome@test.com", password="password"):
        """This helper method helps log in a test user."""
        user_data = {
            'email': email,
            'password': password
        }
        return self.client().post('/api/v1/auth/login', data=user_data)

    def test_registration_with_empty_user_name(self):
        """ Test for empty username validation """
        

        response = self.client().post(
            "/api/v1/auth/register",
            content_type='application/json',
            data=json.dumps(dict(username=" ", email="naome@email.com", password="naome"),)
        )
        reply = json.loads(response.data)
        self.assertEquals(reply.get("message"), "username  feild is required")
        self.assertEquals(response.status_code, 400)
    

    def test_user_login_successful(self):
        """ Test for successful login """
        response2 = self.client().post("/api/v1/auth/register",
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
            "/api/auth/register",
            content_type='application/json',
            data=json.dumps(dict(username="@@@@@", email="naome@email.com", password="naome"),)
        )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "wrong username format entered, Please try again")
        self.assertEquals(response.status_code, 400)

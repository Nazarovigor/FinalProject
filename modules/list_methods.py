import requests
from faker import Faker
import os
import ast
from dotenv import load_dotenv

load_dotenv()
fake = Faker()


headers = ast.literal_eval(os.getenv("headers"))
base_url = os.getenv('base_url')

body = {"name": fake.name()}


def create_folder():
    body1 = {"name": fake.name()}
    return requests.post(base_url + "space/90154821595/folder", json=body1, headers=headers), body1

def get_folders():

    return requests.get(base_url + "space/90154821595/folder", headers=headers)

def get_folder(id):

    return  requests.get(base_url + "folder/" + str(id), headers=headers)

def delete_folder(id):

    return requests.delete(base_url + "folder/" + str(id), headers=headers)


def update_folder(id, body):

    return requests.put(base_url + "folder/" + str(id), json=body, headers=headers)
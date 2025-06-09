from faker import Faker
fake = Faker()
from modules.list_methods import create_folder, get_folder, delete_folder, get_folders, update_folder


def test_get_folder():
    response = create_folder()
    my_name = response[0].json()['name']
    my_id = response[0].json()['id']

    get_response = get_folder(my_id)
    assert get_response.json()['name'] == my_name

    delete_folder(my_id)


def test_get_folders():
    response = create_folder()
    my_id1 = response[0].json()['id']

    response = create_folder()
    my_id2 = response[0].json()['id']


    result = get_folders()
    assert result.json()['folders'][0]['id'] == my_id1 and result.json()['folders'][1]['id'] == my_id2

    delete_folder(my_id1)
    delete_folder(my_id2)


def test_create_folder():
    response, body1 = create_folder()
    assert response.json()['name'] == body1['name']

    my_id = response.json()['id']
    delete_folder(my_id)


def test_update_folder():
    body_upd = {"name": fake.name()}

    response = create_folder()
    my_id = response[0].json()['id']
    my_name = response[0].json()['name']

    get_response = update_folder(my_id, body_upd)
    updated_name = get_response.json()['name']
    assert updated_name != my_name

    delete_folder(my_id)


def test_delete_folder():
    response = create_folder()
    my_id = response[0].json()['id']
    del_response = delete_folder(my_id)
    assert del_response.status_code == 200

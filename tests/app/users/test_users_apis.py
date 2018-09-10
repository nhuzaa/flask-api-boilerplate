import json
from app.users.services import UsersService

users_service = UsersService()


def test_get_users(client, dummy_user):
    response = client.get("/users/")

    assert response.status_code == 200
    assert len(json.loads(response.data)) == 1


def test_get_user(client, dummy_user):
    response = client.get("/users/" + str(dummy_user.id))

    assert response.status_code == 200


def test_get_user_when_nonexistent(client):
    response = client.get("/users/" + str(11))

    assert response.status_code == 404


def test_post_user_with_valid_data(client, dummy_user_data):
    response = client.post("/users/", data=json.dumps(dummy_user_data))

    assert response.status_code == 201

    user = users_service.first()
    assert user.first_name == dummy_user_data["first_name"]


def test_post_user_with_missing_data(client, dummy_user_data):
    dummy_user_data["first_name"] = None
    response = client.post("/users/", data=json.dumps(dummy_user_data))

    assert response.status_code == 422

    user = users_service.first()
    assert user is None


def test_post_user_with_invalid_password(client, dummy_user_data):
    dummy_user_data["password"] = "small"
    response = client.post("/users/", data=json.dumps(dummy_user_data))

    assert response.status_code == 422

    user = users_service.first()
    assert user is None


def test_put_user_with_valid_data(client, dummy_user, dummy_user_data):
    dummy_user_data["first_name"] = "Sudir"
    response = client.put(
        "/users/" + str(dummy_user.id), data=json.dumps(dummy_user_data)
    )

    assert response.status_code == 200

    user = users_service.first()
    assert user.first_name == "Sudir"


def test_put_user_with_missing_data(client, dummy_user, dummy_user_data):
    dummy_user_data["first_name"] = None
    response = client.put(
        "/users/" + str(dummy_user.id), data=json.dumps(dummy_user_data)
    )

    assert response.status_code == 422

    user = users_service.first()
    assert user.first_name == dummy_user.first_name


def test_put_user_with_new_password(client, dummy_user, dummy_user_data):
    dummy_user_data["password"] = "newpassword"
    response = client.put(
        "/users/" + str(dummy_user.id), data=json.dumps(dummy_user_data)
    )

    assert response.status_code == 200

    user = users_service.first()
    # Password should remain unchanged
    assert user.password == dummy_user.password


def test_delete_user_when_existing(client, dummy_user):
    response = client.delete("/users/" + str(dummy_user.id))

    assert response.status_code == 200

    user = users_service.first()
    assert user is None


def test_delete_user_when_non_existing(client, dummy_user):
    response = client.delete("/users/" + str(100))

    assert response.status_code == 404

    user = users_service.first()
    assert user.id == dummy_user.id

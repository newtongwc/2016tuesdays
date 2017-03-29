from __future__ import absolute_import
from users import Users
from user_collection import UserCollection

import pytest


def test_empty_collection():
    collection = UserCollection()
    users = collection.add_user()
    assert len(users) == 0

def test_add_user():
    a = Users("tall, dark, handsome", "SemiAudramatic", "it'sasecret")
    UserCollection.add_user(a)
    assert len(UserCollection) == 1
    assert a in UserCollection

    a_copy = Users("tall, dark, handsome", "SemiAudramatic", "it'sasecret")
    assert a_copy in UserCollection

    b = Users("short, fluffy, kitten-like", "AntidoteForTheAwkward", "alsoasecret")
    UserCollection.add_user(b)
    assert len(UserCollection) == 2
    assert b in UserCollection

    UserCollection.add_user(a_copy)
    assert len(UserCollection) == 2

pytest.main()

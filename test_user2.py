import pytest 
from application.models import User
@pytest.fixture(scope='module') 
def new_user(): 
    user = User('sam123@gmail.com', 'skyisblue') 
    return user
def test_new_user(new_user): 
    assert new_user.email == 'sam123@gmail.com' 
    assert new_user.hashed_password != 'skyisblue' 
    assert not new_user.authenticated 
    assert new_user.role == 'user'
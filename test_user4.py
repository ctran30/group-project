import pytest 
from application.models import User
@pytest.fixture(scope='module') 
def new_user(): 
    user = User('luan3456@gmail.com', 'treeisgreen') 
    return user
def test_new_user(new_user): 
    assert new_user.email == 'luan3456@gmail.com' 
    assert new_user.hashed_password != 'treeisgreen' 
    assert not new_user.authenticated 
    assert new_user.role == 'user'
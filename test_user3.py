import pytest 
from application.models import User
@pytest.fixture(scope='module') 
def new_user(): 
    user = User('victor3598@gmail.com', 'riceiswhite') 
    return user
def test_new_user(new_user): 
    assert new_user.email == 'victor3598@gmail.com' 
    assert new_user.hashed_password != 'riceiswhite' 
    assert not new_user.authenticated 
    assert new_user.role == 'user'
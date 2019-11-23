import pytest
from unittest.mock import Mock

from domain.models.User import User
from domain.service.UserService import UserService, UserSchema

class Test_RepositoryTeste:
    
    #region repository

    def test_user_service_get_all_empty(self):
        repository = Mock()
        repository.get_all.return_value = []
        user_service = UserService(repository=repository)

        users = user_service.get_all()
        assert len(users) == 0

    def test_user_service_get_all_some_values(self):
        repository = Mock()
        repository.get_all.return_value = [User(username='batata', password="batata"), User(username='batatinha', password="batatinha")]
        user_service = UserService(repository=repository)

        users = user_service.get_all()
        assert len(users) == 2

    def test_user_service_get_by_id_incorrect(self):
        repository = Mock()
        repository.get_by_id.return_value = None
        user_service = UserService(repository=repository)

        user = user_service.get_by_id("5ffd3bf47dca2c51a33b5fe0")
        assert user is None

    def test_user_service_authenticate(self):
        repository = Mock()
        repository.get_all.return_value = [User(username='batata', password="batata"), User(username='batatinha', password="batatinha")]
        user_authenticated = UserService.authenticate("batata", "batata", repository=repository)
        assert user_authenticated.username == 'batata'
    
    def test_user_service_not_authenticate(self):
        repository = Mock()
        repository.get_all.return_value = []
        user_authenticated = UserService.authenticate("batata", "batata", repository=repository)
        assert user_authenticated is None
    
    def test_user_service_not_authenticate(self):
        repository = Mock()
        repository.get_all.return_value = []
        user_authenticated = UserService.authenticate("batata", "batata", repository=repository)
        assert user_authenticated is None
   
    
 #endregion


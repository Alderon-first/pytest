# инициализатор фикстуры
import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(password="secret", username="admin")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

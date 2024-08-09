import pytest

from homework.transport import Car, MeansOfTransport, Moped


@pytest.fixture(scope='function')
def generate_means_of_transport(request):
    request.cls.transport = MeansOfTransport(color='green', brand='BMW')



@pytest.fixture(scope='function')
def generate_car(request):
    request.cls.car = Car(color='green', brand='BMW', wheels_count=4, places_count=5, year=1998)
    request.cls.car2 = Car(color='red', brand='VAZ', wheels_count=4, places_count=5, year=1986)


@pytest.fixture(scope='function')
def generate_moped(request):
    request.cls.moped = Moped(color='green', brand='BMW', wheels_count=4)
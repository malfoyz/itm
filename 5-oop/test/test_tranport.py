import pytest


from homework.transport import MeansOfTransport, Car, Moped


@pytest.mark.usefixtures('generate_means_of_transport')
class TestMeansOfTransport:
    def test_object_creating(self):
        assert self.transport.color == 'green'
        assert self.transport.brand == 'BMW'

    def test_color_setter(self):
        self.transport.color = 'red'
        assert self.transport.color == 'red'

    def test_brand_setter(self):
        self.transport.brand = 'VAZ'
        assert self.transport.brand == 'VAZ'

    def test_show_brand_method(self):
        assert self.transport.show_brand() == 'BMW'


@pytest.mark.usefixtures('generate_car')
class TestCar:
    def test_object_creating(self):
        new_car = Car(color='green', brand='BMW', wheels_count=4, places_count=5, year=1998)
        assert new_car.color == 'green'
        assert new_car.brand == 'BMW'
        assert new_car.min_speed == 0.0
        assert new_car.max_speed == 240
        assert new_car.step == 10.0
        assert new_car.values == [1, 2, 3, 4, 5]
        assert new_car.car_drive == 4

    def test_class_attributes(self):
        assert self.car.car_drive == 4

    def test_get_drive_classmethod(self):
        assert Car.get_drive() == 4
        assert self.car.get_drive() == 4

    def test_call_method(self):
        assert self.car(1990) == 1990

    def test_getattribute_method_with_value_error(self):
        with pytest.raises(ValueError):
            self.car.year

    def test_setattr_method_with_correct_attribute(self):
        self.car.new_attr = 10
        assert self.car.new_attr == 10

    def test_setattr_method_with_attribute_error(self):
        with pytest.raises(AttributeError):
            self.car.human = 'Max'

    def test_len_method(self):
        assert len(self.car) == 1998

    def test_bool_method(self):
        assert abs(self.car) == 40

    def test_comprassion_operations(self):
        assert not self.car < self.car2
        assert not self.car > self.car2
        assert self.car <= self.car2
        assert self.car >= self.car2

    def test_getitem_method_with_correct_index(self):
        assert self.car[0] == 1
        assert self.car[4] == 5

    def test_getitem_method_with_uncorrect_index(self):
        with pytest.raises(IndexError):
            self.car[6]

    def test_str_method(self):
        assert str(self.car) == 'BMW'

    def test_setitem_method_with_correct_index(self):
        self.car[5] = 6
        self.car2[7] = 8
        assert self.car.values == [1, 2, 3, 4, 5, 6]
        assert self.car2.values == [1, 2, 3, 4, 5, None, None, 8]

    def test_setitem_method_with_uncorrect_index(self):
        with pytest.raises(TypeError):
            self.car[-2] = -2

    def test_delitem_method_with_correct_index(self):
        del self.car[4]
        assert self.car.values == [1, 2, 3, 4]

    def test_delitem_method_with_uncorrect_index(self):
        with pytest.raises(TypeError):
            del self.car[2.2]

    def test_iterator_in_for(self):
        expected_values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90,
                          100, 110, 120, 130, 140, 150, 160, 170,
                          180, 190, 200, 210, 220, 230, 240]
        iterator_values = []
        for speed in self.car:
            iterator_values.append(speed)
        assert expected_values == [int(x) for x in iterator_values]

    def test_iterator_stop_iteration(self):
        iterator = iter(self.car)
        for _ in range(25):
            next(iterator)
        with pytest.raises(StopIteration):
            next(iterator)

    def test_inheritance(self):
        assert isinstance(self.car, MeansOfTransport)
        assert self.car.show_brand() == 'BMW'


@pytest.mark.usefixtures('generate_moped')
class TestMoped:
    def test_object_creating(self):
        new_moped = Moped(color='green', brand='BMW', wheels_count=4)
        assert new_moped.color == 'green'
        assert new_moped.brand == 'BMW'

    def test_get_time_with_correct_data(self):
        assert self.moped.get_time(200, 20) == 10

    @pytest.mark.parametrize('distance,max_speed',
                             [('asa', 21),
                              (123.3, 'asa'),
                              ('asfa', False)])
    def test_get_time_with_uncorrect_data(self, distance, max_speed):
        with pytest.raises(TypeError):
            self.moped.get_time(distance, max_speed)

    def test_inheritance(self):
        assert isinstance(self.moped, MeansOfTransport)
        assert self.moped.show_brand() == 'BMW'
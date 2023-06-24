from datetime import datetime, timedelta
from parking_machine_import import ParkingMachine
import pytest


@pytest.fixture
def machine():
    return ParkingMachine()


def test_add_car(machine):
    license_plate = "ABC123"
    machine.add_car(license_plate)
    assert machine.license_plate == license_plate


def test_search_car_exists(machine):
    license_plate = "ABC123"
    machine.add_car(license_plate)
    assert machine.search_car(license_plate) is True


def test_search_car_not_exists(machine):
    assert machine.search_car("XYZ789") is False


def test_car_out(machine):
    machine.car_in = datetime.now()
    machine.car_out()
    assert machine.car_outs is not None


def test_time(machine):
    minutes = 60
    car_in = datetime.now()
    car_out = car_in + timedelta(minutes=minutes)
    machine.car_in = car_in
    machine.car_outs = car_out
    assert machine.time() == minutes


def test_search_car_in(machine):
    car_in = datetime.now()
    machine.car_in = car_in
    expected_time = car_in.strftime("%Y-%m-%d %H:%M:%S")
    assert machine.search_car_in() == expected_time


def test_search_car_out(machine):
    car_out = datetime.now()
    machine.car_outs = car_out
    expected_time = car_out.strftime("%Y-%m-%d %H:%M:%S")
    assert machine.search_car_out() == expected_time


def test_seach_car_pay(machine):
    machine.car_in = datetime(2023, 6, 3, 12, 0)
    machine.car_outs = machine.car_in + timedelta(minutes=90)
    assert (
        machine.seach_car_pay() == 30
    )  # Adjust expected value as per your calculation logic

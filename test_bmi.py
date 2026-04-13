import pytest
from bmi import calculate_bmi, get_category

def test_bmi_normal():
    assert calculate_bmi(1.75, 70) == 22.9

def test_bmi_underweight():
    assert calculate_bmi(1.75, 50) == 16.3

def test_bmi_overweight():
    assert calculate_bmi(1.75, 85) == 27.8

def test_bmi_obese():
    assert calculate_bmi(1.75, 100) == 32.7

def test_category_underweight():
    assert get_category(17.0) == "Underweight"

def test_category_normal():
    assert get_category(22.0) == "Normal weight"

def test_category_overweight():
    assert get_category(27.0) == "Overweight"

def test_category_obese():
    assert get_category(35.0) == "Obese"

def test_bmi_boundary_normal():
    assert get_category(18.5) == "Normal weight"

def test_bmi_boundary_overweight():
    assert get_category(25.0) == "Overweight"

def test_bmi_boundary_obese():
    assert get_category(30.0) == "Obese"
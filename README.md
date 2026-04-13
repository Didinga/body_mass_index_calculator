# BMI Calculator

A simple command-line BMI (Body Mass Index) calculator written in Python.

## Features

- Calculates BMI from height and weight
- Classifies result into a category (Underweight, Normal weight, Overweight, Obese)
- Input validation with retry loop — handles non-numeric and negative values

## Usage

```bash
python bmi.py
```
Enter your height in metres:
1.75
Enter your weight in kilograms:
70
Your BMI is: 22.9 (Normal weight)

## BMI Categories

| BMI | Category |
|---|---|
| < 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight |
| ≥ 30.0 | Obese |

## Project Structure
bmi-calculator/
├── bmi.py
└── test_bmi.py

## Running Tests

```bash
pip install pytest
pytest test_bmi.py -v
```

## Requirements

- Python 3.x
- pytest (for tests only)

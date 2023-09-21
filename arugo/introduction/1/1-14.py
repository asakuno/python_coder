person_info = [
    {"name": "aruru", "height": 1.7, "weight": 70.0},
    {"name": "iruru", "height": 1.6, "weight": 65.0},
    {"name": "ururu", "height": 1.8, "weight": 70.0},
    {"name": "eruru", "height": 1.5, "weight": 40.0}
]

for d in person_info:
    bmi = d["weight"] / d["height"]**2
    d["BMI"] = round(bmi, 1)

print(person_info)
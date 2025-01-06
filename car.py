# слвник toyota C-HR Hybrid
auto = {
    "model": "Toyota C-HR Hybrid",
    "price": "1,062,758 грн",
    "engine": "1.8 L",
    "weight": "1,745 kg",
    "speed": "170 km/h",
    "interior": [
        "Upholstery seats",
        "Heated front seats",
        "Dual-zone climate",
        "Touchscreen system"
    ],
    "trunk": {
        "volume": "377 L",
        "folded_volume": "1,160 L"
    }
}

# вага прицепа
auto["trailer_weight"] = "750 kg"

# експорт
model = auto["model"]
price = auto["price"]
first_interior = auto["interior"][0]
folded_trunk = auto["trunk"]["folded_volume"]

# результат
print(f"Model: {model}")
print(f"Price: {price}")
print(f"First interior feature: {first_interior}")
print(f"Trunk volume with folded seats: {folded_trunk}")

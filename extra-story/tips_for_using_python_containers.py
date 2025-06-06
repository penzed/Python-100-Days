person = {
    'name': 234,
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': 234,
    'tel': 13122334455,
    'emergence contact': 13800998877
}

print(max(person.values()))

print(max(person, key=person.get))

print(max(person.items(), key=lambda x: x[1]))

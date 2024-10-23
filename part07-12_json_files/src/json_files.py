# Write your solution here

import json

def print_persons(filename: str):
    with open(filename) as f:
        data = f.read()

    people = json.loads(data)

    for el in people:
        name = el["name"]
        age = el["age"]
        hobbies = ", ".join(el["hobbies"])
        print(f"{name} {age} years ({hobbies})")


if __name__=="__main__":
    print_persons("file3.json")
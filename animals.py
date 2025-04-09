animals = [
    {
        "name": "Dog",
        "group": "mammals",
        "number_of_legs": 4,
        "skills": ["running", "swimming"]
    },
    {
        "name": "Eagle",
        "group": "birds",
        "number_of_legs": 2,
        "skills": ["flying", "hunting"]
    },
    {
        "name": "Shark",
        "group": "fish",
        "number_of_legs": 0,
        "skills": ["swimming", "sensing blood"]
    },
    {
        "name": "Frog",
        "group": "amphibians",
        "number_of_legs": 4,
        "skills": ["jumping", "swimming"]
    },
    {
        "name": "Snake",
        "group": "reptiles",
        "number_of_legs": 0,
        "skills": ["slithering", "camouflage"]
    }
]

class Animal:
    def __init__(self, name: str, group: str, number_of_legs: int, skills: list):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Group: {self.group}")
        print(f"Number of Legs: {self.number_of_legs}")
        print(f"Skills: {', '.join(self.skills)}")
        print("-" * 20)

dog = Animal("Dog", "mammals", 4, ["running", "swimming"])
eagle = Animal("Eagle", "birds", 2, ["flying", "hunting"])
shark = Animal("Shark", "fish", 0, ["swimming", "sensing blood"])
frog = Animal("Frog", "amphibians", 4, ["jumping", "swimming"])
snake = Animal("Snake", "reptiles", 0, ["slithering", "camouflage"])

animals = [dog, eagle, shark, frog, snake]
for animal in animals:
    animal.display_info()

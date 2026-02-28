class Person:
    def __init__(self, name,age, handedness="right-handed"):
       self.name = name
       self.age = age
       self.handedness

    def get_handedness(self):
        return self.handedness

    def set_handedness(self, handedness):
        valid_options = ["left-handed", "right-handed", ambidextrous"]
        if handedness in valid_options:
            self.handedness = handedness
        else:
            print(f"Invalid handedness. Choose from: {valid options}")

    def print_handedness(self):
        print(f"{self.name} is {self.handedness}")

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Handedness: {self.name}")

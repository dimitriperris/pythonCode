class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    pet_name = input('Please enter your pets name: ')
    pet_type = input('What animal is your pet?  ')
    pet_age = (input('What is the age of your pet? '))  

    pet_specs = Pet(pet_name, pet_type, pet_age)

    print('Pet name is', pet_specs.get_name())
    print('Pet type is', pet_specs.get_animal_type())
    print('Pet age is', pet_specs.get_age())

main()

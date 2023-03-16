import random, json

# Exercice 1

class Book:
    def __init__(self, quotes = []):
         self._quotes = quotes
      
    # Getter method
    def get_quotes(self):
        return self._quotes
    
    # Random quote from getter method
    def get_random_quote(self):
        return random.choice(self._quotes)
      
    # Setter method
    def set_quotes(self, x):
        self._quotes = x
  
book1 = Book()
  
# Setting the quotes using setter
book1.set_quotes(["L'habit ne fait pas le moine", "Ne pas mettre de chausser au moine sur ses habits", "Fuyez si le moine ne porte pas d'habits"])
  
# Retrieving random quote
print("Exercice 1")
print("----------")
print(book1.get_random_quote())
print("----------")


# Exercice 2

class People:
    def __init__(self, firstname, lastname, age, gender):
         self._firstname = firstname
         self._lastname = lastname
         self._age = age
         self._gender = gender
      
    # Getter methods
    def get_firstname(self):
        return self._firstname
    def get_lastname(self):
        return self._lastname
    def get_age(self):
        return self._age
    def get_gender(self):
        return self._gender

    # Json encoder of all dictionary's datas
    def get_datas_json(self):
        return json.dumps({
            "First Name": self._firstname,
            "Last Name": self._lastname,
            "Age": self._age,
            "Gender": self._gender
        })
    
      
    # setter methods
    def set_firstname(self, x):
        self._firstname = x
    def set_lastname(self, x):
        self._lastname = x
    def set_age(self, x):
        self._age = x
    def set_gender(self, x):
        self._gender = x

# Setting values with the construct
people1 = People("Basile", "Martin", 23, "Male")

# Render
print("Exercice 2")
print("----------")
print(people1.get_datas_json())
print("----------")
  


class Person:
  def __init__(self, name, age, sex, major , score):
    self.name = name
    self.age = age
    self.sex = sex
    self.major = major
    self.score = score

  def ageTitle(self):
        if self.age >= 18:
            print("Adult")
        else:
            print("Teen")   


samina = Person("samina",15,"female","Experimental Sciences", "19.87")
samina.ageTitle()



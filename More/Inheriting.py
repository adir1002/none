class Person:
    def __init__(self, name):
        self.name=name
    def say_somthing(self):
        print('Hello,'+self.name)
    def __str__(self):
        return 'Person'

class Student(Person):
    def __init__(self,name,school):
        super().__init__(name)
        self.school=school
    def sing_school_song(self):
        super().say_somthing()
        print('sing a song->'+self.school)
    def __str__(self):
        print('My name is '+self.name+'and im a '+super().say_somthing())
    
adir= Student('Adir','SCE')
adir.sing_school_song()
print(isinstance(adir,Student))
print(isinstance(adir,Person))
print(issubclass(Student,Person))
print(adir)
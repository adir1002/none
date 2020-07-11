class Dog():
    def __init__(self,name='NULL'):
        self.name=name
        self.age=0
    def say_hello(self):
        print('Hello '+'WOOF WOOF ->'+ self.name)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if (value!=None):
            self.__name=value
            self.say_hello()
        else:
            print("NO NO NO NO\n")

jack= Dog()
jack.say_hello()
jack.name='None'

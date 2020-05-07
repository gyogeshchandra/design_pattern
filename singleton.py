class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        else:
            return Singleton.__instance

    def __new__(cls):
        if Singleton.__instance != None:
            raise Exception("This class is singleton")
        else:
            Singleton.__instance = super(Singleton,cls).__new__(cls)
        return Singleton.__instance

    def __init__(self):
        print(self)


s1 = Singleton()
print(s1)

s2 = Singleton().get_instance()
print(s2)
 
            

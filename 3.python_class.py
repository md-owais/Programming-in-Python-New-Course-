class Myclass:
    a = 5 # Reference class object
    print("Hello")
    def hello(self):
        print("Hello, world!")
myc = Myclass()
print(myc.a) # By using instance object
print(myc.hello())
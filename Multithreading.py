from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")

he1 = Hello()
he2 = Hi()

he1.start()
he2.start()

"""
Hello
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hi

"""
print("-----------------------------")

from time import sleep

class Hello1(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi1(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.2)

he3 = Hello1()
he4 = Hi1()

he3.start()
he4.start()

"""
Hi
Hello
Hi
Hi
Hi
Hello
Hi
Hi
Hi
Hi
Hello
Hello
Hello
Hello
"""
print("-----------------------------")

class Hello2(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi2(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.2)

h3 = Hello2()
h4 = Hi2()

h3.start()
h4.start()

h3.join() #wait for end h3,h4 and print Bye
h4.join()

print("Bye")
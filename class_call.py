import book
import Bicycle
import human
from robot import Robot

book_obj =  book.book(304, "Harry potter", "Hard cover")

bicycle_obj = Bicycle.Bicycle("Mountain Bike", 85, 7, "Medium") 

human_obj = human.Human("Asia", 9, "Black")

robot_obj = Robot(10000, 128, 20)

print(human_obj)
print(robot_obj)
print(book_obj)
print(bicycle_obj)

print("Hey I was here, this is stored")

print("testing feature branch or something")
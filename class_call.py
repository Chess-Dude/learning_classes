from book import Book
from Bicycle import Bicycle
from human import Human
from robot import Robot

book_obj =  Book(304, "Harry potter", "Hard cover")

bicycle_obj = Bicycle("Mountain Bike", 85, 7, "Medium") 

human_obj = Human("Asia", 9, "Black")

robot_obj = Robot(10000, 128, 20)

print(human_obj)
print(robot_obj)
print(book_obj)
print(bicycle_obj)
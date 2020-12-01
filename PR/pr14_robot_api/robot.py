"""Robot."""
from PiBot import PiBot

robot = PiBot()
distance_from_object = robot.get_front_middle_laser()
robot.set_wheels_speed(30)
while distance_from_object > 0.2:
    distance_from_object = robot.get_front_middle_laser()
    robot.sleep(0.05)
robot.set_wheels_speed(0)
robot.done()

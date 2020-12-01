"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
if robot.get_front_middle_laser() < 10.0:
    robot.set_wheels_speed(0)
robot.done()

"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
robot.sleep(5)
robot.set_wheels_speed(0)


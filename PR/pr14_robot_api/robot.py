"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(99)
robot.sleep(10)
robot.set_wheels_speed(0)

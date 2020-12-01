"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
robot.sleep(2)
robot.set_wheels_speed(0)
robot.done()

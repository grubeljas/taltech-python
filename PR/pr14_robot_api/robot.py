"""Robot."""
from PiBot import PiBot

robot = PiBot()
while robot.get_line_sensors()[0][0] > 200:
    robot.set_wheels_speed(30)
robot.set_wheels_speed(0)

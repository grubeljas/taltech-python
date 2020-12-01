"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
if robot.get_line_sensors() < 200:
    robot.set_wheels_speed(-30)
    robot.sleep(1)
robot.set_wheels_speed(0)

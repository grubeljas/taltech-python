"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(90)
while robot.get_left_line_sensors()[1] > 300:
    robot.sleep(1)
robot.set_wheels_speed(30)
robot.sleep(1)
robot.set_wheels_speed(0)

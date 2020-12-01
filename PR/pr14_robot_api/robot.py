"""Robot."""
from PiBot import PiBot

robot = PiBot()
while robot.get_leftmost_line_sensor() > 150:
    robot.set_wheels_speed(30)
    robot.sleep(3)
    robot.set_wheels_speed(0)

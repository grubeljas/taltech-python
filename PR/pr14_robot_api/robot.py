"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(20)
while robot.get_second_line_sensor_from_left() > 150:
    robot.set_wheels_speed(80)
    robot.sleep(5)
robot.set_wheels_speed(0)
robot.done()

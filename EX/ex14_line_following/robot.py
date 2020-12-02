"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
while True:
    if robot.get_right_line_sensors()[2] < 400:
        robot.set_wheels_speed(30)
        robot.sleep(1)
    else:
        robot.set_left_wheel_speed(-30)
        robot.set_right_wheel_speed(30)
        robot.sleep(1)
robot.set_wheels_speed(30)
robot.sleep(1)
robot.set_wheels_speed(0)

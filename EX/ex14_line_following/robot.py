"""Robot."""
from PiBot import PiBot

robot = PiBot()
while robot.get_line_sensors()[1] > 500:
    robot.set_wheels_speed(10)
    robot.sleep(0.05)
while sum(robot.get_line_sensors()):
    robot.set_wheels_speed(12)
    robot.sleep(3)
    robot.set_right_wheel_speed(-25)
    robot.set_left_wheel_speed(25)
    robot.sleep(0.5)
    robot.set_wheels_speed(0)

"""Robot."""
from PiBot import PiBot

robot = PiBot()
for i in range(4):
    robot.set_left_wheel_speed(-25)
    robot.set_right_wheel_speed(80)
    robot.sleep(1)
    robot.set_wheels_speed(12)
    robot.sleep(3)
    robot.set_right_wheel_speed(-25)
    robot.set_left_wheel_speed(80)
    robot.sleep(0.5)
    robot.set_wheels_speed(0)

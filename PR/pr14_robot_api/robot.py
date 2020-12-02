"""Robot."""
from PiBot import PiBot

robot = PiBot()
for i in range(100):
    robot.set_left_wheel_speed(-40)
    robot.set_right_wheel_speed(40)
    robot.sleep(1.5)
    robot.set_wheels_speed(10)
    robot.sleep(3)
    robot.set_wheels_speed(0)

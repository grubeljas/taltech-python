"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_right_wheel_speed(-2)
robot.set_left_wheel_speed(2)
robot.sleep(2)
robot.set_right_wheel_speed(0)
robot.set_left_wheel_speed(0)
robot.sleep(1)
robot.set_wheels_speed(30)
robot.sleep(3)
robot.set_wheels_speed(0)
robot.done()

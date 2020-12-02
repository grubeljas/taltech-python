"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
robot.sleep(1)
robot.set_left_wheel_speed(-30)
robot.set_right_wheel_speed(30)
print(robot.get_right_wheel_encoder())
print(robot.get_left_wheel_encoder())
robot.sleep(2)
robot.set_wheels_speed(30)
robot.sleep(1)
robot.set_wheels_speed(0)
robot.done()

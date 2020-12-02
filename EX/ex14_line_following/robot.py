"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
if robot.get_rear_right_side_ir() < 400:
    robot.set_wheels_speed(30)
    robot.sleep(1)
    robot.set_left_wheel_speed(-30)
    robot.set_right_wheel_speed(30)
    robot.sleep(1)
robot.set_wheels_speed(30)
robot.sleep(1)
robot.set_wheels_speed(0)
robot.done()

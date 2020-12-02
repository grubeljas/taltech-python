"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
robot.sleep(1)
print(robot.get_left_line_sensors())
robot.set_right_wheel_speed(80)
robot.sleep(0.1)
robot.set_wheels_speed(30)
robot.sleep(2)
print(robot.get_left_line_sensors())
print(robot.get_leftmost_line_sensor())
print(robot.get_line_sensors())
robot.set_wheels_speed(0)
robot.done()

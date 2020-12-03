"""Robot."""
from PiBot import PiBot

robot = PiBot()
print(robot.get_line_sensors())
robot.set_right_wheel_speed(60)
robot.set_left_wheel_speed(-25)
robot.sleep(0.4)
print(robot.get_line_sensors())
robot.set_wheels_speed(10)
robot.sleep(5)
print(robot.get_line_sensors())
robot.set_wheels_speed(0)

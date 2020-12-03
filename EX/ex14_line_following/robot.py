"""Robot."""
from PiBot import PiBot

robot = PiBot()
print(robot.get_line_sensors())
robot.set_wheels_speed(30)
robot.sleep(5)
robot.set_right_wheel_speed(20)
robot.set_left_wheel_speed(-20)
robot.sleep(3)
print(robot.get_line_sensors())
robot.set_wheels_speed(10)
robot.sleep(5)
print(robot.get_line_sensors())
robot.set_wheels_speed(0)

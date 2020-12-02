"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.get_left_line_sensors()
for i in range(10):
    robot.set_left_wheel_speed(-20)
    robot.set_right_wheel_speed(43)
    print(robot.get_rotation())
    robot.sleep(1.5)
    robot.set_wheels_speed(30)
    robot.sleep(3)
    print(robot.get_left_wheel_encoder())
    print(robot.get_right_wheel_encoder())
    print(robot.get_line_sensors())
robot.set_wheels_speed(0)

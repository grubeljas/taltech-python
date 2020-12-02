"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
robot.sleep(1)
robot.get_left_line_sensors()
for i in range(100):
    robot.set_left_wheel_speed(-30)
    robot.set_right_wheel_speed(40)
    print(robot.get_rotation())
    robot.sleep(1)
    robot.set_wheels_speed(30)
    robot.sleep(0.05)
    print(robot.get_left_wheel_encoder())
    print(robot.get_right_wheel_encoder())
    print(robot.get_left_line_sensors())
    print(robot.get_leftmost_line_sensor())
    print(robot.get_line_sensors())
robot.set_wheels_speed(0)
robot.done()

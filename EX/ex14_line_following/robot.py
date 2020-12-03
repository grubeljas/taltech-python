"""Robot."""
from PiBot import PiBot

robot = PiBot()
print(robot.get_line_sensors())
while robot.get_line_sensors()[2] < 10:
    robot.set_wheels_speed(10)
    robot.sleep(0.05)
    print(robot.get_line_sensors())
while 0 in robot.get_line_sensors():
    """while robot.get_line_sensors()[2] > 10:
        robot.set_right_wheel_speed(25)
        robot.set_left_wheel_speed(-25)
        robot.sleep(0.05)
        print(robot.get_line_sensors())
    """
    while robot.get_line_sensors()[2] == 500:
        robot.set_wheels_speed(10)
        robot.sleep(0.05)
        print(robot.get_line_sensors())
robot.set_wheels_speed(0)

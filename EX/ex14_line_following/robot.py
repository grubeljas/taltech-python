"""Robot."""
from PiBot import PiBot

robot = PiBot()
print(robot.get_line_sensors())
while robot.get_line_sensors()[2] < 10:
    robot.set_wheels_speed(10)
    robot.sleep(0.05)
    print(robot.get_line_sensors())
robot.set_wheels_speed(-10)
robot.sleep(0.05)
i = 20
while 0 in robot.get_line_sensors() and i > -4:
    while robot.get_line_sensors()[2] > 100 or i > 0:
        robot.set_right_wheel_speed(25)
        robot.set_left_wheel_speed(-25)
        robot.sleep(0.05)
        print(robot.get_line_sensors())
        i -= 1
    while robot.get_third_line_sensor_from_left() < 101 or i > - 5:
        robot.set_wheels_speed(10)
        robot.sleep(0.05)
        print(robot.get_line_sensors())
        i -= 1
    break
robot.set_wheels_speed(0)

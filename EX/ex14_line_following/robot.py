"""Robot."""
from PiBot import PiBot

robot = PiBot()
print(robot.get_line_sensors())
i = 21
while 0 in robot.get_line_sensors() and i > 0:
    while i % 3 == 0:
        robot.set_right_wheel_speed(30)
        robot.set_left_wheel_speed(-25)
        robot.sleep(0.05)
        print(robot.get_line_sensors())
        i -= 1
    while i % 5 == 0:
        robot.set_wheels_speed(10)
        robot.sleep(0.05)
        print(robot.get_line_sensors())
    i -= 1
robot.set_wheels_speed(0)

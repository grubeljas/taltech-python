"""Robot."""
from PiBot import PiBot

robot = PiBot()
print(robot.get_line_sensors())
for i in range(50):
    robot.set_wheels_speed(10)
    robot.sleep(0.05)
    print(robot.get_line_sensors())
while False:
    robot.set_wheels_speed(10)
    robot.sleep(0.05)
    print(robot.get_line_sensors())
while robot.get_line_sensors()[3] < 500:
    while robot.get_line_sensors()[4] < 500:
        robot.set_right_wheel_speed(25)
        robot.set_left_wheel_speed(-25)
        robot.sleep(0.05)
        print(robot.get_line_sensors())
    while robot.get_line_sensors()[3] >= 500:
        robot.set_wheels_speed(10)
        robot.sleep(0.05)
        print(robot.get_line_sensors())
robot.set_wheels_speed(0)

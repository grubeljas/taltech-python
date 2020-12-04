"""Robot."""
from PiBot import PiBot

robot = PiBot()

a = 0
while 0 in robot.get_line_sensors() or 16 in robot.get_line_sensors():
    i = 0
    if robot.get_third_line_sensor_from_left() > 0:
        robot.set_right_wheel_speed(-2)
        robot.set_left_wheel_speed(2)
        robot.sleep(0.005)
        print(robot.get_line_sensors())
        i = 1
    if robot.get_third_line_sensor_from_left() == 0:
        robot.set_wheels_speed(8)
        robot.sleep(0.01)
        print(robot.get_line_sensors())
        i = 1
    if i == 0:
        print('MMMMMMMMMMMMMMMMMMM')
        a += 1
        if a == 20:
            break
robot.set_wheels_speed(0)
robot.done()

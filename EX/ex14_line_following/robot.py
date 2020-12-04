"""Robot."""
from PiBot import PiBot

robot = PiBot()

while 0 in robot.get_line_sensors():
    i = 0
    if robot.get_third_line_sensor_from_left() > 0:
        robot.set_right_wheel_speed(-2)
        robot.set_left_wheel_speed(2)
        robot.sleep(0.005)
        i = 1
    if robot.get_third_line_sensor_from_left() == 0:
        robot.set_wheels_speed(10)
        robot.sleep(0.01)
        i = 1
    if i == 0:
        break
robot.set_wheels_speed(0)
robot.done()

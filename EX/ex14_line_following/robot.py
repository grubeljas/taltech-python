"""Robot."""
from PiBot import PiBot

robot = PiBot()
while 0 in robot.get_line_sensors():
    while robot.get_third_line_sensor_from_left() > 100:
        robot.set_right_wheel_speed(-20)
        robot.set_left_wheel_speed(43)
        robot.sleep(0.05)
    while robot.get_third_line_sensor_from_left() == 0:
        robot.set_wheels_speed(10)
        robot.sleep(0.05)
robot.set_wheels_speed(0)
robot.done()

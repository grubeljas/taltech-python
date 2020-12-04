"""Robot."""
from PiBot import PiBot

robot = PiBot()

a = 0
while 0 in robot.get_line_sensors() or 100 > robot.get_line_sensors()[5]:
    if robot.get_third_line_sensor_from_left() > 0:
        robot.set_right_wheel_speed(-2)
        robot.set_left_wheel_speed(2)
        robot.sleep(0.005)
        print(robot.get_line_sensors())
    if robot.get_third_line_sensor_from_left() == 0:
        robot.set_wheels_speed(8)
        robot.sleep(0.01)
        print(robot.get_line_sensors())
robot.set_wheels_speed(0)
robot.done()

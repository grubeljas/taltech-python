"""Robot."""
from PiBot import PiBot

robot = PiBot()
for i in range(100):
    robot.set_left_wheel_speed(-25)
    robot.set_right_wheel_speed(43)
    print(robot.get_rotation())
    robot.sleep(1.5)
    robot.set_wheels_speed(12)
    robot.sleep(3)
    robot.set_wheels_speed(0)

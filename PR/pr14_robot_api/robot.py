"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
distance_from_object = robot.get_front_middle_laser()
while True:
    if robot.get_front_middle_laser() < 10.0:
        robot.set_wheels_speed(0)
        break
    robot.sleep(1)
robot.done()

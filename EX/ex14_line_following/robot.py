"""Robot."""
from PiBot import PiBot

robot = PiBot()
robot.set_wheels_speed(30)
while True:
    if robot.get_rear_right_side_ir() < 400:
        robot.set_wheels_speed(30)
        robot.sleep(0.05)
    elif robot.get_rear_left_straight_ir() > 400:
        break
    else:
        robot.set_left_wheel_speed(-30)
        robot.set_right_wheel_speed(30)
        robot.sleep(0.05)
robot.set_wheels_speed(0)

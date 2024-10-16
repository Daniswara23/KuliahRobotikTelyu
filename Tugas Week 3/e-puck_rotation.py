from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

left_speed = 2.0
right_speed = 6.28

while robot.step(timestep) != -1:
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

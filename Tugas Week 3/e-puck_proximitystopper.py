from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

left_speed = 6.28
right_speed = 6.28

proximity_sensors = []
sensor_names = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']

for sensor_name in sensor_names:
    sensor = robot.getDevice(sensor_name)
    sensor.enable(timestep)
    proximity_sensors.append(sensor)

while robot.step(timestep) != -1:
    front_obstacle = False
    
    for i in range(3): 
        if proximity_sensors[i].getValue() > 80:  
            front_obstacle = True
            break

    if front_obstacle:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
    else:
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

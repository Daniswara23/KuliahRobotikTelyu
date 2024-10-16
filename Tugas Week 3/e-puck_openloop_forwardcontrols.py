# Mengimpor library Webots untuk kontrol robot
from controller import Robot

# Membuat instance dari class Robot
robot = Robot()

# Mendapatkan timestep default dari Webots
timestep = int(robot.getBasicTimeStep())

# Mendapatkan referensi untuk motor roda kiri dan kanan
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Mengatur posisi motor menjadi 'infinite' untuk memungkinkan pengaturan kecepatan
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Mengatur kecepatan awal roda kiri dan kanan (nilai defaultnya adalah 0)
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Kecepatan konstan untuk bergerak maju
speed = 6.28  # kecepatan maksimum dalam rad/s

# Loop kontrol utama
while robot.step(timestep) != -1:
    # Mengatur kecepatan kedua motor untuk membuat robot bergerak maju
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

# Fungsi clean-up akan dipanggil secara otomatis ketika simulasi berhenti

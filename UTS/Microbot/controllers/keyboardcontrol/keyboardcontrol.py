# Import library yang diperlukan dari Webots
from controller import Robot, Keyboard

# Inisialisasi Robot
robot = Robot()

# Mendefinisikan waktu langkah simulasi
TIME_STEP = 64  # interval waktu simulasi (dalam ms)

# Kecepatan dasar untuk gerakan robot
MAX_SPEED = 20  # nilai maksimum kecepatan roda

# Mendefinisikan motor roda kiri dan kanan
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Mengatur motor ke modus kecepatan (Velocity mode)
left_motor.setPosition(float('inf'))  # memungkinkan rotasi terus menerus
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)  # menginisialisasi kecepatan awal sebagai 0
right_motor.setVelocity(0.0)

# Inisialisasi Keyboard untuk kontrol input
keyboard = Keyboard()
keyboard.enable(TIME_STEP)

# Fungsi utama untuk kontrol gerak robot
def control_robot():
    while robot.step(TIME_STEP) != -1:  # loop utama program
        key = keyboard.getKey()  # membaca input keyboard

        # Menginisialisasi kecepatan roda kiri dan kanan
        left_speed = 0.0
        right_speed = 0.0

        # Mengontrol gerakan dengan keyboard
        if key == ord('W'):  # Tombol W untuk maju
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
        elif key == ord('S'):  # Tombol S untuk mundur
            left_speed = -MAX_SPEED
            right_speed = -MAX_SPEED
        elif key == ord('A'):  # Tombol A untuk berbelok ke kiri
            left_speed = -0.5 * MAX_SPEED
            right_speed = 0.5 * MAX_SPEED
        elif key == ord('D'):  # Tombol D untuk berbelok ke kanan
            left_speed = 0.5 * MAX_SPEED
            right_speed = -0.5 * MAX_SPEED

        # Menyetel kecepatan motor roda kiri dan kanan
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

# Menjalankan fungsi kontrol robot
control_robot()
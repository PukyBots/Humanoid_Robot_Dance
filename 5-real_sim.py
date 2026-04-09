import subprocess
import time
import math
import serial

# ====== SERIAL SETUP ======
arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)


# ====== GAZEBO ======
def gz_move(joint, value):
    cmd = f'gz topic -t /model/Nao/joint/{joint}/0/cmd_pos -m gz.msgs.Double -p "data: {value}"'
    subprocess.Popen(cmd, shell=True)


# ====== CONVERSION ======
def rad_to_deg(rad):
    rad = max(min(rad, 1.5), -1.5)
    return int((rad + 1.5) * 60)


# ====== SEND TO ARDUINO ======
def send_servo(channel, angle):
    cmd = f"{channel},{angle}\n"
    arduino.write(cmd.encode())


# ====== JOINT MAP ======
joint_map = [
    ("HeadYaw", 0),
    ("RShoulderRoll", 1),
    ("LHipRoll", 2),
    ("RHipRoll", 3),
    ("RWristYaw", 4),
    ("HeadPitch", 5)
]


# ====== MAIN CONTROL ======
def move_all(values):
    for i, val in enumerate(values):
        joint, ch = joint_map[i]

        # Gazebo
        gz_move(joint, val)

        # Real robot
        angle = rad_to_deg(val)
        send_servo(ch, angle)


# ====== DANCE ======
print("🤖 Starting NAO Dual Control (Arduino + Gazebo)")

t = 0
try:
    while True:
        head = 0.8 * math.sin(t)
        shoulder = -1.2 * math.sin(t)
        lhip = 0.5 * math.sin(t)
        rhip = -0.5 * math.sin(t)
        wrist = 1.0 * math.sin(t)
        extra = 0.3 * math.cos(t)

        move_all([head, shoulder, lhip, rhip, wrist, extra])

        t += 0.2
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping...")
    arduino.close()


#Available joints for real robot-

    #LHipPitch
    #LKneePitch
    #LAnglePitch

    #RHipPitch
    #RKneePitch
    #RAnglePitch

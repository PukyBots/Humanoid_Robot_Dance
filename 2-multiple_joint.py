import subprocess
import time


def move_joints(head_yaw, shoulder_roll):
    cmd1 = f'gz topic -t /model/Nao/joint/HeadYaw/0/cmd_pos -m gz.msgs.Double -p "data: {head_yaw}"'
    cmd2 = f'gz topic -t /model/Nao/joint/RShoulderRoll/0/cmd_pos -m gz.msgs.Double -p "data: {shoulder_roll}"'

    subprocess.Popen(cmd1, shell=True)
    subprocess.Popen(cmd2, shell=True)


print("Starting NAO control...")

while True:
    print("Moving Right Pose")
    move_joints(0.8, -1.5)
    time.sleep(2)

    print("Moving Left Pose")
    move_joints(-0.8, 1.5)
    time.sleep(2)
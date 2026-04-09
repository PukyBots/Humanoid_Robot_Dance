import subprocess
import time


def move_joints(head_yaw, shoulder_roll, left_hip_roll, right_hip_roll, right_wrist_yaw):
    cmd1 = f'gz topic -t /model/Nao/joint/HeadYaw/0/cmd_pos -m gz.msgs.Double -p "data: {head_yaw}"'
    cmd2 = f'gz topic -t /model/Nao/joint/RShoulderRoll/0/cmd_pos -m gz.msgs.Double -p "data: {shoulder_roll}"'
    cmd3 = f'gz topic -t /model/Nao/joint/LHipRoll/0/cmd_pos -m gz.msgs.Double -p "data: {left_hip_roll}"'
    cmd4 = f'gz topic -t /model/Nao/joint/RHipRoll/0/cmd_pos -m gz.msgs.Double -p "data: {right_hip_roll}"'
    cmd5 = f'gz topic -t /model/Nao/joint/RWristYaw/0/cmd_pos -m gz.msgs.Double -p "data: {right_wrist_yaw}"'


    subprocess.Popen(cmd1, shell=True)
    subprocess.Popen(cmd2, shell=True)
    subprocess.Popen(cmd3, shell=True)
    subprocess.Popen(cmd4, shell=True)
    subprocess.Popen(cmd5, shell=True)


print("Starting NAO control...")

while True:
    print("Moving Right Pose")
    move_joints(0.8, -1.5,0,0,0)
    time.sleep(2)

    print("Moving Left Pose")
    move_joints(-0.8, 1.5,0,0,0)
    time.sleep(2)

    print("Moving Right Pose")
    move_joints(0.8, -1.5,1.0,1.0,0.3)
    time.sleep(2)

    print("Moving Left Pose")
    move_joints(-0.8, 1.5,-1.0,-2.0,0)
    time.sleep(2)

    print("Moving Right Pose")
    move_joints(0.8, 1.5,3.0,2.0,1.0)
    time.sleep(2)

    print("Moving Left Pose")
    move_joints(0.8, 1.5,-1.0,0,0)
    time.sleep(2)
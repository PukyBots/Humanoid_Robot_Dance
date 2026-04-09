import subprocess
import time

def move_joint(value):
    cmd = f'gz topic -t /model/Nao/joint/HeadYaw/0/cmd_pos -m gz.msgs.Double -p "data: {value}"'
    subprocess.run(cmd, shell=True)

print("Starting NAO control...")

while True:
    print("Moving Right")
    move_joint(0.8)
    time.sleep(2)

    print("Moving Left")
    move_joint(-0.8)
    time.sleep(2)

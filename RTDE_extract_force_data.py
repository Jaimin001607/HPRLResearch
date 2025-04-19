import sys
import time
import logging
from connector import RTDEConnect
sys.path.append('..')

ROBOT_HOST = '192.168.1.133'
ROBOT_PORT = 30004
config_filename = 'control_loop_configuration.xml'

keep_running = True

monitor = RTDEConnect(ROBOT_HOST, config_filename)

while keep_running:
    # receive the current state
    state = monitor.receive()
    s1 = state.timestamp
    s2 = state.tcp_force_scalar


    print(s1)
    print(s2)

    time.sleep(1)


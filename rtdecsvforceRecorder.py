# This program is meant to be a helper for users to begin experimenting with servo commands. Please see the
# "sendPath.urp" file on the robot to get an idea of how handshaking between the robot and PC are done.
import rtdeState
import csv
import time

ROBOT_HOST = '192.168.1.133'
ROBOT_PORT = 30004
config_filename = 'control_loop_configuration.xml'

state_monitor = rtdeState.RtdeState(ROBOT_HOST, config_filename, frequency=500)
state_monitor.initialize()

force = []
timestamp = []

while state_monitor.keep_running:
    state = state_monitor.receive()
    if state.runtime_state == 2:
        force.append(state.tcp_force_scalar)
        timestamp.append(state.timestamp)
        print(state.tcp_force_scalar)
        

    if state.runtime_state == 0:
        break

state_monitor.con.send_pause()
state_monitor.con.disconnect()


name = 'sanchez.csv'
with open(name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(len(force)):
        writer.writerow([force[i],timestamp[i]])

"""
All commented code below is old. It was used before RTDE outputs could be received at 500Hz.
The code was meant to interpolate the 125Hz to get a 500Hz path. Kept as a reference.
"""
# tf = np.arange(0, ti[-1], 0.02)
#
# q1_f = np.interp(tf, ti, q1)
# q2_f = np.interp(tf, ti, q2)
# q3_f = np.interp(tf, ti, q3)
# q4_f = np.interp(tf, ti, q4)
# q5_f = np.interp(tf, ti, q5)
# q6_f = np.interp(tf, ti, q6)

# name = 'path500.csv'
# with open(name, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     for i in range(len(tf)):
#         writer.writerow([q1_f[i], q2_f[i], q3_f[i], q4_f[i], q5_f[i], q6_f[i]])

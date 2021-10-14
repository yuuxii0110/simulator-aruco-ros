'''
this script is to generate four corner's coordinates for each aruco markers with respect to aruco_map
input: {'id:x':[x,y,z,roll,pitch,yaw]} of the center of a marker
output: coordinates of corners of all aruco markers 
ERROR CAUTIONS:
1)
    need to double check the result, especially for those that rotated >= 180 deg,
    for example: 
    the pose of 
        1) [-2.5, -0.5, 0.5, 0, -1.57, 3.14] & 
        2) [-2.5, -0.5, 0.5, 3.14, -1.57, 0] 
        
    will show the same orientation and position in gazebo,
    
    the output for above are:
        1) [[-2.5002123801990743, -0.5888997745011922, 0.5888999718126401], [-2.499929206510523, -0.41110000000003577, 0.5888999718126401], [-2.4997876198009257, -0.4111002254988077, 0.4111000281873599], [-2.500070793489477, -0.5888999999999642, 0.4111000281873599]] }
        2) [[-2.4999292065554157, -0.4111, 0.5888999718126401], [-2.4999292065554157, -0.5889, 0.5888999718126401], [-2.5000707934445843, -0.5889, 0.4111000281873599], [-2.5000707934445843, -0.4111, 0.4111000281873599]] }
    respectively,
    but the correct answer is the first answer...
    
2)
    when copy to yml file, keep the format exactly the same, even a extra empty line or tap might causing error when loading the yml file.
'''


import numpy as np
from math import sin, cos, pi

marker_size = 0.1778
rotating_matrix = np.array([[1, 0, 0],
                            [0, 0, 1],
                            [0, -1,  0]])

#[x,y,z,roll,pitch,yaw], can get from aruco_world.world file/ manually key in 

location = {'id:0': [1.5 ,1.5, 1, -0, -1.57, 1.57],  
            'id:1': [0, 1.5, 0.5, -0, -1.57, 1.57],  
            'id:2':[-1.5, 1.5, 1, -0, -1.57, 1.57], 
            'id:3':[-2.5, -0.5, 0.5, 0, -1.57, 3.14],   
            'id:4':[-2.5, 0.5, 1, 0, -1.57, 3.14],   
            'id:5': [0, 1.5, 1.5, -0, -1.57, 1.57],   
            'id:6':[2.5, 0.5, 1, 0, -1.57, 0],   
            'id:7':[2.5, -0.5, 0.5, 0, -1.57, 0]} 

result = {e:[] for e in location.keys()}
rotated_result = {e:[] for e in location.keys()}

R = marker_size/2
for key,value in location.items():
    tmp=[]
    tmp2=[]
    origin = np.array(value[0:3])
    roll = value[3]
    pitch = value[4]
    yaw = value[5]

    C1 = np.array([R,R,0])
    C2 = np.array([R,-R,0])
    C3 = np.array([-R,-R,0])
    C4 = np.array([-R,R,0])
    corners = [C1,C2,C3,C4]

    Rz = np.array([[cos(yaw), -sin(yaw), 0],
                [sin(yaw), cos(yaw),  0],
                [0,         0      ,  1]])

    Ry = np.array([[cos(pitch),  0 , sin(pitch)],
                [0,           1 ,          0],
                [-sin(pitch), 0, cos(pitch)]])

    Rx = np.array([[1,         0,          0],
                [0, cos(roll), -sin(roll)],
                [0, sin(roll), cos(roll)]])

    R_total = np.matmul(Rz, Ry, Rx)              #total rotation

    for C in corners:
        delta_distance = np.matmul(R_total,C)
        cor = delta_distance + origin
        tmp.append(list(cor))
        rotated = np.matmul(rotating_matrix,delta_distance + origin)
        tmp2.append(list(rotated))

    result[key] = tmp
    rotated_result[key] = tmp2

print(" ")
print("coordinate in gazebo: ")
print("__________________________________________________for debugging______________________________________________________________")
for i in result.items():
    id = list(i)[0]
    lst = list(i)[1]
    chr1 = "{ "
    chr2 = " }"
    print(f"    - {chr1}{id}, corners: {lst}{chr2}")
print(" ")

print("coordinate after rotating: ")
print("__________________________________________________copy below to yml file______________________________________________________________")
for i in rotated_result.items():
    id = list(i)[0]
    lst = list(i)[1]
    chr1 = "{ "
    chr2 = " }"
    print(f"    - {chr1}{id}, corners: {lst}{chr2}")

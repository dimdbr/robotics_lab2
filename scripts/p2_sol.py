# import required modules 
import math
import numpy as np 

# define 6 basic funcions for homogeneous transformation using slides

# translation along 3 axes
def trans_x_a(a): 
	trans_x = np.array([[1.0, 0.0, 0.0, a],
						[0.0, 1.0, 0.0, 0.0],
						[0.0, 0.0, 1.0, 0.0],
						[0.0, 0.0, 0.0, 1.0]])
	return trans_x

def trans_y_b(b): 
	trans_y = np.array([[1.0, 0.0, 0.0, 0.0],
						[0.0, 1.0, 0.0, b],
						[0.0, 0.0, 1.0, 0.0],
						[0.0, 0.0, 0.0, 1.0]])
	return trans_y

def trans_z_c(c): 
	trans_z = np.array([[1.0, 0.0, 0.0, 0.0],
						[0.0, 1.0, 0.0, 0.0],
						[0.0, 0.0, 1.0, c],
						[0.0, 0.0, 0.0, 1.0]])
	return trans_z
	
# rotation about 3 axes	
def rot_x_a(alpha): 
	rot_x = np.array([[1.0, 0.0, 0.0, 0.0],
				     [0.0, math.cos(alpha), -math.sin(alpha), 0.0],
				     [0.0, math.sin(alpha), math.cos(alpha), 0.0],
					 [0.0, 0.0, 0.0, 1.0]])
	return rot_x
	
def rot_y_b(beta): 
	rot_y = np.array([[math.cos(beta), 0.0,math.sin(beta), 0.0],
				     [0.0, 1.0, 0.0, 0.0],
				     [-math.sin(beta), 0.0, math.cos(beta), 0.0],
					 [0.0, 0.0, 0.0, 1.0]])
	return rot_y
	
def rot_z_g(gamma): 
	rot_z = np.array([[math.cos(gamma), -math.sin(gamma),0.0, 0.0],
				     [math.sin(gamma), math.cos(gamma), 0.0, 0.0],
				     [0.0, 0.0, 1.0, 0.0],
					 [0.0, 0.0, 0.0, 1.0]])
	return rot_z

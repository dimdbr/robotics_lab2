# import the rigid body motion module
import rbm
import math
import numpy as np 

if __name__ == '__main__': 
	# define rotation degrees
	# about x_0 
	psi = math.pi/2 
	# about y_0 
	theta = math.pi/2 
	# about z_0 
	phi = math.pi/2 
	# define a 3D rotation about x axes
	Rx = rbm.rot_x(psi)
	# define a 3D rotation about y axes
	Ry = rbm.rot_y(theta)
	# define a 3D rotation about z axes
	Rz = rbm.rot_z(phi)
	# calculate a total rotation via CURRENT FRAMES
	# we will use premultiplication in this case
	R = np.matmul(Ry, Rx)
	R = np.matmul(Rz, R)
	# define test 3D vector
	v_test = rbm.vec(1,1,1)	
	np.set_printoptions(precision = 2, suppress = True)
	v_test_transformed = R.dot(v_test)
	print('Final rotation matrix is:\n',R)
	print('The transformed vector (rotations about FIXED FRAME) is:\n',v_test_transformed)
	

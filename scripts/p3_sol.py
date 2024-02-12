# import needed modules
import math
import numpy as np  
# import the module with homogeneous transformations
import p2_sol 


if __name__ == '__main__': 

	np.set_printoptions(precision = 2, suppress = True)
	
	# Transformation 1 CURRENT FRAME 
	# translation of 2.5 units along the current x-axis
	tran_x = p2_sol.trans_x_a(2.5) 
	# translation of 0.5 units along the current z-axis
	tran_z = p2_sol.trans_z_c(0.5)
	# translation of -1.5 units along the current y-axis
	tran_y = p2_sol.trans_y_b(-1.5)
	# because of CURRENT frame have to use postmultiply 
	H_1 = np.matmul(tran_x, tran_z) 
	H_1 = np.matmul(H_1, tran_y) 
	print('Final homogeneous transformations matrix H_1 is:\n',H_1) 
	
	
	# Transformation 2 CURRENT FRAME 
	# translation of 0.5 units along the current z-axis
	tran_z = p2_sol.trans_z_c(0.5)
	# translation of 2.5 units along the current x-axis
	tran_x = p2_sol.trans_x_a(2.5) 
	# translation of -1.5 units along the current y-axis
	tran_y = p2_sol.trans_y_b(-1.5)
	# because of CURRENT frame have to use postmultiply 
	H_2 = np.matmul(tran_z, tran_x) 
	H_2 = np.matmul(H_2, tran_y) 
	print('Final homogeneous transformations matrix H_2 is:\n',H_2) 

	# Transformation 3 FIXED FRAME 
	# translation of 2.5 units along the current x-axis
	tran_x = p2_sol.trans_x_a(2.5) 
	# translation of 0.5 units along the current z-axis
	tran_z = p2_sol.trans_z_c(0.5)
	# translation of -1.5 units along the current y-axis
	tran_y = p2_sol.trans_y_b(-1.5)
	# because of CURRENT frame have to use premultiply 
	H_3 = np.matmul(tran_z, tran_x) 
	H_3 = np.matmul(tran_y, H_3) 
	print('Final homogeneous transformations matrix H_3 is:\n',H_3) 

	# Transformation 4 FIXED FRAME 
	# translation of 0.5 units along the current z-axis
	tran_z = p2_sol.trans_z_c(0.5)
	# translation of 2.5 units along the current x-axis
	tran_x = p2_sol.trans_x_a(2.5) 
	# translation of -1.5 units along the current y-axis
	tran_y = p2_sol.trans_y_b(-1.5)
	# because of CURRENT frame have to use premultiply 
	H_4 = np.matmul(tran_x, tran_z) 
	H_4 = np.matmul(tran_y, H_4) 
	print('Final homogeneous transformations matrix H_4 is:\n',H_4) 

	# extra function for further testing
	def vec(x,y,z):
		#Define a vector as an numpy and transpose it to a column vector.
		vec = np.array([[x, y, z,1.0]]).T 
		return vec
		
    # Transformation 5 CURRENT FRAME 
    # rotation by angle π/2 about the current x-axis
	rot_x = p2_sol.rot_x_a(math.pi/2) 
	# translation of 3 units along the current x-axis
	tran_x = p2_sol.trans_x_a(3) 
	# translation of -3 units along the current z-axis
	tran_z = p2_sol.trans_z_c(-3)
	# rotation by angle -π/2 about the current z-axis
	rot_z = p2_sol.rot_z_g(-math.pi/2)
	# because of CURRENT frame have to use postmultiply 
	H_5 = np.matmul(rot_x, tran_x) 
	H_5 = np.matmul(H_5, tran_z) 
	H_5 = np.matmul(H_5, rot_z)
	print('Final homogeneous transformations matrix H_5 is:\n',H_5) 
	v_test = vec(0,1,1) 
	print('The test vector is:\n',v_test)
	v_test_transformed = H_5.dot(v_test)
	print('The transformed vector (transformations(rotations and translations) about CURRENT FRAME) is \n',v_test_transformed)
	

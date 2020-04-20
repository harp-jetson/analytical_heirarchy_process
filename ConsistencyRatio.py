import numpy as np

def ConsistencyRatio(criteria_matrix, priority_vector):
	
	# defining the Random Index
	random_index=[0, 0, .58, .9, 1.12, 1.24, 1.32, 1.41, 1.45]
	
	# matrix multiplying priority vector weights * criteria matrix
	summed_rows = criteria_matrix.dot(priority_vector)

	# element by element wise division
	some_vector = np.divide(summed_rows,priority_vector)
	
	# average the last vector to get lambda max
	lambda_max = np.mean(some_vector)

	rows, columns = criteria_matrix.shape 
	# it's a square matrix so could've used rows or columns
	consistency_index = 0
	consistency_index = (lambda_max - rows)/(rows - 1)

	consistencyRatio = consistency_index / random_index[rows]
	return consistencyRatio
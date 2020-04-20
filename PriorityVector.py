import numpy as np

def PriorityVector(criteria_matrix):
	
	# sum the columns
	column_sums = criteria_matrix.sum(axis=0)
	
	priority_vector = []
	for row in criteria_matrix:
		
		# element by element division
		# divide each element in the column by the sum
		# normalize each row
		normalized_criteria_matrix = np.divide(row, column_sums)
		
		# average the rows 
		priority_vector.append(np.mean(normalized_criteria_matrix))

	return priority_vector

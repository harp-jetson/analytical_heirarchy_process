from PriorityVector import PriorityVector
from ConsistencyRatio import ConsistencyRatio
import numpy as np


print_options = 0
print_criteria = 0
print_criteria_matrix = 0
print_criteria_comparison_matrix = 0
print_priority_vector = 0
print_consistency_ratio = 0
print_priority_vector_matrix = 0

# defining options for clarity in printing later
# keep this order consistent throughout the process
options = []
options.append("MPLab PIC32")
options.append("Vorago VA10820")
options.append("Microchip STK600")

if print_options:
    print("options: ")
    for option in options:
        print("\t {}".format(option))

criteria = []
criteria.append("IDE")
criteria.append("Radiation Protection")
criteria.append("Space Proven")
criteria.append("Processor Speed")
criteria.append("Price")
criteria.append("Memory Size")

if print_criteria:
    print("criteria: ")
    for choice in criteria:
        print("\t {}".format(choice))

# defining Matrices
                     # IDE Radiation   Space  Processor Price
                     #     Protection  Proven   Speed        
# IDE                   #      #         #        #       #  # look at [2,1]
# Radiation Protection  2      #         #        #       #  # Radiation Protection is 2x more preferred than IDE
# Space Proven          #      #         #        #       #  
# Processor Speed       #      #         #        #       #  
# Price                 #      #         #        #       #  
# Memory Size           #      #         #        #       #  
criteriaMatrix = []
criteriaMatrix = np.array( [ [  1,  1/7,  1/3,  1/4,    2], 
                             [  7,    1,    2,    5,    6], 
                             [  3,  1/2,    1,    3,    5],
                             [  4,  1/5,  1/3,    1,    2],
                             [1/2,  1/6,  1/5,  1/2,    1] ] )

if print_criteria_matrix:
    # print(criteriaMatrix)
    print("criteriaMatrix: ")
    for i, row in enumerate(criteriaMatrix):
        # print(matrix)
        for element in row:
            print("\t {:1.3f}".format(element), end = '') 
        print("\t {}".format(criteria[i]))
        print("\n")

                  # MPLab PIC32  Vorago VA10820 Microchip STK600
# MPLab PIC32            #             #                 #      # look at [2,1]
# Vorago VA10820         6             #                 #      # Vorago VA10820 is 6x more preferred than MPLab PIC32
# Microchip STK600       #             #                 #

# 1: IDE
# MPLab ATSAM4E-EK = Yes, very nice with in circuit debugger capabilities
# Vorago REB1-VA10820 = No, just command line
# Microchip ATSTK600-ND = Yes, with multiple debug add ons
CriteriaComparisonMatrix = np.array( [ [ [   1,   5,    2], 
                                       [ 1/5,   1,  1/4], 
                                       [ 1/2,   4,    1] ] ]) 


# 2: Radation Protection
# MPLab ATSAM4E-EK = no radiation protection
# Vorago REB1-VA10820 = radiation hardened 
# Microchip ATSTK600-ND = radiation tolerant
CriteriaComparisonMatrix = np.vstack((CriteriaComparisonMatrix,
                                     [[ [   1, 1/9,  1/5],
                                       [   9,   1,    3],
                                       [   5, 1/3,    1] ]]))

# 3: Space Proven
# MPLab ATSAM4E-EK = Yes, in LEO
# Vorago REB1-VA10820 = Yes, In LEO 
# Microchip ATSTK600-ND = No
CriteriaComparisonMatrix = np.vstack((CriteriaComparisonMatrix,
                                     [ [ [   1,   5,    5],
                                       [ 1/5,   1,    1],
                                       [ 1/5,   1,    1] ] ]))
# 4: Processing Speed
# MPLab ATSAM4E-EK = up to 120MHz
# Vorago REB1-VA10820 = 50MHz 
# Microchip ATSTK600-ND = 8MHz
CriteriaComparisonMatrix = np.vstack((CriteriaComparisonMatrix,
                                     [ [ [   1,   3,    5],
                                       [ 1/3,   1,    4],
                                       [ 1/5, 1/4,    1] ] ]))
# 5: Price
# MPLab ATSAM4E-EK = $278.99
# Vorago REB1-VA10820 = $730
# Microchip ATSTK600-ND = $215.06
CriteriaComparisonMatrix = np.vstack((CriteriaComparisonMatrix,
                                     [ [ [   1,   4,    2],
                                       [ 1/4,   1,  1/4],
                                       [ 1/2,   4,    1] ] ]))


if print_criteria_comparison_matrix:
    print("CriteriaComparisonMatrix: ")
    for i,matrix in enumerate(CriteriaComparisonMatrix):
        print("\t {}".format(criteria[i]))
        for j,row in enumerate(matrix):
            for element in row:
                print("\t\t {:1.3f}".format(element), end = '') 
            print("\t {}".format(options[j]))
            print("\n")
        print("\n")

# find priority vectors of criteria matrix 
priority_vector = PriorityVector(criteriaMatrix);
if print_priority_vector:
    print(priority_vector)

# find consistency ratio of criteria matrix
criteriaConsistency=ConsistencyRatio(criteriaMatrix, priority_vector)
if print_consistency_ratio:
    print(criteriaConsistency)

# find priority vector and consistency ratio for each criteria comparison matrix
priorityVecMatrix = []
consistency_ratio = []
for i in range(len(criteria)-1):
    # print(len(criteria))
    single_priority_vector = PriorityVector(CriteriaComparisonMatrix[:][:][i])
    priorityVecMatrix.append(single_priority_vector)
    single_consistency_ratio = ConsistencyRatio(CriteriaComparisonMatrix[:][:][i], single_priority_vector)
    consistency_ratio.append(single_consistency_ratio)

# convert to np array for easier printing
consistency_ratio = np.array(consistency_ratio).T
if print_consistency_ratio:
    print(consistency_ratio)
#convert to np array for easier printing
priorityVecMatrix = np.array(priorityVecMatrix).T
if print_priority_vector_matrix:
    print(priorityVecMatrix)

winner=priorityVecMatrix.dot(priority_vector)

# printing the results
for i in range(len(options) ):
    print("{}: {:1.3f}".format(options[i],winner[i]))

import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
     return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    return False

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    return False

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
UC add to queue 
'''
def is_queue_empty_UC():
    # Your code here
    return False

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    return False

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
	state = []
	if (n <= 0):
		return state
	
	
	for x in range(n):
		state.append(random.randint(1, n))
	
	return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
	# count number of elements in state
	n = len(state)
	nLimit = n-1
	#  CREATE AND INITIALIZE TABLE
	
	# Create table: Table of empty rows
	aTable = [[] for _ in range(n)]
	# print aTable

	# Initialize table:
	rowIndex = 0
	while rowIndex <= nLimit:
		for x in range(n):
			aTable[rowIndex].append('')
		#print aTable
		rowIndex += 1
		#print("============")
	# print aTable
	
	# add queens
	colIndex = 0
	while (colIndex <= nLimit):
		rowVal = state[colIndex] - 1
		aTable[rowVal][colIndex] = 'Q'
		colIndex += 1
	# print aTable

	# ==== COMPUTE ATTACKS

	# Horizontal | Checks if the same number exists elsewhere in the state[]
	hAttacks = 0
	for stateIndex in range(n):
		selected = state[stateIndex]
		# print("SELECTED VAL: " + str(selected))
		subRange = nLimit - stateIndex
		for subIndex in range(subRange):
			# print("new arr: " + str(state[index + newIndex + 1]))
			if (state[stateIndex + subIndex + 1] == selected):
				hAttacks += 1

	# print("Horizontal hits: " + str(hAttacks))

	# Diagonals
	qCol = 0
	stateIndex = 0
	totalDiagonalHits = 0
	while qCol <= nLimit:
		# Get queen's row value
		qRow = state[stateIndex] - 1
		#Queen's coordinate = its row and column.
		qCoordTpl = (qRow+1, qCol+1)
		#Print for confirmation. If Q shows up = ready
		# print(">>>>>>>>>>>>>Queen: @ " + str(qCoordTpl) + " : " + str(arrTable[qRow][qCol]))
	
		
		# Down Right (+ +)
		# Current position = qRow, qCol
		diagonalHit = 0
		subQRow = qRow + 1
		subQCol = qCol + 1
		while (subQRow <= n-1 and subQCol <= n-1):
			if (aTable[subQRow][subQCol] == aTable[qRow][qCol]):
				
				hitTpl = (aTable[qRow][qCol], aTable[subQRow][subQCol])
				subQCoordTpl = (subQRow +1, subQCol + 1)
				
				# print("HIT: [" + str(hitTpl) + "]" + "[(" + str(qCoordTpl) + ") X (" + str(subQCoordTpl) + ")]")
				diagonalHit += 1
			subQRow += 1
			subQCol += 1
			
		
		# Up Right (- +)
		subQRow = qRow - 1
		subQCol = qCol + 1
		while (subQRow >= 0 and subQCol <= n-1):
			if (aTable[subQRow][subQCol] == aTable[qRow][qCol]):
				hitTpl = (aTable[qRow][qCol], aTable[subQRow][subQCol])
				subQCoordTpl = (subQRow + 1, subQCol + 1)
				
				# print("HIT: [" + str(hitTpl) + "]" + "[(" + str(qCoordTpl) + ") X (" + str(subQCoordTpl) + ")]")
				diagonalHit += 1
			subQRow -= 1
			subQCol += 1
			
	
		# print ("DIAGONAL HITS  @ " + str(qRow + 1) + "," + str(qCol + 1) + ": " + str(diagonalHit))
		totalDiagonalHits += diagonalHit
		# iteration
		qCol += 1
		stateIndex += 1

	total = totalDiagonalHits + hAttacks

	# print("TOTAL HITS: " + str(total))
	
	number_attacking_pairs = total
	
	return number_attacking_pairs



'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
	final_state = []
	
	
	
	
	
	#Copy state into ORI state for safe keeping
	oriState = []
	for i in range(len(state)):
		oriState.append(state[i])
	
	oriConflicts = comp_att_pairs(oriState)
	
	#print(state)
	#print(oriState)
	
	n = len(state)
	nLimit = n-1
	#base case
	if n == 0:
		return []
	
	
	
	prevConflicts = oriConflicts
	minCol = 0
	minRow = state[minCol] - 1
	
	minConflicts = oriConflicts - 1
	while (1):
		#print("START ITERATION")
		colStateIndex = 0
		
		
		minConflicts = comp_att_pairs(state)
		#print("Minimum value set to: " +str(minConflicts))
		while colStateIndex <= nLimit:
			# for each column in state[]
			#print(">> Column " + str(colStateIndex) + " of " + str(nLimit))
			potentialRow = 0
			originalValue = state[colStateIndex] - 1
			
			
			# print ("State RESET: " + str(state))
			
			while potentialRow <= nLimit:
				
				state[colStateIndex] = potentialRow + 1
				# print state
				#keep track of minimum x value (change variable names after)
				tempMin = comp_att_pairs(state)
				#print ("Conflicts at "+ str(potentialRow) + "," + str(colStateIndex) + " is: " + str(tempMin))
				
				if (tempMin < minConflicts):
					minConflicts = tempMin
					minCol = colStateIndex
					minRow = potentialRow
					
				potentialRow+=1
			
			minTuple = (minConflicts, "@", minRow, minCol)
			state[colStateIndex] = originalValue + 1
			colStateIndex+= 1
		
		
		#Just for checking
		newState = []
		for i in range(len(state)):
			newState.append(state[i])
		 
		newState[minCol] = minRow+1
		
		
		state[minCol] = minRow+1
		if (minConflicts == 0):
			break
		elif (prevConflicts == minConflicts):
			break
		else:
			prevConflicts = minConflicts
		

	
	return state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
	final_state = []
	# Your code here
	conflicts = n
	#iteration = 0
	if (n > 3):
		while (conflicts != 0):
			#print("RESET!!")
			
			#print("ITERATION #" + str(iteration))
			state = get_rand_st(n)
			final_state = hill_descending(state, comp_att_pairs)
			conflicts = comp_att_pairs(final_state)
			#print("Conflicts: " + str(conflicts) + " | State: " + str(final_state))
			#iteration+=1
	else:
	
		final_state.append("No Solution for given n value.")
	
	
	return final_state








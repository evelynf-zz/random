#bfs
def island_bfs(x_coord, y_coord, array):
	#run bfs & mark all the seen ones as Ns
	queue = [(x_coord, y_coord)]
	visited = []
	length = 0
	while len(queue) != 0:	
		parent_x, parent_y = queue.pop(0)
		#takes into account if visited or not
		# print "x", parent_x
		# print "y", parent_y
		# print array[parent_y][parent_x]
		if array[parent_y][parent_x] == 1:
			array[parent_y][parent_x] = "X"
			length +=1
			neighbors = [(parent_x -1, parent_y), (parent_x+1, parent_y), (parent_x, parent_y-1), (parent_x, parent_y+1)]
			for neighbor in neighbors:
				#check if in array
				if neighbor not in visited:
					if neighbor[0] < len(array[0]) and neighbor[0] >= 0 and neighbor[1] < len(array) and neighbor[1] >= 0:
						queue.append(neighbor)
						visited.append(neighbor)
		elif array[parent_y][parent_x] == 0:
			array[parent_y][parent_x] = "S"
	print array
	return length

#dfs recursive
def find_island(x, y, grid):
	return find_island_helper((x,y), grid, {})

def find_island_helper((x, y), grid, visited):
	#base cases
	if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
		return 0
	if not grid[y][x]: 
		return 0
	if (x,y) in visited:
		return 0
	children = [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]
	visited[(x,y)] = 1
	size = 1
	for child in children:
		size += find_island_helper(child, grid, visited)
	return size 
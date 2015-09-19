import kdtree

def route(start, destinations):
	print start
	print destinations
	tree = kdtree.create(destinations, dimensions=2)
	order = [tree.search_nn(start)[0].data]
	print order
	for i in range(len(destinations) - 1):
		tree.remove(order[-1])
		next = tree.search_nn(order[-1])
		order.append(next[0].data)
	return order


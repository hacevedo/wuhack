import kdtree
# Comments for debugging purposes only
#from formatIO import Destination

#dests = [Destination(lat=0.0, long=0.0, id="0"), Destination(lat=40.745617, long=-74.00324, id="1"), Destination(lat=40.730125, long=-74.0004, id="2"), Destination(lat=40.80586, long=-73.94951, id="3"), Destination(lat=40.734184, long=-74.0028, id="4")]
#start = (41.0, 42.0)

def route(start, destinations):
	tree = kdtree.create(destinations, dimensions=2)
	order = [tree.search_nn(start)[0].data]
	for i in range(len(destinations) - 1):
		tree = tree.remove(order[-1])
		next = tree.search_nn(order[-1])
		order.append(next[0].data)

	return order


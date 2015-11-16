import pprint
cities = ['Beaufort West','Beitbridge','Bloemfontein','Cape Town','Colesberg','Durban','East London','George','Graaff-Reinet','Grahamstown','Johannesburg','Kimberley','Nelspruit','Oudsthoorn','Port Elizabeth','Pretoria','Springbok','Umtata','Upington']
print 'There are',len(cities),'cities'
print 'and', len(cities)*(len(cities)+1)/2, 'entries'
adj = [[0 for i in xrange(len(cities))]for j in xrange(len(cities))]
pprint.pprint(adj)
print ''
for i in xrange(len(cities)):
	for j in xrange(len(cities)):
		if i != j:
			adj[i][j] = 1
pprint.pprint(adj)
adj[0][1] = 1503
adj[0][2] = 535
adj[0][3] = 463
adj[0][4] = 316
adj[0][5] = 1225
adj[0][6] = 597
adj[0][7] = 237
adj[0][8] = 209
adj[0][9] = 483
adj[0][10] = 951
adj[0][11] = 497
adj[0][12] = 1293
adj[0][13] = 179
adj[0][14] = 405
adj[0][15] = 1009
adj[0][16] = 741
adj[0][17] = 718
adj[0][18] = 519

adj[1][2] = 955
adj[1][3] = 1957
adj[1][4] = 1174
adj[1][5] = 1081
adj[1][6] = 1530
adj[1][7] = 1719
adj[1][8] = 1377
adj[1][9] = 1525
adj[1][10] = 552
adj[1][11] = 1026
adj[1][12] = 513
adj[1][13] = 1669
adj[1][14] = 1620
adj[1][15] = 494
adj[1][16] = 0 #continue from here
adj[1][17] = 0
adj[1][18] = 0
print ''
pprint.pprint(adj)
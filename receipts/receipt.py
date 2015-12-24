import time

class Receipt():
	def __init__(self, price=0, category='misc'):
		self.price = price
		self.category = category
		# categories will include 
		self.time = time.ctime()

	def __str__(self):
		print "This purchase was a %s product/service that cost %.2f \nThis purchase was made at %s" % (self.category,self.price, self.time)

def main():
	r = Receipt()
	print r.__str__()

if __name__ == '__main__':
	main()
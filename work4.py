class nesh(object): 
	def __init__(self, something): 
		print("A init called") 
		self.something = something 
		

class malli(nesh): 
	def __init__(self, something): 
		print("B init called") 
		self.something = something  
		nesh.__init__(self, something) 
		
a = malli("Something") 

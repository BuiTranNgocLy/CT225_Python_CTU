class Point:
	def _init_(self, x=0,y=0):
		self.x=x
		elf.y=y
	def _sub_(self, other):
		x=self.x+ other.x
		y=self.y + other.y 
		return Point(x,y)
	p1=Point(3,4)
	p2=Point(1,2)
	result=p1 - p2
	print(result.x, result.y)
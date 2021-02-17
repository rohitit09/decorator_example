class Myplexer:
	def __init__(self):
		self.avail_func={}

	def route(self, command):
			def wrap(args):
				self.avail_func[command]=args
				return args	
			return wrap

	def getCommand(self, key, value):
		if self.avail_func.get(key,None) is not None or self.avail_func.get(key+" $name",None) is not None:
			if key=='count':
				print(self.avail_func[ key ](*value.split()))
			elif key=='sayhito':
				print(self.avail_func[ key+" $name" ](value))
			else:
				print(self.avail_func[key]())
		else:
			print("wrong command")


	def run(self):
		print("Run was called>")
		while True:
			cmd = input(">")
			args = cmd.split()
			self.getCommand( args[0], ' '.join( args[1:] ) )

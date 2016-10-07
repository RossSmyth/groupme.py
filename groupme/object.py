
class Object:
	"""Represents a generic object.
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two objects are equal.     |
	+-----------+--------------------------------------+
	| x != y    | Checks if two objects are not equal. |
	+-----------+--------------------------------------+
	| hash(x)   | Returns the object's hash.           |
	+-----------+--------------------------------------+
	| str(x)    | Returns the object's name.           |
	+-----------+--------------------------------------+
	
	Used to make most objects within the library
	
	Attributes
	----------
	id : str
		The ID of the object
	"""
	__slots__ = []
	
	def __init__(self, **kwargs):
		self.id = kwargs.pop('id')
		
	def __eq__(self, other):
		return isinstance(other, self.__class__) and other.id == self.id
		
	def __ne__(self, other):
		if isinstance(other, self.__class__):
			return other.id != self.id
		return True
		
	def __hash__(self):
		return hash(self.id)
		
	def __str__(self):
		return self.name
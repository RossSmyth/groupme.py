from .object import Object

class Member(Object):
	"""Represents a Group Me member.
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two members are equal.     |
	+-----------+--------------------------------------+
	| x != y    | Checks if two members are not equal. |
	+-----------+--------------------------------------+
	| hash(x)   | Returns the members's hash.          |
	+-----------+--------------------------------------+
	| str(x)    | Returns the member's name.           |
	+-----------+--------------------------------------+
	
	Attributes
	----------
	autokicked : bool
		Whether the member is automatically kicked or not
	id : str
		The unique ID of the member
	image_url : str
		URL of the member's avatar
	muted : bool
		Wether the member is muted or not
	name : str
		The name of the member
	user_id : str
		The ID in that group of the user
	"""
	__slots__ = [
				'autokicked', 'id', 'image_url', 'muted', 'name', 'user_id'
				]
		
	def __init__(self, **kwargs):
		super(Member, self).__init__(**kwargs)

		self.autokicked = kwargs.pop('autokicked')
		self.id = kwargs.pop('user_id')
		self.image_url = kwargs.pop('image_url')
		self.muted = kwargs.pop('muted')
		self.name = kwargs.pop('nickname')
		self.user_id = kwargs.pop('id')

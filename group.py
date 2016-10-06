
class Group:
	"""Represents a Group Me group.
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two groups are equal.      |
	+-----------+--------------------------------------+
	| x != y    | Checks if two groups are not equal.  |
	+-----------+--------------------------------------+
	| hash(x)   | Returns the groups's hash.           |
	+-----------+--------------------------------------+
	| str(x)    | Returns the group's name.            |
	+-----------+--------------------------------------+
	
	Attributes
	----------
	created_at : int
		The unix time-stamp when the group was made
	description : str
		The group's description
	image_url : str
		The URL of the group's image
	id : str
		The ID of the group
	max_members : int
		The maximum members allowed in the group
	members : ???
		List of members (TO BE FINAL LATER)
	messages : ???
		??? (TO BE FINAL LATER)
	name : str
		The name of the group
	office_mode : bool
		When the group is in office mode or not
	phone_number : str
		The phone number of the group
	share_url : str
		URL to join the group, can be none if private
	type : str
		Whether the group is public or private
	updated_at : int
		unix time-stamp of when the group was updated last	
	"""
	__slots__ = [
		'created_at', 'description', 'image_url', 'id', 'max_members',
		'members', 'messages', 'name', 'office_mode', 'phone_number',
		'share_url', 'type', 'updated_at'
		]
	
	def __init__(self, **kwargs):
	
		self.created_at = kwargs.pop('created_at')
		self.description = kwargs.pop('description')
		self.image_url = kwargs.pop('image_url')
		self.id = kwargs.pop('id')
		self.max_members = kwargs.pop('max_members')
		self.name = kwargs.pop('name')
		self.office_mode = kwargs.pop('office_mode')
		self.phone_number = kwargs.pop('phone_number')
		self.share_url = kwargs.pop('share_url')
		self.type = kwargs.pop('type')
		self.updated_at = kwargs.pop('updated_at')
		
		self._members = kwargs.pop('members')
		self._messages = kwargs.pop('messages')
		
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
		
	@property
	def members(self):
		"""ADD WHEN MEMBER CLASS IS MADE"""
		
	@property
	def messages(self):
		"""ADD WHEN MESSAGE CLASS IS MADE"""
		
		
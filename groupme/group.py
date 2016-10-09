from .object import Object
from .member import Member
from .message import Preview

class Group(Object):
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
	count : int
		Number of messages sent in group
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
	members : list
		List of :class:`Member`
	messages : ???
		??? (TO BE FINAL LATER)
	name : str
		The name of the group
	office_mode : bool
		When the group is in office mode or not
	phone_number : str
		The phone number of the group
	preview : :class:`Preview`
		The last message sent in the group. The preview doesn't have as much
		information as a full :class:`Message` but is similar.
	share_url : str
		URL to join the group, can be none if private
	type : str
		Whether the group is public or private
	updated_at : int
		Unix time-stamp of when the group was updated last	
	"""
	__slots__ = [
		'count', 'created_at', 'description', 'image_url', 'id', 'max_members',
		'members', 'messages', 'name', 'office_mode',
		'phone_number', 'preview' 'share_url', 'type', 'updated_at'
		]
	
	def __init__(self, **kwargs):
		
		super(Group, self).__init__(**kwargs)
		
		_members = kwargs.pop('members')
		_messages = kwargs.pop('messages')
	
		self.count = _messages.pop('count')
		self.created_at = kwargs.pop('created_at')
		self.description = kwargs.pop('description')
		self.image_url = kwargs.pop('image_url')
		self.max_members = kwargs.pop('max_members')
		self.members = self._get_members(_members)
		self.name = kwargs.pop('name')
		self.office_mode = kwargs.pop('office_mode')
		self.phone_number = kwargs.pop('phone_number')
		self.preview = Preview(**_messages['preview'],
						id=_messages['last_message_id']),
						created_at=_messages['last_message_created_at']
		self.share_url = kwargs.pop('share_url')
		self.type = kwargs.pop('type')
		self.updated_at = kwargs.pop('updated_at')
		
	def _get_members(self, member_list):
		"""Makes a list of member objects"""
		members = []
		for member in member_list:
			member = Member(**member)
			members.append(member)
		return members

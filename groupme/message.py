from .object import Object
from .member import Member

class Base(Object):
	"""Base object for message-esque objects"""
	
	__slots__ = []
	
	def __init__(self, **kwargs):
		super(Preview, self).__init__(**kwargs)
		
		self.attachments = self._attachments(kwargs.pop['attachments'])
		self.author = kwargs.pop('nickname')
		self.created_at = kwargs.pop('created_at')
		self.text = kwargs.pop('text')
	
	def __str__(self):
		return self.text

class Preview(Base):
	"""Represents :class:`Group` message previews
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two previews are equal.    |
	+-----------+--------------------------------------+
	| x != y    | Checks if two previews are not equal.|
	+-----------+--------------------------------------+
	| hash(x)   | Returns the preview's hash.          |
	+-----------+--------------------------------------+
	| str(x)    | Returns the preview's text.          |
	+-----------+--------------------------------------+
	
	Attributes
	----------
	attachments : list
		A list of attachments
	author : str
		The name of the author
	author_image : str
		URL to the author's image_url
	created_at : int
		Unix time-stamp when the preview was created
	text : str
		The preview's contents
	"""
	
	__slots__ = ['attachments', 'author', 'author_image', 'created_at', 'text']
	
	def __init__(self, **kwargs):
		super(Preview, self).__init__(**kwargs)
		
		self.author_image = kwargs.pop('author_image')

class Message(Base):
	"""Represents Group Me messages
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two messages are equal.    |
	+-----------+--------------------------------------+
	| x != y    | Checks if two messages are not equal.|
	+-----------+--------------------------------------+
	| hash(x)   | Returns the message's hash.          |
	+-----------+--------------------------------------+
	| str(x)    | Returns the message's text.          |
	+-----------+--------------------------------------+
	
	Attributes
	----------
	attachments : list
		A list of attachments
	author : str
		The name of the author
	created_at : int
		Unix time-stamp when the message was created
	text : str
		The Message's contents
	"""
	
	__slots__ = ['attachments', 'author', 'created_at', 'text']
	
	def __init__(self, **kwargs):
		super(Message, self).__init__(**kwargs)
		
		author_id = kwargs.pop('user_id')
		author_name = kwargs.pop('name')
		author_avatar = kwargs.pop('avatar_url')
		
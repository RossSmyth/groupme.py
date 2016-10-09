from .object import Object

class Preview(Object):
	"""The class for :class:`Group` message previews
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two previews are equal.    |
	+-----------+--------------------------------------+
	| x != y    | Checks if two previews are not equal.|
	+-----------+--------------------------------------+
	| hash(x)   | Returns the previews's hash.         |
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
	"""
	def __init__(self, **kwargs):
		super(Preview, self).__init__(**kwargs)
		
		self.attachments = self._attachments(kwargs.pop['attachments'])
		self.author = kwargs.pop('nickname')
		self.author_image = kwargs.pop('image_url')
		self.created_at = kwargs.pop('created_at')
		self.text = kwargs.pop('text')
	
	def __str__(self):
		return self.text

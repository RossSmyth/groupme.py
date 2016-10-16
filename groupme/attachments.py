
class Base:
    """Represents a base Group Me attachment"""

    __slots__ = []

    def __init__(self, **kwargs):
        self.type = kwargs.pop('type')

class Emoji(Base):
    """Represents a Group Me emoji attachment

    Supported Operations:

    +-----------+---------------------------------------+
	| Operation |             Description               |
	+===========+=======================================+
	| x == y    | Checks if two emojis are equal.       |
	+-----------+---------------------------------------+
	| x != y    | Checks if two emojis are not equal.   |
	+-----------+---------------------------------------+
	| str(x)    | Returns the emojis.                   |
	+-----------+---------------------------------------+

	Attributes
	----------
	charmap : list
        A list of the emojis in a message, and their positions in the Group Me character map
    placeholder : str
        A Unicode character that hold the place of an emoji
    type : str
        The type of the attachment
	"""

    __slots__ = [
                'charmap', 'placeholder', 'type'
                ]

    def __init__(self, **kwargs):
        super(Emoji, self).__init__(**kwargs)

        self.placeholder = kwargs.pop('placeholder')
        self.charmap = kwargs.pop('charmap')

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.charmap == other.charmap

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.charmap != other.charmap
        return True

    def __str__(self):
        """MAKE WHEN CHARMAPS ARE FIGURED OUT"""

class Image:
    """Represents a Group Me image

    Supported Operations:

    +-----------+---------------------------------------+
	| Operation |             Description               |
	+===========+=======================================+
	| x == y    | Checks if two imaages are equal.      |
	+-----------+---------------------------------------+
	| x != y    | Checks if two imagess are not equal.  |
	+-----------+---------------------------------------+
	| hash(x)   | Returns the image's hash              |
	+-----------+---------------------------------------+
	| str(x)    | Returns the image's URL.              |
	+-----------+---------------------------------------+

	Attributes
	----------
    type : str
        The type of the attachment
    url : str
        The URL of the image
	"""

    __slots__ = [
                'type', 'url'
                ]

    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)

        self.url = kwargs.pop('url')

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.url == other.url

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.url != other.url
        return True

    def __hash__(self):
        return hash(self.url)

    def __str__(self):
        return self.url


class Location(Base):
    """Represents a Group Me location attachment

    Supported Operations:

    +-----------+---------------------------------------+
	| Operation |             Description               |
	+===========+=======================================+
	| x == y    | Checks if two locations are equal.    |
	+-----------+---------------------------------------+
	| x != y    | Checks if two locations are not equal.|
	+-----------+---------------------------------------+
	| hash(x)   | Returns the location's hash.          |
	+-----------+---------------------------------------+
	| str(x)    | Returns the location's name.          |
	+-----------+---------------------------------------+

	Attributes
	----------
	lat : str
	    The latitude of the location
	lgn : str
	    The longitude of the location
	name : str
	    The name of the location
	type : str
	    The type of the attachment
	"""

    __slots__ = [
                'lat', 'lgn', 'name', 'type'
                ]

    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)

        self.name = kwargs.pop('name')

        self.lat = kwargs.pop('lat')
        self.lng = kwargs.pop('lgn')

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.lat == other.lat and self.lng == other.lng

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.lat != other.lat or self.lng != other.lng
        return True

    def __hash__(self):
        hash(self.lat + self.lng)

    def __str__(self):
        return '{0.lng} degrees longitude, {0.lat} degrees latitude'.format(self)

class Split(Base):
    """Represents a Group Me check split

    Supported Operations:

    +-----------+---------------------------------------+
	| Operation |             Description               |
	+===========+=======================================+
	| x == y    | Checks if two splits are equal.       |
	+-----------+---------------------------------------+
	| x != y    | Checks if two splits are not equal.   |
	+-----------+---------------------------------------+
	| hash(x)   | Returns the split's hash              |
	+-----------+---------------------------------------+

	Attributes
	----------
	token : str
        The split token
    type : str
        The type of the attachment
	"""

    __slots__ = [
                'token', 'type'
                ]

    def __init__(self, **kwargs):
        super(Split, self).__init__(**kwargs)

        self.token = kwargs.pop('token')

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.token == other.token

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.token != other.token
        return True

    def __hash__(self):
        return hash(self.token)

import unittest
import sys
import json

sys.path.append("D:\\Libraries\\Documents\GitHub\\groupme.py\\")

import groupme

class message_test(unittest.TestCase):
	
	def setUp(self):
		with open('test_message.txt') as test:
			example_json = json.load(test)['message']
	
		self.example_message_object = groupme.Message(**example_json)
	
	def test_message_text(self):
		self.assertEqual(self.example_message_object.text,
		"Kira would probably love to write something. Any ideas?")
	
	def test_message_created_at(self):
		self.assertEqual(self.example_message_object.created_at, 1475455189)
	
	def test_message_author_name(self):
		self.assertEqual(self.example_message_object.author.name, "Kira Frahm")
	
	def test_author_id(self):
		self.assertEqual(self.example_message_object.author.id, "30506935")
	
	def test_message_author_image_url(self):
		self.assertEqual(self.example_message_object.author.image_url,
						"https://i.groupme.com/sms_avatar")
	
	def test_message_source_guid(self):
		self.assertEqual(self.example_message_object.source_guid, 
						"d069c0c0-6b2f-0134-027f-22000b430990-0")
	
	def test_message_id(self):
		self.assertEqual(self.example_message_object.id, "147545518935507575")
	
	def test_message_attachments(self):
		self.assertEqual(self.example_message_object.attachments, [])
	
	def test_message_favorited_by(self):
		self.assertEqual(self.example_message_object.favorited_by, [])
	
	def test_message_group(self):
		self.assertEqual(self.example_message_object.group, "25081074")

	def test_message_is_system(self):
		self.assertEqual(self.example_message_object.is_system, False)

if __name__ == '__main__':
	unittest.main()

import unittest
import sys
import json

sys.path.append("D:\\Libraries\\Documents\GitHub\\groupme.py\\")

import groupme


class group_test(unittest.TestCase):

    def setUp(self):

        with open('test.txt') as test:

            example_json = json.load(test)['response']

        self.example_group_object = groupme.Group(**example_json)

    def test_group_count(self):

        self.assertEqual(self.example_group_object.count, 41)

    def test_group_created_at(self):

        self.assertEqual(self.example_group_object.created_at, 1474202308)

    def test_group_description(self):

        self.assertEqual(self.example_group_object.description, '')

    def test_group_image_url(self):

        self.assertEqual(self.example_group_object.image_url,
        'https://i.groupme.com/214x214.jpeg.51228d02319a4ed9abfa3f2cd7b2d1a6')

    def test_group_id(self):

        self.assertEqual(self.example_group_object.id, '25081074')

    def test_group_max_members(self):

        self.assertEqual(self.example_group_object.max_members, 200)

    def test_group_name(self):

        self.assertEqual(self.example_group_object.name, "Bleu Print '16-'17")

    def test_group_office_mode(self):

        self.assertEqual(self.example_group_object.office_mode, False)

    def test_group_phone_number(self):

        self.assertEqual(self.example_group_object.phone_number,
                         '+1 9165208970')

    def test_group_preview_attachments(self):

        self.assertEqual(self.example_group_object.preview.attachments, [])

    def test_group_preview_author(self):

        self.assertEqual(self.example_group_object.preview.author,
                         'Julia Van Goor')

    def test_group_preview_author_image(self):

        self.assertEqual(self.example_group_object.preview.author_image,
        'https://i.groupme.com/638x638.jpeg.035a2f4a4d8d4ebf970fc69524dc3f5f')

    def test_group_preview_created_at(self):

        self.assertEqual(self.example_group_object.preview.created_at,
                         1475784598)

    def test_group_preview_id(self):

        self.assertEqual(self.example_group_object.preview.id,
                         '147578459817776012')

    def test_group_preview_text(self):

        self.assertEqual(self.example_group_object.preview.text,
                         'My email is 7vangooj@chelsea.k12.mi.us')

    def test_group_share_url(self):

        self.assertEqual(self.example_group_object.share_url, None)

    def test_group_type(self):

        self.assertEqual(self.example_group_object.type, 'private')

    def test_group_updated_at(self):

        self.assertEqual(self.example_group_object.updated_at, 1475784598)

if __name__ == '__main__':
    unittest.main()
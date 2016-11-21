import unittest
import tag


class ParserTests(unittest.TestCase):
    def test_1(self):
        s = "a#enter.knob.green a#enter a#enter"
        tag1 = tag.Tag("a", "enter", {"knob", "green"})
        tag2 = tag.Tag("a", "enter", set())
        tag3 = tag.Tag("a", "enter", set())
        expected = [tag1, tag2, tag3]

        self.assertEqual(tag.parse_hierarchy(s), expected)

    def test_2(self):
        s = "id img.photo.bw a#enter.btn.share.link"
        tag1 = tag.Tag("id", None, set())
        tag2 = tag.Tag("img", None, {"photo", "bw"})
        tag3 = tag.Tag("a", "enter", {"btn", "share", "link"})
        expected = [tag1, tag2, tag3]

        self.assertEqual(tag.parse_hierarchy(s), expected)

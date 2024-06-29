import unittest
from markdown_converter import convert_markdown_to_html, convert_markdown_to_ansi

class TestMarkdownConverter(unittest.TestCase):
    
    def test_bold_conversion_html(self):
        self.assertEqual(convert_markdown_to_html('**bold**'), '<b>bold</b>')
    
    def test_italic_conversion_html(self):
        self.assertEqual(convert_markdown_to_html('_italic_'), '<i>italic</i>')
    
    def test_monospaced_conversion_html(self):
        self.assertEqual(convert_markdown_to_html('`code`'), '<tt>code</tt>')
    
    def test_preformatted_conversion_html(self):
        self.assertEqual(convert_markdown_to_html('```\npreformatted\n```'), '<pre>\npreformatted\n</pre>')
    
    def test_bold_conversion_ansi(self):
        self.assertEqual(convert_markdown_to_ansi('**bold**'), '\033[1mbold\033[0m')
    
    def test_italic_conversion_ansi(self):
        self.assertEqual(convert_markdown_to_ansi('_italic_'), '\033[3mitalic\033[0m')
    
    def test_monospaced_conversion_ansi(self):
        self.assertEqual(convert_markdown_to_ansi('`code`'), '\033[7mcode\033[0m')
    
    def test_preformatted_conversion_ansi(self):
        self.assertEqual(convert_markdown_to_ansi('```\npreformatted\n```'), '\033[7m\npreformatted\n\033[0m')

if __name__ == '__main__':
    unittest.main()

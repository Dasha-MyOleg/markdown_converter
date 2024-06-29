import sys
import os
import re

def convert_markdown_to_html(markdown_text):
    # Обробка преформатованого тексту
    markdown_text = re.sub(r'```([\s\S]*?)```', r'<pre>\1</pre>', markdown_text)
    # Обробка жирного тексту
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_text)
    # Обробка курсивного тексту
    markdown_text = re.sub(r'_(.*?)_', r'<i>\1</i>', markdown_text)
    # Обробка моноширинного тексту
    markdown_text = re.sub(r'`(.*?)`', r'<tt>\1</tt>', markdown_text)
    return markdown_text

def convert_markdown_to_ansi(markdown_text):
    # Обробка преформатованого тексту
    markdown_text = re.sub(r'```([\s\S]*?)```', r'\033[7m\1\033[0m', markdown_text)
    # Обробка жирного тексту
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'\033[1m\1\033[0m', markdown_text)
    # Обробка курсивного тексту
    markdown_text = re.sub(r'_(.*?)_', r'\033[3m\1\033[0m', markdown_text)
    # Обробка моноширинного тексту
    markdown_text = re.sub(r'`(.*?)`', r'\033[7m\1\033[0m', markdown_text)
    return markdown_text

def main(input_file, output_file=None, format_type="html"):
    try:
        with open(input_file, 'r') as file:
            markdown_text = file.read()
        
        if format_type == "html":
            output_text = convert_markdown_to_html(markdown_text)
        elif format_type == "ansi":
            output_text = convert_markdown_to_ansi(markdown_text)
        else:
            raise ValueError("Unsupported format type")
        
        if output_file:
            output_dir = os.path.dirname(output_file)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            with open(output_file, 'w') as file:
                file.write(output_text)
            print(f"Output has been written to {output_file}")
        else:
            print(output_text)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python markdown_converter.py <input_file> [--out <output_file>] [--format <format_type>]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = None
    format_type = "html"
    if "--out" in sys.argv:
        output_file = sys.argv[sys.argv.index("--out") + 1]
    if "--format" in sys.argv:
        format_type = sys.argv[sys.argv.index("--format") + 1]
    
    main(input_file, output_file, format_type)

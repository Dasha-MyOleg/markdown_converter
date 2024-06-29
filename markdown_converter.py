import sys
import os

print("Starting the script")  # Додано для перевірки виконання скрипта

def convert_markdown_to_html(markdown_text):
    html_text = markdown_text.replace("**", "<b>").replace("**", "</b>")
    html_text = html_text.replace("_", "<i>").replace("_", "</i>")
    html_text = html_text.replace("`", "<tt>").replace("`", "</tt>")
    html_text = html_text.replace("```", "<pre>").replace("```", "</pre>")
    return html_text

def main(input_file, output_file=None):
    try:
        print(f"Reading input file: {input_file}")
        with open(input_file, 'r') as file:
            markdown_text = file.read()
        
        print("Converting Markdown to HTML")
        html_text = convert_markdown_to_html(markdown_text)
        
        if output_file:
            output_dir = os.path.dirname(output_file)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            print(f"Writing HTML output to: {output_file}")
            with open(output_file, 'w') as file:
                file.write(html_text)
            print(f"HTML output has been written to {output_file}")
        else:
            print(html_text)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    print("Script started with arguments:", sys.argv)  # Додано для перевірки аргументів
    if len(sys.argv) < 2:
        print("Usage: python markdown_converter.py <input_file> [--out <output_file>]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = None
    if len(sys.argv) > 2 and sys.argv[2] == "--out":
        output_file = sys.argv[3]
        output_file = os.path.join('C:\\Users\\Даша\\markdown_converter\\markdown_converter', output_file)
        print(f"Full path for output file: {output_file}")
    
    print(f"Running script with input_file: {input_file} and output_file: {output_file}")
    main(input_file, output_file)

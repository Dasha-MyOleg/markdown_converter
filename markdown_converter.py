import sys
import os

# Додано для перевірки виконання скрипта
print("Starting the script")

def convert_markdown_to_html(markdown_text):
    # Замінюємо подвійні зірочки на тег <b> для жирного тексту
    html_text = markdown_text.replace("**", "<b>").replace("**", "</b>")
    # Замінюємо нижні підкреслення на тег <i> для курсивного тексту
    html_text = html_text.replace("_", "<i>").replace("_", "</i>")
    # Замінюємо бектики на тег <tt> для моноширинного тексту
    html_text = html_text.replace("`", "<tt>").replace("`", "</tt>")
    # Замінюємо потрійні бектики на тег <pre> для попередньо відформатованого тексту
    html_text = html_text.replace("```", "<pre>").replace("```", "</pre>")
    return html_text

def main(input_file, output_file=None):

    try:# Повідомлення про зчитування вхідного файлу
        print(f"Reading input file: {input_file}")  
        with open(input_file, 'r') as file:
            markdown_text = file.read()
        
        # Повідомлення про початок конвертації
        print("Converting Markdown to HTML")  
        html_text = convert_markdown_to_html(markdown_text)
        
        if output_file:
            output_dir = os.path.dirname(output_file)
            if not os.path.exists(output_dir):
                # Створюємо директорію для вихідного файлу, якщо її не існує
                os.makedirs(output_dir)  
            # Повідомлення про запис вихідного файлу
            print(f"Writing HTML output to: {output_file}")  
            with open(output_file, 'w') as file:
                file.write(html_text)
            # Підтвердження успішного запису файлу
            print(f"HTML output has been written to {output_file}")  
        else:
            # Виводимо HTML текст у консоль
            print(html_text)  
    
    except Exception as e:
        # Виводимо повідомлення про помилку
        print(f"Error: {e}", file=sys.stderr)  
        sys.exit(1)

if __name__ == "__main__":
    # Додано для перевірки аргументів
    print("Script started with arguments:", sys.argv)  
    if len(sys.argv) < 2:
        print("Usage: python markdown_converter.py <input_file> [--out <output_file>]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = None
    if len(sys.argv) > 2 and sys.argv[2] == "--out":
        output_file = sys.argv[3]
        output_file = os.path.join('C:\\Users\\Даша\\markdown_converter\\markdown_converter', output_file)
        # Повне ім'я вихідного файлу
        print(f"Full path for output file: {output_file}")  
    
    # Інформація про запущений скрипт
    print(f"Running script with input_file: {input_file} and output_file: {output_file}")  
    main(input_file, output_file)

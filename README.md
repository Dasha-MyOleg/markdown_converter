# Markdown Converter

## Опис
Цей проект конвертує файли Markdown у HTML та ANSI форматування.

## Лабораторна робота 1

### Інструкція з установки
1. Клонуйте репозиторій: `git clone https://github.com/Dasha-MyOleg/markdown_converter.git`
2. Перейдіть до каталогу проекту: `cd markdown_converter`

### Інструкція з використання
1. Запустіть скрипт: `python markdown_converter.py input.md --out output.html`




## Лабораторна робота 2

### Модифікації
1. Додана можливість вибору формату виводу через прапорець командного рядка `--format=value`.
2. Додано виведення відформатованого тексту у стандартний вивід з використанням ANSI Escape Codes.
3. Додано підтримку моноширинного та преформатованого тексту у інвертованому режимі (inverse/reverse mode).

### Інструкція з використання
1. Запустіть скрипт з вибором формату: `python markdown_converter.py <input_file> [--out <output_file>] [--format <format_type>]`
   Наприклад: python markdown_converter.py input.md --format html --out output.html
2. Доступні формати: `html`, `ansi`.

### Інструкція по запуску тестів
1. Створіть і активуйте віртуальне середовище:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Для Windows
   source venv/bin/activate  # Для Unix

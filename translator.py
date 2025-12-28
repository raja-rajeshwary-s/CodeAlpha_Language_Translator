# CodeAlpha Task 1: Language Translation Tool
# Simple & beginner-friendly version

from googletrans import Translator

def translate_text():
    translator = Translator()

    print("Language Translator")
    print("-------------------")

    text = input("Enter text to translate: ")
    source_lang = input("Enter source language code (ex: en, ta, hi): ")
    target_lang = input("Enter target language code (ex: en, ta, hi): ")

    try:
        result = translator.translate(
            text,
            src=source_lang,
            dest=target_lang
        )

        print("\nTranslated Text:")
        print(result.text)

    except Exception as e:
        print("Error:", e)

# Run the function
translate_text()

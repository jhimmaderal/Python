from googletrans import Translator


def translate_to_arabic(text):
    translator = Translator()
    translation = translator.translate(text, dest="ar")
    return translation.text


def main():
    # Input text to be translated
    input_text = input("Enter text to translate to Arabic: ")

    # Translate the text to Arabic
    translated_text = translate_to_arabic(input_text)

    # Display the translated text
    print("\nTranslated to Arabic:")
    print(translated_text)


if __name__ == "__main__":
    main()

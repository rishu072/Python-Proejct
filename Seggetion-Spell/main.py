from spellchecker import SpellChecker

class SpellCheckApp:

    def __init__(self):
        # Create spell checker object
        self.spell = SpellChecker()

    def correct_text(self, text):
        # Split the entered text into words
        words = text.split()

        corrected_words = []

        for word in words:

            # Find the correct spelling
            corrected_word = self.spell.correction(word)

            # If no correction is found, keep the original word
            if corrected_word is None:
                corrected_word = word

            # Show the correction if the word was changed
            if corrected_word != word.lower():
                print(f"Corrected '{word}' to '{corrected_word}'")

            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)

    def run(self):

        print("\n-------- Spell Checker --------")

        while True:

            text = input("Enter text to check spelling (or type 'exit' to quit): ")

            if text.lower() == 'exit':

                print("Exiting Spell Checker App.")
                break

            corrected_text = self.correct_text(text)

            print(f"Corrected Text: {corrected_text}")


if __name__ == "__main__":
    SpellCheckApp().run()
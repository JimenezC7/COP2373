import re

# This function finds and returns all complete sentences from
# paragraph entered by user.

def get_sentences(paragraph):
    'Find and return all sentences in the paragraph.'

    pattern = r"[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)"
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    return sentences

# Displays each sentence found in paragraph then prints total number
# of sentences.

def display_sentences(sentences):
    'Display each sentence and the total sentence count.'

    print("\nSentences found:")

    for sentence in sentences:
        print("->", sentence.strip())

    print("\nTotal sentences:", len(sentences))


def main():
    'Get paragraph input from the user and display sentence results.'

    paragraph = input("Enter a paragraph: ")

    sentences = get_sentences(paragraph)

    display_sentences(sentences)


if __name__ == "__main__":
    main()

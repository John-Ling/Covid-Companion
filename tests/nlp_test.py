from nltk.tokenize import sent_tokenize, word_tokenize

def main():
    EXCERPT = """It was a bright cold day in April, and the clocks were striking thirteen.
        Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."""

    words = word_tokenize(EXCERPT)
    for word in words:
        print(word)

if __name__ == "__main__":
    main()
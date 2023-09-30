def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_count = len(words)
    print("The sentence contains", word_count, "words.")

count_words()

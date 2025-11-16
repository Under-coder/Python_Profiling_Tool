import re
import os
import codeoptimizex as co


def extract_emails(filename):
    # Inefficient: reads the file every time called
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    emails = []
    email_pattern = r"\w{1,20}@\w{1,10}\.\w{1,5}"
    emails = re.findall(email_pattern, text)

    # Manual nested loops to count emails (O(n^2))
    email_counts = {}
    for email in emails:
        count = 0
        for e in emails:
            if e == email:
                count += 1
        email_counts[email] = count

    return email_counts


def extract_words(filename):
    # Inefficient: reads the file every time called
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())

    # Manual nested loops to count words (O(n^2))
    word_counts = {}
    for word in words:
        count = 0
        for w in words:
            if w == word:
                count += 1
        word_counts[word] = count

    # Remove stopwords after counting (extra looping)
    stopwords = set([
        'the', 'and', 'to', 'of', 'a', 'in', 'for', 'is', 'on', 'that', 'with', 'as', 'at', 'by', 'an', 'be', 'this', 'or', 'from', 'it',
        'are', 'was', 'but', 'not'
    ])
    filtered_word_counts = {}
    for word, count in word_counts.items():
        if word not in stopwords:
            filtered_word_counts[word] = count

    return filtered_word_counts


def main():
    filename = 'sample.txt'  # Change this to your actual file path

    email_counts = extract_emails(filename)
    word_counts = extract_words(filename)

    print("Top 10 email addresses:")
    for email, count in sorted(email_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
        print(f"{email}: {count}")

    print("\nTop 10 words:")
    for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
        print(f"{word}: {count}")


if __name__ == '__main__':
    main()

co.profile_function(main)
co.save_profile(main, "optimized_profile.prof")
import re
from collections import Counter
import codeoptimizex as co

def extract_emails(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    email_pattern = re.compile(r"\w{1,20}@\w{1,10}\.\w{1,5}")
    emails = email_pattern.findall(text)

    email_counts = Counter(emails)
    return dict(email_counts)

def extract_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())

    stopwords = {
        'the', 'and', 'to', 'of', 'a', 'in', 'for', 'is', 'on', 'that',
        'with', 'as', 'at', 'by', 'an', 'be', 'this', 'or', 'from',
        'it', 'are', 'was', 'but', 'not'
    }

    filtered_words = (word for word in words if word not in stopwords)
    word_counts = Counter(filtered_words)

    return dict(word_counts)

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
    co.profile_function(main)
    co.save_profile(main, "optimized_profile.prof")

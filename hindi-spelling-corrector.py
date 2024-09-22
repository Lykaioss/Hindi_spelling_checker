import re
from collections import Counter

def load_hindi_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file)

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]

def get_word_freq(words):
    return Counter(words)

def correct_spelling(word, hindi_words, word_freq):
    if word in hindi_words:
        return word
    
    candidates = [w for w in hindi_words if edit_distance(word, w) <= 2]
    if not candidates:
        return word
    
    return max(candidates, key=lambda w: word_freq[w])

# Main function
def main():
    
    hindi_words = load_hindi_words('hindi-words-list.txt')
    word_freq = get_word_freq(hindi_words)
    
    
    test_words = ["आम", "अम", "भारत", "भरत", "विद्यालय", "वद्यालय"]
    
    for word in test_words:
        corrected = correct_spelling(word, hindi_words, word_freq)
        print(f"Original: {word}, Corrected: {corrected}")

if __name__ == "__main__":
    main()

# Given a string 'paragraph' and a string array of the banned words 'banned', return the most frequent word that is not banned. It is guaranteed there is at least one word
# that is not banned, and that the answer is unique. 

# The words in 'paragraph' are case-insensitive and the answer should be returned in lowercase. 

# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]

# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 

# Note that words in the paragraph are not case sensitive, that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"

class Solution:
  def most_common_word(self, paragraph: str, banned: List[str]) -> str:
    words = []
    word = ""
    for i in range(len(paragraph)):
      if paragraph[i] in "!?',;.":
        if word:
          words.append(word)
          word = ""
      else: 
        word += paragraph[i]
    if word:
      words.append(word)
    return words







///
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def tokenize(paragraph):
            words = []
            word = ""
            for i in range(len(paragraph)):
                if paragraph[i] in " !?',;.":
                    if word:
                        words.append(word)
                        word = ""
                else:
                    word += paragraph[i]
            if word:
                words.append(word)
            return words

        words = tokenize(paragraph.lower())
        word_map = {}
        common_word = ("", 0)
        for word in words:
            if word in banned: continue
            word_map[word] = word_map.get(word, 0) + 1
            if (word_map[word] > common_word[1]):
                common_word = (word, word_map[word])
        return common_word[0]

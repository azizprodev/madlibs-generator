# get the story file and read it
with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# loop through story file 
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1

answers = {}

# loop through words set, and get answer from user
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

# loop through and replace word with ansewer word
for word in words:
    story = story.replace(word, answers[word])

print(story)
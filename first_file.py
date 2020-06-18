absolute_file_path="/home/kanan/Documents/python/files/robinson-chapter-i.txt"

with open(absolute_file_path,"r") as file:
    content=file.read()

print(f"The length of text is -> {len(content)}")
sum_element=0
content.replace("\n"," ")
for e in content:
    content.replace("!","")
    content.replace("?","")
    content.replace(".","")
    content.replace("-","")
    content.replace(",","")
    if e != " ":
        sum_element+=1

print(f"The number of elements in text is -> {sum_element}")

separate=content.split(" ")

words={}
for word in separate:
    words[word]=words.get(word,0) + 1

print(words)

print(f"Sum of words in text -> {sum(words.values())}")

max_word=0
keys=0
for key, value in words.items():
        if value>max_word:
            max_word = value
            keys = key

print(f'The most frequency word is -> {keys.upper()} : {max_word}')
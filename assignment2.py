sent=input("Enter your sentence\n")
sent=sent.lower()
vowels="aeiou"
count=0
while len(sent)>7:
    print(sent[7])
    print(len(sent))
    sentup=sent.title()
    print(sentup)
    print(sent[1:-1])
    print(sent.replace("a" ,"e"))
    for ch in sent:
     if ch in vowels:
        count=1 + count
    print(count)

    break
else:
    print("The sentence is too short")
    sent=input("Enter a sentence  with letters greater than 7\n")
    
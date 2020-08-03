def convert_to_wordlist(sentence):
    result = []
    wordlist = sentence.split(" ")
    for word in wordlist:
        if len(word) > 0:
            result.append(word.lower())
    return result

def sort_wordlist_by_len(wordlist):
    sorted_dic = {}
    for word in wordlist:
        if len(word) in sorted_dic.keys():
            sorted_dic[len(word)].append(word)
        else:
            new_change = {len(word): [word]}
            sorted_dic.update( new_change )
    return sorted_dic

sentence_input = raw_input("Enter a sentence: ")
wordlist = convert_to_wordlist(sentence_input)
sorted_wordlist = sort_wordlist_by_len(wordlist)

for key in sorted_wordlist:
    words = ''
    for word in sorted(sorted_wordlist[key]):
        words += ' ' + word
    print key, words

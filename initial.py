#English Poetry Appreciation using nlp
#first step tokenization

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

#taking file from the computer
def get_raw_text(filename):
    """give a file name set a raw text"""
    with open(filename,'r') as fin:
        raw_text=fin.read()
    return raw_text

#function for removing stopword from the poem
def stopwords_remove(sentence):
    stop_words = set(stopwords.words('english'))
    words = sentence.split()
    for r in words:
        r=r.lower()
        if not r in stop_words:
            appendFile = open('stopallwords.txt', 'a')
            appendFile.write(" " + r)
            appendFile.close()


#deleting the content of stopwords present in the file
def truncatefile(filename):
    """clear the content from the file"""
    f = open(filename, 'r+')
    f.truncate()


#tokenization of each stanza present in them poem
def tokenize_line(line_text):
    """Given a raw text that is a list  of lines produce the token"""
    sentence=nltk.sent_tokenize(line_text)
    return sentence


#tokenization of word after sentence tokenization
def tokenize_word(set_sentence):
    "word tokenization using the sentence above covered"
    wordlist = []
    for singleline in set_sentence:
        #below tokenization is a normal tokenization below two lines
        #words=nltk.word_tokenize(singleline)
        #wordlist.append(words)
        #this tokenization is a regular expression tokenizer
        tokenizer = RegexpTokenizer(r'\w+')
        words=tokenizer.tokenize(singleline)
        wordlist.append(words)

    return wordlist


#tagging of each word present in the list
def tagging(words):
    taglist = []
    for wordlist in words:
        tagg=nltk.pos_tag(wordlist)
        taglist.append(tagg)

    return  taglist



#lemmitization of the word which is pos tagg
def lemmitize_word(tagwords):
    wnl = WordNetLemmatizer()
    whole_tag_list=[]
    complete_lema_list=[]
    for l in tagwords:
        for a in l:
            whole_tag_list.append(a)

    for word,tag in whole_tag_list:
        wtag = tag[0].lower()
        wtag = wtag if wtag in ['a', 'r', 'n', 'v'] else None
        if not wtag:
            lemma = word
        else:
            lemma = wnl.lemmatize(word, wtag)

        complete_lema_list.append(lemma)

    return complete_lema_list

#this is the main function which is resonsible for this
def main():

    truncatefile('stopallwords.txt')
    filename="a.txt"
    print("\nThe data present in the file:")
    file=get_raw_text(filename)
    print(file)

    print("\nThe data after removing stopwords from file:")
    stopewords=stopwords_remove(file)
    filename='stopallwords.txt'
    file1 = get_raw_text(filename)
    print(file1)

    senttoken=tokenize_line(file1)
    print("\nThe sentence tokenization fo the poem sentences:")
    print(senttoken)

    wordtoken=tokenize_word(senttoken)
    print("\nThe word tokenization of sentence present in the poem:")
    print(wordtoken)

    tags=tagging(wordtoken)
    print("\nThe list of the tags present in the poem:\n")
    print(tags)

    #calling of lemmitize_word function
    lem=lemmitize_word(tags)
    print("\nLemmitization of the word give following result:")
    print(lem)


#calling of the main function
main()
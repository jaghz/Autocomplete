class TriePredict:
    def __init__(self):
        self.terminalPoint = False
        self.children = {}
        self.wordString = ''
        self.length = 0
    def insert(self, word, position=0):
        if position == len(word):
            self.terminalPoint = True
            self.wordString = word
            return
        self.length+=1
        if word[position] not in self.children:
            letterNode = TriePredict()
            self.children[word[position]] = letterNode
            letterNode.insert(word, position + 1)
        elif word[position] in self.children:
            letterNode = self.children[word[position]]
            letterNode.insert(word, position + 1)
    def exists(self, word, position=0):
        if position == len(word):
            return True
        if word[position] in self.children:
            letterNode = self.children[word[position]]
            return letterNode.exists(word, position + 1)
        else:
            return False

    def isTerminal(self):
        if self.terminalPoint == True:
            return True

    def predictWord(self, prefix, position=0, wordList=None):
        if position == 0:
            while position < len(prefix):
                if prefix[position] in self.children:
                    self = self.children[prefix[position]]
                    position +=1
                else:
                    return []
        if prefix is '':
            if wordList is None:
                wordList = []
            if self.wordString is not '' :
                wordList.append(self.wordString)
        else:
            if wordList is None:
                wordList = []
            if self.wordString is not '' and prefix[0] is self.wordString[0]:
                wordList.append(self.wordString)

        for ele in self.children:
            self.children[ele].predictWord(prefix, position, wordList)
        
        return wordList
   

    def __len__(self):
        return self.length


wordlist = []


while True:
    try:
        fileName = input("Enter name of text file (ensure .txt extension added): ")
        f = open(fileName)
        break
    except FileNotFoundError:
        print("File not found. Please ensure text file is in the same directory.")
    
print("Creating dictionary for " + fileName)
readWords = f.readlines()
for word in readWords:
    wordlist.append(word)
x = TriePredict()
for word in wordlist:
    x.insert(word)
print("Dictionary created.")
quit = False

def runProgram(prefix):
    print('''Words that begin with characters "''' + prefix + '''":''' )
    a = x.predictWord(prefix)
    for word in a:
        print(word)

while True:
    prefix = input("Enter a prefix (0 to quit): ")
    if prefix == '0':
        break
    else:
        runProgram(prefix)

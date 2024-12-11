import heapq

# SIMPLE OVERVIEW OF A HUFFMAN TREE:
# Have a map of a character and its frequency.
# Compare (starting at least frequent) two nodes. Have them point to a parent node.
# The parent node will contain the frequency and the two nodes below it.
# Every leaf will be some value node.
# Every inner node will be a combination of two other nodes.
# A leaf's node contains a character and its frequency. 
# For every left taken, add 0. Every right, add 1.

# Pair-Encoding:
# For any pair which is 'popular' (used more than once), we will encode it as its own 'symbol'.
# Encodes more spacially efficiently.

# Node class for our heap.
# Stores the character, its frequency, and its binary notation.
# Additionally had the child nodes.
class Node:
    def __init__(self, frequency, character, left=None, right=None):
        self.character = character;
        self.frequency = frequency;

        self.left = left;
        self.right = right;

        self.binary = '';
        
    def __lt__(self, otherNode):
        return self.frequency < otherNode.frequency;
    def __gt__(self, otherNode):
        return self.frequency > otherNode.frequency;

# Iterates through a heap starting at the first node in a tree.
# Prints all nodes and their values.
def printNodes(Node, previousValue=""):
    recurseValue = previousValue + str(Node.binary);
    if(Node.left): 
        printNodes(Node.left, recurseValue);
    if(Node.right): 
        printNodes(Node.right, recurseValue); 
    if(not Node.left and not Node.right): 
        print(Node.character,": ", recurseValue);

# Given a node, create a hashmap we can use to find our characters binary value in O(1).
# The process below is O(N), but only needs to be ran once.
def translateToBinary(Node):
    def createMap(Node, mapping, previousValue=""):
        recurseValue = previousValue + str(Node.binary);
        if(Node.left): 
            createMap(Node.left, mapping, recurseValue);
        if(Node.right): 
            createMap(Node.right, mapping, recurseValue); 
        if(not Node.left and not Node.right): 
            mapping[Node.character] = recurseValue;

    mapping = {}
    createMap(Node, mapping)
    return mapping;

# Given some string, we will create a heap of nodes and then compare them.
def createHuffman(text):
    HuffmanTree = []

    character = []
    frequency = [];
    
    charsAndFreqs = findFrequenciesPair(text)

    for key in charsAndFreqs.keys():
        character.append(key)
        frequency.append(charsAndFreqs[key])
    

    for i in range(len(character)):
        heapq.heappush(HuffmanTree, Node(frequency[i], character[i]));

    while (len(HuffmanTree) > 1):

        leftNode = heapq.heappop(HuffmanTree);
        rightNode = heapq.heappop(HuffmanTree);

        leftNode.binary = 0;
        rightNode.binary = 1;

        newNode = Node(leftNode.frequency + rightNode.frequency, leftNode.character + rightNode.character, leftNode, rightNode);
        heapq.heappush(HuffmanTree, newNode);

    translationMap = translateToBinary(HuffmanTree[0])
    # print(translationMap)
    file = open('huffmanEncodingP.txt', "w")
    file.write('');

    encoded = '';

    writeTo = open('huffmanEncodingP.txt','a');
    skip = False;
    text = text + ' ';
    for i in range(0, len(text) - 1):
        if skip:
            skip = False;
            continue;
        pair = text[i] + text[i + 1]
        char = text[i]
        if pair in translationMap:
            writeTo.write(translationMap[pair] + "")
            skip = True;
            continue;
        if char in translationMap:
            writeTo.write(translationMap[char] + "")
            pass

# We will iterate through the text and determine which characters are the most popular.
def findFrequenciesPair(text):
    mapping = {}
    for i in range(1, len(text)):
        char = text[i];
        pair = text[i - 1] + char
        if not pair in mapping:
            mapping[pair] = 1;
        else:
            mapping[pair] = mapping[pair]+ 1;

    returnKey = "";
    for key in mapping.keys():
        returnKey = returnKey + " '" + key + "'" + ": " + str(mapping[key])

    swapped = {}
    for keys in mapping.keys():
        swapped[mapping[keys]] = keys

    s = list(mapping.values())
    s.sort()
    sd = {i: swapped[i] for i in reversed(s)}

    file = open('huffmanKeyP.txt', "w")
    for keys in sd.keys():
        mapping[sd[keys]] = keys
    
    toReturn = {};
    i = 0;
    for keys in mapping:
        if mapping[keys] < 2:
            continue;
        toReturn[keys] = mapping[keys]
        i = i + 1

    nums = 0;
    for i in range(0, len(text)):
        nums = nums + 1;
        char = text[i];
        if not char in toReturn:
            toReturn[char] = 1;
        else:
            toReturn[char] = toReturn[char]+ 1;
    for keys in toReturn:
        toReturn[keys] = toReturn[keys] / (nums + 10)
    file.write(str(toReturn));

    # Our key
    return toReturn;

# Main method.
def main(sampleFile):

    asString = open(sampleFile, 'r').read().replace('\n','')
    createHuffman(asString)
    byteCount = open('huffmanEncodingP.txt', 'r').read();
    bytes = 0;
    for byte in byteCount:
        bytes = bytes + 1;
    print(bytes, " bytes")
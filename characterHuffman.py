import heapq

# SIMPLE OVERVIEW OF A HUFFMAN TREE:
# Have a map of a character and its frequency.
# Compare (starting at least frequent) two nodes. Have them point to a parent node.
# The parent node will contain the frequency and the two nodes below it.
# Every leaf will be some value node.
# Every inner node will be a combination of two other nodes.
# A leaf's node contains a character and its frequency. 
# For every left taken, add 0. Every right, add 1.


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
    # Reached the end, print out the directions we took. 
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
    # print(mapping)
    return mapping;

# Given some string, we will create a heap of nodes and then compare them.
def createHuffman(text):
    HuffmanTree = []

    character = []
    frequency = [];
    
    charsAndFreqs = findFrequencies(text)

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
    # We will print the encoded text to the following file.
    file = open('huffmanEncoding.txt', "w")
    file.write('');

    writeTo = open('huffmanEncoding.txt','a');
    for char in text:
        writeTo.write(translationMap[char])

# We will iterate through the text and determine which characters are the most popular.
def findFrequencies(text):
    charNum = 0;
    mapping = {}
    for char in text:
        charNum = charNum + 1;
        if not char in mapping:
            mapping[char] = 1;
        else:
            mapping[char] = mapping[char]+ 1;

    for char in mapping:
        mapping[char] = mapping[char] / charNum;
    
    returnKey = "";
    for key in mapping.keys():
        returnKey = returnKey + " '" + key + "'" + ": " + str(mapping[key])
    # We will write our key (Characters and their frequency) to the following file.
    file = open('huffmanKey.txt', "w")
    file.write(returnKey);
    # Our key
    return mapping;

# Main method.
def main(sampleFile):

    asString = open(sampleFile, 'r').read().replace('\n','')
    createHuffman(asString)

    byteCount = open('huffmanEncoding.txt', 'r').read();
    bytes = 0;
    for byte in byteCount:
        bytes = bytes + 1;
    print(bytes, " bytes")

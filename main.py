def asciiSize(fileName):
    file = open(fileName).read()
    bytes = 0;
    for char in file:
        bytes = bytes + 8;
    return bytes;

import characterHuffman
import letterPairHuffman

fileName = input("What file would you like to encode? : ")

print("\n\nRegular Huffman Encoding: ")
characterHuffman.main(fileName)

print("Pair Huffman Encoding: ")
letterPairHuffman.main(fileName)

print('\nHuffman Encodings (translations, keys) have been printed to files in the directory.\n\n')

print("ASCII Encoding Size: ")
print(asciiSize(fileName))
import heapq
import pickle
import os
from collections import Counter
from typing import Dict, Tuple, Optional


class HuffmanNode:
    """Node class for Huffman Tree"""
    
    def __init__(self, char: Optional[str] = None, freq: int = 0, 
                 left: Optional['HuffmanNode'] = None, right: Optional['HuffmanNode'] = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    """Huffman Coding implementation for lossless text compression"""
    
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
    
    def frequency_analysis(self, text: str) -> Dict[str, int]:
        """Analyze frequency distribution of characters in text"""
        return dict(Counter(text))
    
    def build_heap(self, frequency: Dict[str, int]):
        """Build priority queue (min-heap) from frequency dictionary"""
        self.heap = []
        for char, freq in frequency.items():
            node = HuffmanNode(char=char, freq=freq)
            heapq.heappush(self.heap, node)
    
    def merge_nodes(self):
        """Build Huffman Tree by merging nodes"""
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            
            merged = HuffmanNode(
                freq=node1.freq + node2.freq,
                left=node1,
                right=node2
            )
            
            heapq.heappush(self.heap, merged)
    
    def generate_codes_helper(self, node: HuffmanNode, current_code: str):
        """Recursively generate Huffman codes"""
        if node is None:
            return
        
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return
        
        self.generate_codes_helper(node.left, current_code + "0")
        self.generate_codes_helper(node.right, current_code + "1")
    
    def generate_codes(self):
        """Generate prefix codes for each character"""
        root = self.heap[0]  # Get root without popping
        current_code = ""
        self.generate_codes_helper(root, current_code)
    
    def build_huffman_tree(self, text: str):
        """Complete process to build Huffman tree and generate codes"""
        frequency = self.frequency_analysis(text)
        self.build_heap(frequency)
        self.merge_nodes()
        self.generate_codes()
    
    def encode_text(self, text: str) -> str:
        """Encode text using generated Huffman codes"""
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text
    
    def decode_text(self, encoded_text: str) -> str:
        """Decode encoded text back to original"""
        current_code = ""
        decoded_text = ""
        
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                char = self.reverse_mapping[current_code]
                decoded_text += char
                current_code = ""
        
        return decoded_text
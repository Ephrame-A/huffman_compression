class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
    
    def frequency_analysis(self, text):
        pass
    
    def build_heap(self, frequency):
        pass
    
    def merge_nodes(self):
        pass
    
    def generate_codes(self):
        pass
    
    def encode(self, text):
        pass
    
    def decode(self, encoded_text):
        pass

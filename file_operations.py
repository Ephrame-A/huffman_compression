import os
from typing import Tuple
from huffman_coding import HuffmanCoding


class FileOperations:
    """Handle file I/O operations for Huffman compression"""
    
    def __init__(self):
        self.huffman = HuffmanCoding()
    
    def read_text_file(self, file_path: str) -> str:
        """Read text file content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading file {file_path}: {str(e)}")
    
    def write_text_file(self, file_path: str, content: str):
        """Write text content to file"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            raise Exception(f"Error writing file {file_path}: {str(e)}")
    
    def compress_file(self, input_path: str, output_path: str) -> Tuple[float, float]:
        """Compress a text file and save compressed data"""
        # Read original file
        original_text = self.read_text_file(input_path)
        
        # Compress the text
        compressed_data = self.huffman.compress(original_text)
        
        # Save compressed data
        with open(output_path, 'wb') as file:
            file.write(compressed_data)
        
        # Calculate metrics
        compression_ratio = self.huffman.calculate_compression_ratio(original_text, compressed_data)
        space_savings = self.huffman.calculate_space_savings(original_text, compressed_data)
        
        return compression_ratio, space_savings
    
    def decompress_file(self, input_path: str, output_path: str) -> str:
        """Decompress a file and save original text"""
        # Read compressed data
        with open(input_path, 'rb') as file:
            compressed_data = file.read()
        
        # Decompress
        original_text = self.huffman.decompress(compressed_data)
        
        # Save decompressed text
        self.write_text_file(output_path, original_text)
        
        return original_text
    
    def get_file_size(self, file_path: str) -> int:
        """Get file size in bytes"""
        return os.path.getsize(file_path)
    
    def compare_file_sizes(self, original_path: str, compressed_path: str) -> Tuple[int, int, float]:
        """Compare original and compressed file sizes"""
        original_size = self.get_file_size(original_path)
        compressed_size = self.get_file_size(compressed_path)
        size_ratio = original_size / compressed_size if compressed_size > 0 else 0
        return original_size, compressed_size, size_ratio
    
    def verify_compression(self, original_path: str, compressed_path: str, decompressed_path: str) -> bool:
        """Verify that decompressed file matches original"""
        try:
            # Read original
            original_text = self.read_text_file(original_path)
            
            # Decompress to the specified path
            self.decompress_file(compressed_path, decompressed_path)
            
            # Read decompressed
            decompressed_text = self.read_text_file(decompressed_path)
            
            # Compare
            return original_text == decompressed_text
        except Exception as e:
            print(f"Verification error: {str(e)}")
            return False

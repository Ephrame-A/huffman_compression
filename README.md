# Huffman Coding Lossless Text Compression System

A comprehensive implementation of Huffman Coding for lossless text compression, designed for digital platforms handling large volumes of textual data such as citizen records, reports, service logs, and legal documents.

## Features

- **Lossless Compression**: Guarantees perfect reconstruction of original data
- **Frequency Analysis**: Analyzes character distribution patterns in text
- **Huffman Tree Construction**: Builds optimal prefix codes based on character frequencies
- **File I/O Operations**: Complete file compression and decompression capabilities
- **Command-line Interface**: Easy-to-use CLI for all operations
- **Verification System**: Ensures data integrity throughout compression/decompression

## Algorithm Overview

Huffman Coding is a lossless data compression algorithm that assigns variable-length prefix codes to characters based on their frequency in the input text. More frequent characters receive shorter codes, while less frequent characters receive longer codes.

### Key Components

1. **Frequency Analysis**: Counts occurrences of each character
2. **Priority Queue**: Builds min-heap for optimal tree construction
3. **Huffman Tree**: Binary tree where left edges represent '0' and right edges represent '1'
4. **Code Generation**: Traverses tree to generate prefix codes
5. **Encoding/Decoding**: Converts text to bit sequences and back

## Installation & Usage

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Files Structure

```
huffman/
├── file_operations.py         # File I/O and CLI interface
├── huffman_coding.py          # Core Huffman compression implementation
├── performance_evaluation.py  # Performance testing and benchmarking
├── data/
│   ├── input/                 # Sample input text files
│   ├── output/                # Compressed and restored files
│   └── reports/               # Benchmark JSON/CSV reports
└── README.md                  # This documentation
```

Generated benchmark outputs such as `*.zip`, `*_restored.txt`, `huffman_results.json`, and `huffman_results.csv` are written under `data/output` and `data/reports` and are ignored by default.

### Command Line Usage

#### Compress a file
```bash
python file_operations.py compress data/input/document.txt
python file_operations.py compress data/input/document.txt -o data/output/compressed.zip
```

#### Decompress a file
```bash
python file_operations.py decompress data/output/compressed.zip
python file_operations.py decompress data/output/compressed.zip -o data/output/restored.txt
```

#### Analyze character frequency
```bash
python file_operations.py analyze data/input/document.txt
```

#### Run performance evaluation directly
```bash
python performance_evaluation.py
```
This will automatically test the two retained text scenarios from `data/input` and generate JSON and CSV reports in `data/reports`.

## Performance Evaluation

The implementation includes comprehensive performance evaluation with the following metrics:

- **Compression Ratio**: Original size / Compressed size
- **Space Savings**: Percentage of storage space saved
- **Time Complexity**: Compression and decompression speed
- **Verification**: Data integrity checks

### Test Results Summary

Based on comprehensive testing with realistic data (~20KB+ per file):

| Text Type | Space Savings | Interpretation |
|-----------|---------------|----------------|
| **Repetitive Text** | **45.3%** | Excellent efficiency. Repeated natural-language patterns allow for optimal bit-grouping. |
| **Random Data** | **26.0%** | Good efficiency. Even with high entropy, Huffman achieves compression by optimizing bit sequences. |


## Algorithm Complexity

- **Time Complexity**: O(n log n) where n is the number of unique characters
- **Space Complexity**: O(n) for storing Huffman tree and codes
- **Compression Speed**: Linear to input size after tree construction
- **Decompression Speed**: Linear to compressed data size

## Implementation Details

### Core Classes

- `HuffmanNode`: Represents nodes in the Huffman tree
- `HuffmanCoding`: Main compression/decompression logic
- `FileOperations`: File I/O and compression utilities

### Data Storage

Compressed files store:
- Huffman codes dictionary
- Padding information for bit alignment
- Compressed bit sequence
- Original text length for verification

## Testing
```bash
python file_operations.py compress data/input/repetitive_text.txt
python file_operations.py compress data/input/random_text.txt

```
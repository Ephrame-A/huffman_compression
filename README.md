# Huffman Coding Lossless Text Compression System

A comprehensive implementation of Huffman Coding for lossless text compression, designed for a national digital platform (e.g., e-government system) handling sensitive data such as citizen records, reports, service logs, and legal documents.

## 1. Scenario & Problem Statement

As digital platforms scale, storage costs and data transmission overhead increase, especially in bandwidth-constrained environments. A lossless text compression mechanism is critical to:
- Reduce storage space
- Optimize data transmission
- Preserve exact original content

Given the sensitivity of government records, lossy techniques are strictly unacceptable. This project uses Huffman Coding, an optimal prefix coding algorithm, to minimize the bits required to represent text without any information loss.

## 2. System Implementation

The system implements the complete classical Huffman algorithm in Python:

1. **Frequency Analysis**: Counts character occurrences in the dataset.
2. **Tree Construction**: Uses a min-heap (priority queue) to construct an optimal binary tree.
3. **Code Generation**: Traverses the tree to generate unique binary prefix codes for every character.
4. **Encoding/Decoding**: Converts text to binary, and reconstructs the exact original text.
5. **Serialization**: Packs the compression map into a binary header without using external libraries like `pickle`, ensuring authentic bit-level evaluation.

### File Structure
- `file_operations.py`: Handles transparent reading/writing of files and command-line execution.
- `huffman_coding.py`: Core algorithm implementation (Node classes, heap building, encoding, decoding).
- `performance_evaluation.py`: Testing suite to measure compression ratio, byte-level savings, and time complexity.

## 3. Performance Evaluation

The evaluation tests three distinct datasets matching real-world scenarios: natural language, structured/repetitive data, and randomized text. 

### Empirical Results

| Dataset | Type Description | Space Savings | Compression Ratio | Compression Time | Verification | Interpretation |
|---|---|---|---|---|---|---|
| **Alice29.txt** | Natural Language | **42.8%** | 1.75 | 0.07s | PASSED | Excellent compression. The uneven frequency distribution of natural English makes Huffman highly effective for standard reports. |
| **Alphabet.txt** | Repetitive Pattern | **40.2%** | 1.67 | 0.08s | PASSED | High compression due to consistent character patterns. |
| **Random.txt** | High Entropy (Worst Case) | **24.6%** | 1.33 | 0.07s | PASSED | Even with randomized data, Huffman compresses efficiently, though less optimally due to uniform character frequencies. |

*(Results automatically generated using `performance_evaluation.py` on a standard CPU node)*

A bar chart visualizing these file size differences is generated at `data/reports/performance_chart.png`.

## 4. Time Complexity Analysis

- **Frequency Analysis**: O(N) where N is the length of the string.
- **Tree Construction**: O(K log K) where K is the number of unique characters. In text files, K is typically small (e.g., K < 256), turning this into a near constant operation overhead.
- **Encoding/Decoding**: O(N) as it iterates through the text sequence linearly.

Overall Time Complexity: **O(N + K log K)**, making it highly efficient for massive log processing and real-time document delivery.
Overall Space Complexity: **O(K)** auxiliary space to store the prefix codes and tree, well within acceptable bounds.

## 5. How to Run

1. **Setup Environment**:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows Git Bash
   pip install matplotlib numpy
   ```

2. **Run Benchmark Suite**:
   ```bash
   python performance_evaluation.py
   ```
   *This evaluates the 3 specific datasets, generating summary reports and visual charts under `data/reports/`.*

3. **Manual CLI Usage**:
   ```bash
   # Compress a file
   python file_operations.py compress data/input/alice29.txt -o data/output/example.zip
   
   # Decompress a file
   python file_operations.py decompress data/output/example.zip -o data/output/restored.txt
   
   # View Character Frequencies
   python file_operations.py analyze data/input/alice29.txt
   ```

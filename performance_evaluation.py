#!/usr/bin/env python3
"""
Performance Evaluation Module for Huffman Coding System
Comprehensive testing, benchmarking, and result saving
"""

import time
import os
import json
import csv
from datetime import datetime
from typing import Dict, List
from huffman_coding import HuffmanCoding


class PerformanceEvaluator:
    """Evaluate compression performance metrics"""

    def __init__(self):
        self.huffman = HuffmanCoding()

    # -----------------------------
    # FILE I/O HELPERS
    # -----------------------------
    def read_text_file(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            raise Exception(f"Error reading file {file_path}: {str(e)}")

    def write_text_file(self, file_path: str, content: str):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            raise Exception(f"Error writing file {file_path}: {str(e)}")

    # -----------------------------
    # COMPRESSION OPERATIONS
    # -----------------------------
    def compress_file(self, input_path: str, output_path: str):
        original_text = self.read_text_file(input_path)

        compressed_data = self.huffman.compress(original_text)

        with open(output_path, 'wb') as file:
            file.write(compressed_data)

        compression_ratio = self.huffman.calculate_compression_ratio(
            original_text, compressed_data
        )
        space_savings = self.huffman.calculate_space_savings(
            original_text, compressed_data
        )

        return compression_ratio, space_savings

    def decompress_file(self, input_path: str, output_path: str) -> str:
        with open(input_path, 'rb') as file:
            compressed_data = file.read()

        original_text = self.huffman.decompress(compressed_data)

        self.write_text_file(output_path, original_text)

        return original_text

    # -----------------------------
    # VERIFICATION
    # -----------------------------
    def verify_compression(self, original_path: str, compressed_path: str, decompressed_path: str) -> bool:
        try:
            original_text = self.read_text_file(original_path)

            self.decompress_file(compressed_path, decompressed_path)

            decompressed_text = self.read_text_file(decompressed_path)

            return original_text == decompressed_text

        except Exception as e:
            print(f"Verification error: {str(e)}")
            return False

    # -----------------------------
    # CORE EVALUATION (TEXT)
    # -----------------------------
    def evaluate_text_compression(self, text: str, description: str) -> dict:
        print(f"\n--- Testing: {description} ---")

        start_time = time.time()
        compressed_data = self.huffman.compress(text)
        compression_time = time.time() - start_time

        start_time = time.time()
        decompressed_text = self.huffman.decompress(compressed_data)
        decompression_time = time.time() - start_time

        original_size = len(text) * 8
        compressed_size = len(compressed_data) * 8

        compression_ratio = original_size / compressed_size if compressed_size > 0 else 0
        space_savings = ((original_size - compressed_size) / original_size) * 100

        is_correct = text == decompressed_text

        results = {
            "description": description,
            "original_size": original_size,
            "compressed_size": compressed_size,
            "compression_ratio": compression_ratio,
            "space_savings": space_savings,
            "compression_time": compression_time,
            "decompression_time": decompression_time,
            "is_correct": is_correct
        }

        print(f"Original size: {original_size:,} bits")
        print(f"Compressed size: {compressed_size:,} bits")
        print(f"Compression ratio: {compression_ratio:.2f}")
        print(f"Space savings: {space_savings:.1f}%")
        print(f"Compression time: {compression_time:.4f}s")
        print(f"Decompression time: {decompression_time:.4f}s")
        print(f"Verification: {'✓ PASSED' if is_correct else '✗ FAILED'}")

        return results

    # -----------------------------
    # FREQUENCY ANALYSIS
    # -----------------------------
    def analyze_frequency_distribution(self, text: str, description: str):
        print(f"\n--- Frequency Analysis: {description} ---")

        frequency = self.huffman.frequency_analysis(text)
        total_chars = len(text)

        sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        print(f"Total characters: {total_chars:,}")
        print(f"Unique characters: {len(sorted_freq)}")

        print("\nTop 10 characters:")
        for i, (char, freq) in enumerate(sorted_freq[:10]):
            percentage = (freq / total_chars) * 100
            display_char = repr(char) if char.isspace() else char
            print(f"{i+1}. '{display_char}': {freq:,} ({percentage:.1f}%)")

    # -----------------------------
    # SAVE RESULTS (JSON)
    # -----------------------------
    def save_results_json(self, results: list, filename: str = "huffman_results.json"):
        data = {
            "timestamp": datetime.now().isoformat(),
            "results": results
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"\n Results saved to {filename}")

    # -----------------------------
    # SAVE RESULTS (CSV)
    # -----------------------------
    def save_results_csv(self, results: list, filename: str = "huffman_results.csv"):
        if not results:
            return

        keys = results[0].keys()

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)

        print(f" Results saved to {filename}")

    # -----------------------------
    # COMPREHENSIVE TESTS
    # -----------------------------
    def run_comprehensive_tests(self) -> List[dict]:
        print("=" * 60)
        print("HUFFMAN CODING COMPREHENSIVE EVALUATION")
        print("=" * 60)

        test_cases = [
            ("hello hello hello world", "Repetitive Text"),
            ("abcdefghijklmnopqrstuvwxyz", "Random Text"),
            ("The quick brown fox jumps over the lazy dog", "Mixed Content"),
            ("def function(): return True", "Code-like Text")
        ]

        all_results = []

        for text, description in test_cases:
            self.analyze_frequency_distribution(text, description)
            results = self.evaluate_text_compression(text, description)
            all_results.append(results)

        self.generate_summary_report(all_results)

        # SAVE RESULTS
        self.save_results_json(all_results)
        self.save_results_csv(all_results)

        return all_results

    # -----------------------------
    # SUMMARY REPORT
    # -----------------------------
    def generate_summary_report(self, results: List[dict]):
        print("\n" + "=" * 60)
        print("COMPREHENSIVE SUMMARY REPORT")
        print("=" * 60)

        avg_ratio = sum(r['compression_ratio'] for r in results) / len(results)
        avg_savings = sum(r['space_savings'] for r in results) / len(results)

        print(f"\nAverage compression ratio: {avg_ratio:.2f}")
        print(f"Average space savings: {avg_savings:.1f}%")

        best = max(results, key=lambda x: x['space_savings'])
        worst = min(results, key=lambda x: x['space_savings'])

        print(f"\nBest case: {best['description']} ({best['space_savings']:.1f}%)")
        print(f"Worst case: {worst['description']} ({worst['space_savings']:.1f}%)")


# -----------------------------
# RUN PROGRAM
# -----------------------------
if __name__ == "__main__":
    evaluator = PerformanceEvaluator()
    evaluator.run_comprehensive_tests()
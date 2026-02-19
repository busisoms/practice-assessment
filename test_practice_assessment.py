import unittest
import sys
from pathlib import Path
import string
import random

sys.path.insert(0, str(Path(__file__).parent))

from practice_assessment import (
    flatten_nested_list,
    merge_catalogs,
    validate_password,
    transpose_matrix,
    remove_duplicates_preserve_order,
    calculate_final_grades,
    word_frequency,
    generate_primes,
    binary_search,
)


class TestPracticeAssessment(unittest.TestCase):
    
    # ==================================================================================
    # Question 1: Flatten Nested List Tests
    # ==================================================================================
    
    def test_flatten_nested_list_simple(self):
        self.assertEqual(flatten_nested_list([1, [2, 3], 4]), [1, 2, 3, 4])
    
    def test_flatten_nested_list_deep(self):
        self.assertEqual(
            flatten_nested_list([1, [2, [3, [4, 5]]]]),
            [1, 2, 3, 4, 5]
        )
    
    def test_flatten_nested_list_empty(self):
        self.assertEqual(flatten_nested_list([]), [])
    
    def test_flatten_nested_list_stress_deep_nesting(self):
        """Stress test: Very deep nesting (50 levels)"""
        nested = 1
        for i in range(50):
            nested = [nested]
        result = flatten_nested_list(nested)
        self.assertEqual(result, [1])
    
    def test_flatten_nested_list_stress_wide(self):
        """Stress test: Wide list with many nested lists"""
        nested = [[i] for i in range(1000)]
        result = flatten_nested_list(nested)
        self.assertEqual(result, list(range(1000)))
    
    def test_flatten_nested_list_stress_mixed(self):
        """Stress test: Mixed depths and types"""
        nested = [1, [2, [3, 4]], 5, [6, [7, [8, 9]]], 10]
        result = flatten_nested_list(nested)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    def test_flatten_nested_list_edge_single_element(self):
        """Edge case: Single element"""
        self.assertEqual(flatten_nested_list([42]), [42])
    
    def test_flatten_nested_list_edge_only_nested_empty(self):
        """Edge case: Only nested empty lists"""
        self.assertEqual(flatten_nested_list([[], [[]], [[[]]]]), [])
    
    # ==================================================================================
    # Question 2: Merge Catalogs Tests
    # ==================================================================================
    
    def test_merge_catalogs_overlap(self):
        result = merge_catalogs(
            {'apple': 5, 'banana': 3},
            {'apple': 2, 'orange': 4}
        )
        self.assertEqual(result, {'apple': 7, 'banana': 3, 'orange': 4})
    
    def test_merge_catalogs_no_overlap(self):
        result = merge_catalogs({'apple': 5}, {'banana': 3})
        self.assertEqual(result, {'apple': 5, 'banana': 3})
    
    def test_merge_catalogs_stress_large_catalogs(self):
        """Stress test: Large catalogs with 1000 items each"""
        catalog_a = {f'item_{i}': i for i in range(1000)}
        catalog_b = {f'item_{i}': i * 2 for i in range(500, 1500)}
        result = merge_catalogs(catalog_a, catalog_b)
        
        # Check overlap items
        self.assertEqual(result['item_500'], 1500)  # 500 + 1000
        self.assertEqual(result['item_999'], 2997)  # 999 + 1998
        # Check unique items
        self.assertEqual(result['item_0'], 0)
        self.assertEqual(result['item_1499'], 2998)
    
    def test_merge_catalogs_stress_all_overlap(self):
        """Stress test: Catalogs with complete overlap"""
        catalog_a = {f'item_{i}': 100 for i in range(500)}
        catalog_b = {f'item_{i}': 200 for i in range(500)}
        result = merge_catalogs(catalog_a, catalog_b)
        
        # All should be 300
        self.assertTrue(all(v == 300 for v in result.values()))
        self.assertEqual(len(result), 500)
    
    def test_merge_catalogs_edge_empty_catalogs(self):
        """Edge case: Empty catalogs"""
        self.assertEqual(merge_catalogs({}, {}), {})
        self.assertEqual(merge_catalogs({'a': 1}, {}), {'a': 1})
        self.assertEqual(merge_catalogs({}, {'b': 2}), {'b': 2})
    
    def test_merge_catalogs_edge_zero_quantities(self):
        """Edge case: Zero quantities"""
        result = merge_catalogs({'apple': 0}, {'apple': 5})
        self.assertEqual(result, {'apple': 5})
    
    # ==================================================================================
    # Question 3: Transpose Matrix Tests
    # ==================================================================================
    
    def test_transpose_matrix(self):
        result = transpose_matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result, [[1, 4], [2, 5], [3, 6]])
    
    def test_transpose_matrix_square(self):
        result = transpose_matrix([[1, 2], [3, 4]])
        self.assertEqual(result, [[1, 3], [2, 4]])
    
    def test_transpose_matrix_stress_large_matrix(self):
        """Stress test: Large 100x100 matrix"""
        matrix = [[i * 100 + j for j in range(100)] for i in range(100)]
        result = transpose_matrix(matrix)
        
        # Check dimensions
        self.assertEqual(len(result), 100)
        self.assertEqual(len(result[0]), 100)
        
        # Check a few values
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[50][25], 2550)  # Original [25][50]
    
    def test_transpose_matrix_stress_rectangular_wide(self):
        """Stress test: Wide matrix (10x1000)"""
        matrix = [[i * 1000 + j for j in range(1000)] for i in range(10)]
        result = transpose_matrix(matrix)
        
        self.assertEqual(len(result), 1000)
        self.assertEqual(len(result[0]), 10)
        self.assertEqual(result[500][5], 5500)
    
    def test_transpose_matrix_stress_rectangular_tall(self):
        """Stress test: Tall matrix (1000x10)"""
        matrix = [[i * 10 + j for j in range(10)] for i in range(1000)]
        result = transpose_matrix(matrix)
        
        self.assertEqual(len(result), 10)
        self.assertEqual(len(result[0]), 1000)
        self.assertEqual(result[5][500], 5005)
    
    def test_transpose_matrix_edge_single_row(self):
        """Edge case: Single row matrix"""
        result = transpose_matrix([[1, 2, 3]])
        self.assertEqual(result, [[1], [2], [3]])
    
    def test_transpose_matrix_edge_single_column(self):
        """Edge case: Single column matrix"""
        result = transpose_matrix([[1], [2], [3]])
        self.assertEqual(result, [[1, 2, 3]])
    
    def test_transpose_matrix_edge_1x1(self):
        """Edge case: 1x1 matrix"""
        result = transpose_matrix([[42]])
        self.assertEqual(result, [[42]])
    
    # ==================================================================================
    # Question 4: Calculate Final Grades Tests
    # ==================================================================================
    
    def test_calculate_final_grades(self):
        students = {
            'Alice': {
                'assignments': [80, 90, 85],
                'midterm': 88,
                'final': 92
            }
        }
        result = calculate_final_grades(students)
        self.assertAlmostEqual(result['Alice'], 88.0, places=1)
    
    def test_calculate_final_grades_stress_many_students(self):
        """Stress test: 1000 students"""
        students = {
            f'Student_{i}': {
                'assignments': [70 + i % 30, 80 + i % 20, 75 + i % 25],
                'midterm': 80 + i % 20,
                'final': 85 + i % 15
            }
            for i in range(1000)
        }
        result = calculate_final_grades(students)
        
        self.assertEqual(len(result), 1000)
        # All grades should be between 0 and 100
        self.assertTrue(all(0 <= grade <= 100 for grade in result.values()))
    
    def test_calculate_final_grades_stress_many_assignments(self):
        """Stress test: Student with 100 assignments"""
        students = {
            'Overachiever': {
                'assignments': [80 + i % 20 for i in range(100)],
                'midterm': 90,
                'final': 95
            }
        }
        result = calculate_final_grades(students)
        self.assertTrue(80 <= result['Overachiever'] <= 95)
    
    def test_calculate_final_grades_edge_perfect_scores(self):
        """Edge case: All perfect scores"""
        students = {
            'Perfect': {
                'assignments': [100, 100, 100],
                'midterm': 100,
                'final': 100
            }
        }
        result = calculate_final_grades(students)
        self.assertEqual(result['Perfect'], 100.0)
    
    def test_calculate_final_grades_edge_zero_scores(self):
        """Edge case: All zero scores"""
        students = {
            'Struggling': {
                'assignments': [0, 0, 0],
                'midterm': 0,
                'final': 0
            }
        }
        result = calculate_final_grades(students)
        self.assertEqual(result['Struggling'], 0.0)
    
    def test_calculate_final_grades_edge_single_assignment(self):
        """Edge case: Single assignment"""
        students = {
            'OnlyOne': {
                'assignments': [85],
                'midterm': 90,
                'final': 95
            }
        }
        result = calculate_final_grades(students)
        # 40% * 85 + 30% * 90 + 30% * 95 = 89.5
        self.assertAlmostEqual(result['OnlyOne'], 89.5, places=1)
    
    # ==================================================================================
    # Question 5: Word Frequency Tests
    # ==================================================================================
    
    def test_word_frequency(self):
        result = word_frequency("The cat and the dog. The cat!", 2)
        self.assertEqual(result, [('the', 3), ('cat', 2)])
    
    def test_word_frequency_case_insensitive(self):
        result = word_frequency("Hello hello HELLO", 1)
        self.assertEqual(result, [('hello', 3)])
    
    def test_word_frequency_stress_large_text(self):
        """Stress test: Large text with 10,000 words"""
        words = ['word' + str(i % 100) for i in range(10000)]
        text = ' '.join(words)
        result = word_frequency(text, 5)
        
        # Each word should appear 100 times
        self.assertEqual(len(result), 5)
        self.assertTrue(all(count == 100 for word, count in result))
    
    def test_word_frequency_stress_unique_words(self):
        """Stress test: 1000 unique words (each appears once)"""
        text = ' '.join([f'unique{i}' for i in range(1000)])
        result = word_frequency(text, 10)
        
        self.assertEqual(len(result), 10)
        # All should have count of 1
        self.assertTrue(all(count == 1 for word, count in result))
    
    def test_word_frequency_stress_punctuation_heavy(self):
        """Stress test: Text with heavy punctuation"""
        text = "Hello!!! World??? Test... Hello, world! Test; hello."
        result = word_frequency(text, 3)
        self.assertEqual(result, [('hello', 3), ('world', 2), ('test', 2)])
    
    def test_word_frequency_edge_empty_text(self):
        """Edge case: Empty text"""
        result = word_frequency("", 5)
        self.assertEqual(result, [])
    
    def test_word_frequency_edge_only_punctuation(self):
        """Edge case: Only punctuation"""
        result = word_frequency("!!! ... ???", 5)
        self.assertEqual(result, [])
    
    def test_word_frequency_edge_more_top_n_than_words(self):
        """Edge case: top_n larger than unique words"""
        result = word_frequency("one two three", 10)
        self.assertEqual(len(result), 3)
    
    # ==================================================================================
    # Question 6: Remove Duplicates Preserve Order Tests
    # ==================================================================================
    
    def test_remove_duplicates_preserve_order(self):
        result = remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4])
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_remove_duplicates_strings(self):
        result = remove_duplicates_preserve_order(['a', 'b', 'a', 'c'])
        self.assertEqual(result, ['a', 'b', 'c'])
    
    def test_remove_duplicates_stress_large_list(self):
        """Stress test: 10,000 items with many duplicates"""
        items = [i % 100 for i in range(10000)]  # 0-99 repeated
        result = remove_duplicates_preserve_order(items)
        
        self.assertEqual(result, list(range(100)))
        self.assertEqual(len(result), 100)
    
    def test_remove_duplicates_stress_all_duplicates(self):
        """Stress test: All same element"""
        items = [42] * 1000
        result = remove_duplicates_preserve_order(items)
        self.assertEqual(result, [42])
    
    def test_remove_duplicates_stress_no_duplicates(self):
        """Stress test: No duplicates (1000 unique items)"""
        items = list(range(1000))
        result = remove_duplicates_preserve_order(items)
        self.assertEqual(result, items)
    
    def test_remove_duplicates_edge_empty_list(self):
        """Edge case: Empty list"""
        self.assertEqual(remove_duplicates_preserve_order([]), [])
    
    def test_remove_duplicates_edge_single_element(self):
        """Edge case: Single element"""
        self.assertEqual(remove_duplicates_preserve_order([1]), [1])
    
    def test_remove_duplicates_edge_mixed_types(self):
        """Edge case: Mixed types (if supported)"""
        # This tests if implementation can handle mixed types
        result = remove_duplicates_preserve_order([1, '1', 1, 2, '2', 2])
        # Should preserve all different types
        self.assertEqual(len(result), 4)  # 1, '1', 2, '2'
    
    # ==================================================================================
    # Question 7: Validate Password Tests
    # ==================================================================================
    
    def test_validate_password_valid(self):
        self.assertTrue(validate_password("Secure123!"))
        self.assertTrue(validate_password("P@ssw0rd"))
    
    def test_validate_password_invalid(self):
        self.assertFalse(validate_password("weak"))
        self.assertFalse(validate_password("NoNumbers!"))
        self.assertFalse(validate_password("nouppercas3!"))
        self.assertFalse(validate_password("NOLOWERCASE3!"))
        self.assertFalse(validate_password("NoSpecial123"))
    
    def test_validate_password_stress_very_long(self):
        """Stress test: Very long password (1000 chars)"""
        long_password = "Aa1!" + "a" * 996
        self.assertTrue(validate_password(long_password))
    
    def test_validate_password_stress_all_specials(self):
        """Stress test: Password with all special characters"""
        password = "Abc123!@#$%^&*"
        self.assertTrue(validate_password(password))
    
    def test_validate_password_edge_exactly_8_chars(self):
        """Edge case: Exactly 8 characters"""
        self.assertTrue(validate_password("Abcd123!"))
    
    def test_validate_password_edge_7_chars(self):
        """Edge case: 7 characters (too short)"""
        self.assertFalse(validate_password("Abc12!"))
    
    def test_validate_password_edge_missing_each_requirement(self):
        """Edge case: Missing one requirement at a time"""
        self.assertFalse(validate_password("abcdefg1!"))  # No uppercase
        self.assertFalse(validate_password("ABCDEFG1!"))  # No lowercase
        self.assertFalse(validate_password("Abcdefgh!"))  # No digit
        self.assertFalse(validate_password("Abcdefg12"))  # No special
    
    def test_validate_password_edge_all_requirements_minimal(self):
        """Edge case: Minimal valid password"""
        self.assertTrue(validate_password("Aa1!aaaa"))
    
    # ==================================================================================
    # Question 8: Generate Primes Tests
    # ==================================================================================
    
    def test_generate_primes(self):
        result = generate_primes(20)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19])
    
    def test_generate_primes_small(self):
        result = generate_primes(10)
        self.assertEqual(result, [2, 3, 5, 7])
    
    def test_generate_primes_stress_large_limit(self):
        """Stress test: Generate primes up to 10,000"""
        result = generate_primes(10000)
        
        # There are 1229 primes less than 10,000
        self.assertEqual(len(result), 1229)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[-1], 9973)
        
        # Verify all are actually prime
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        # Check first 10 and last 10
        for prime in result[:10] + result[-10:]:
            self.assertTrue(is_prime(prime))
    
    def test_generate_primes_stress_verify_no_composites(self):
        """Stress test: Verify no composite numbers in result"""
        result = generate_primes(100)
        
        # 4, 6, 8, 9, 10 should NOT be in result
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for composite in composites:
            self.assertNotIn(composite, result)
    
    def test_generate_primes_edge_limit_2(self):
        """Edge case: Limit of 2"""
        self.assertEqual(generate_primes(2), [])
    
    def test_generate_primes_edge_limit_3(self):
        """Edge case: Limit of 3"""
        self.assertEqual(generate_primes(3), [2])
    
    def test_generate_primes_edge_limit_0(self):
        """Edge case: Limit of 0"""
        self.assertEqual(generate_primes(0), [])
    
    def test_generate_primes_edge_limit_1(self):
        """Edge case: Limit of 1"""
        self.assertEqual(generate_primes(1), [])
    
    # ==================================================================================
    # Question 9: Binary Search Tests
    # ==================================================================================
    
    def test_binary_search_found(self):
        result = binary_search([1, 3, 5, 7, 9], 5)
        self.assertEqual(result, 2)
    
    def test_binary_search_not_found(self):
        result = binary_search([1, 3, 5, 7, 9], 4)
        self.assertEqual(result, -1)
    
    def test_binary_search_first_element(self):
        result = binary_search([1, 3, 5, 7, 9], 1)
        self.assertEqual(result, 0)
    
    def test_binary_search_stress_large_list(self):
        """Stress test: Binary search in list of 100,000 elements"""
        sorted_list = list(range(0, 200000, 2))  # Even numbers
        
        # Search for existing elements
        self.assertEqual(binary_search(sorted_list, 0), 0)
        self.assertEqual(binary_search(sorted_list, 100000), 50000)
        self.assertEqual(binary_search(sorted_list, 199998), 99999)
        
        # Search for non-existing elements
        self.assertEqual(binary_search(sorted_list, 1), -1)  # Odd number
        self.assertEqual(binary_search(sorted_list, 99999), -1)  # Odd number
    
    def test_binary_search_stress_duplicates(self):
        """Stress test: List with duplicates (should return any valid index)"""
        sorted_list = [1, 2, 2, 2, 3, 4, 5]
        result = binary_search(sorted_list, 2)
        # Should return any index where 2 exists (1, 2, or 3)
        self.assertIn(result, [1, 2, 3])
        self.assertEqual(sorted_list[result], 2)
    
    def test_binary_search_edge_single_element_found(self):
        """Edge case: Single element (found)"""
        self.assertEqual(binary_search([42], 42), 0)
    
    def test_binary_search_edge_single_element_not_found(self):
        """Edge case: Single element (not found)"""
        self.assertEqual(binary_search([42], 10), -1)
    
    def test_binary_search_edge_last_element(self):
        """Edge case: Last element"""
        result = binary_search([1, 3, 5, 7, 9], 9)
        self.assertEqual(result, 4)
    
    def test_binary_search_edge_negative_numbers(self):
        """Edge case: List with negative numbers"""
        sorted_list = [-10, -5, -1, 0, 3, 7, 12]
        self.assertEqual(binary_search(sorted_list, -5), 1)
        self.assertEqual(binary_search(sorted_list, 0), 3)
    
    def test_binary_search_stress_all_same_value(self):
        """Stress test: All elements are the same"""
        sorted_list = [5] * 1000
        result = binary_search(sorted_list, 5)
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 1000)
        self.assertEqual(sorted_list[result], 5)


if __name__ == "__main__":
    unittest.main()
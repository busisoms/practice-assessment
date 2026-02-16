import unittest
import sys
from pathlib import Path

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
# ---------------------------------------------------------------------------------------------------------- #

    def test_flatten_nested_list_simple(self):
        self.assertEqual(flatten_nested_list([1, [2, 3], 4]), [1, 2, 3, 4])
    
    def test_flatten_nested_list_deep(self):
        self.assertEqual(
            flatten_nested_list([1, [2, [3, [4, 5]]]]),
            [1, 2, 3, 4, 5]
        )
    
    def test_flatten_nested_list_empty(self):
        self.assertEqual(flatten_nested_list([]), [])
    
# ---------------------------------------------------------------------------------------------------------- #

    def test_merge_catalogs_overlap(self):
        result = merge_catalogs(
            {'apple': 5, 'banana': 3},
            {'apple': 2, 'orange': 4}
        )
        self.assertEqual(result, {'apple': 7, 'banana': 3, 'orange': 4})
    
    def test_merge_catalogs_no_overlap(self):
        result = merge_catalogs({'apple': 5}, {'banana': 3})
        self.assertEqual(result, {'apple': 5, 'banana': 3})

# ---------------------------------------------------------------------------------------------------------- #

    def test_transpose_matrix(self):
        result = transpose_matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result, [[1, 4], [2, 5], [3, 6]])
    
    def test_transpose_matrix_square(self):
        result = transpose_matrix([[1, 2], [3, 4]])
        self.assertEqual(result, [[1, 3], [2, 4]])
    
# ---------------------------------------------------------------------------------------------------------- #

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
    
# ---------------------------------------------------------------------------------------------------------- #

    def test_word_frequency(self):
        result = word_frequency("The cat and the dog. The cat!", 2)
        self.assertEqual(result, [('the', 3), ('cat', 2)])
    
    def test_word_frequency_case_insensitive(self):
        result = word_frequency("Hello hello HELLO", 1)
        self.assertEqual(result, [('hello', 3)])
    
  # ---------------------------------------------------------------------------------------------------------- #
    
    def test_remove_duplicates_preserve_order(self):
        result = remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4])
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_remove_duplicates_strings(self):
        result = remove_duplicates_preserve_order(['a', 'b', 'a', 'c'])
        self.assertEqual(result, ['a', 'b', 'c'])

# ---------------------------------------------------------------------------------------------------------- #

    def test_validate_password_valid(self):
        self.assertTrue(validate_password("Secure123!"))
        self.assertTrue(validate_password("P@ssw0rd"))
    
    def test_validate_password_invalid(self):
        self.assertFalse(validate_password("weak"))
        self.assertFalse(validate_password("NoNumbers!"))
        self.assertFalse(validate_password("nouppercas3!"))
        self.assertFalse(validate_password("NOLOWERCASE3!"))
        self.assertFalse(validate_password("NoSpecial123"))

# ---------------------------------------------------------------------------------------------------------- #

    def test_generate_primes(self):
        result = generate_primes(20)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19])
    
    def test_generate_primes_small(self):
        result = generate_primes(10)
        self.assertEqual(result, [2, 3, 5, 7])

# ---------------------------------------------------------------------------------------------------------- #

    def test_binary_search_found(self):
        result = binary_search([1, 3, 5, 7, 9], 5)
        self.assertEqual(result, 2)
    
    def test_binary_search_not_found(self):
        result = binary_search([1, 3, 5, 7, 9], 4)
        self.assertEqual(result, -1)
    
    def test_binary_search_first_element(self):
        result = binary_search([1, 3, 5, 7, 9], 1)
        self.assertEqual(result, 0)

# ---------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    unittest.main()
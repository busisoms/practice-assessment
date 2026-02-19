def flatten_nested_list(nested_list: list) -> list:
    """
    Flatten a nested list of any depth into a single list.
    
    Args:
        nested_list: A list that may contain other lists
        
    Returns:
        A flat list containing all elements
        
    Example:
        flatten_nested_list([1, [2, 3], [4, [5, 6]]]) -> [1, 2, 3, 4, 5, 6]
    """
    flat = []
    for i in nested_list:
        if isinstance(i, list):
            flat.extend(flatten_nested_list(i))
        else:
            flat.append(i)
    
    return flat

def merge_catalogs(catalog_a: dict, catalog_b: dict) -> dict:
    """
    Merge two product catalogs. If a product exists in both,
    sum their quantities.
    
    Args:
        catalog_a: {'product_name': quantity}
        catalog_b: {'product_name': quantity}
        
    Returns:
        Merged catalog with summed quantities
        
    Example:
        merge_catalogs({'apple': 5, 'banana': 3}, {'apple': 2, 'orange': 4})
        -> {'apple': 7, 'banana': 3, 'orange': 4}
    """
    complete_catalog = {}
    complete_catalog = complete_catalog | catalog_a
    for k, v in catalog_b.items():
        if k in complete_catalog.keys():
            complete_catalog[k] = complete_catalog[k] + catalog_b[k]
        else:
            complete_catalog[k] = v
    
    return complete_catalog

def transpose_matrix(matrix: list) -> list:
    """
    Transpose a 2D matrix (swap rows and columns).
    
    Args:
        matrix: 2D list (list of lists)
        
    Returns:
        Transposed matrix
        
    Example:
        transpose_matrix([[1, 2, 3], [4, 5, 6]])
        -> [[1, 4], [2, 5], [3, 6]]
    """
    transposed = []
    for inner in range(len(matrix[0])):
        temp = []
        for i in range(len(matrix)):
            temp.append(matrix[i][inner])
        transposed.append(temp)
    
    return transposed                

def calculate_final_grades(students: dict) -> dict:
    """
    Calculate final grades based on weighted scores.
    
    Args:
        students: {
            'name': {
                'assignments': [scores],  # 40% of grade
                'midterm': score,         # 30% of grade
                'final': score            # 30% of grade
            }
        }
        
    Returns:
        {'name': final_grade} where final_grade is weighted average
        
    Example:
        calculate_final_grades({
            'Alice': {'assignments': [80, 90, 85], 'midterm': 88, 'final': 92}
        })
        -> {'Alice': 88.0}
    """
    final = {}
    for key in students.keys():
        assignments = (sum(students[key]['assignments']) / len(students[key]['assignments'])) * 0.4
        final_marks = (students[key]['midterm'] * 0.3) + (students[key]['final'] * 0.3) + assignments
        final.update({key: final_marks})
        
    return final


def word_frequency(text: str, top_n: int = 5) -> list:
    """
    Find the top N most frequent words in text (case-insensitive).
    Ignore punctuation.
    
    Args:
        text: Input text string
        top_n: Number of top words to return (default 5)
        
    Returns:
        List of tuples (word, count) sorted by count (descending)
        
    Example:
        word_frequency("The cat and the dog. The cat!", 2)
        -> [('the', 3), ('cat', 2)]
    """
 
    usable = []
    for word in text.lower().split():
        temp_str = "".join([i for i in word if i.isalnum()])
        if temp_str != "":
            usable.append(temp_str)
    
    d = {i: usable.count(i) for i in usable}
  
    x = dict(sorted(d.items(), key=lambda item:item[1], reverse=True))
    
    return x[:top_n]
    
    

def remove_duplicates_preserve_order(items: list) -> list:
    """
    Remove duplicates from list while preserving original order.
    
    Args:
        items: List with potential duplicates
        
    Returns:
        List with duplicates removed, original order maintained
        
    Example:
        remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4])
        -> [1, 2, 3, 4]
    """
    res = []
    for i in items:
        if i not in res:
            res.append(i)
    
    return res

def validate_password(password: str) -> bool:
    """
    Validate password meets all requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*)
    
    Args:
        password: String to validate
        
    Returns:
        True if valid, False otherwise
        
    Example:
        validate_password("Secure123!") -> True
        validate_password("weak") -> False
    """
    pass

def generate_primes(limit: int) -> list:
    """
    Generate all prime numbers up to (but not including) limit.
    
    Args:
        limit: Upper bound (exclusive)
        
    Returns:
        List of prime numbers
        
    Example:
        generate_primes(20) -> [2, 3, 5, 7, 11, 13, 17, 19]
    """
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        
        if n == 2:
            return True
        
        for i in range(2, n):
            if n % i == 0:
                return False 
        return True
    
    primes = []
    for i in range(limit):
        if is_prime(i):
            primes.append(i)
    
    return primes

def binary_search(sorted_list: list, target: int) -> int:
    """
    Implement binary search to find target in sorted list.
    
    Args:
        sorted_list: Sorted list of integers
        target: Value to find
        
    Returns:
        Index of target if found, -1 otherwise
        
    Example:
        binary_search([1, 3, 5, 7, 9], 5) -> 2
        binary_search([1, 3, 5, 7, 9], 4) -> -1
    """
    l = 0
    r = len(sorted_list)
    
    while l < r:
        mid = (l + r) // 2
        
        if sorted_list[mid] == target:
            return mid
        
        if target > sorted_list[mid]:
            l = mid + 1
        
        if target < sorted_list[mid]:
            r = mid - 1
        
    return -1

# print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))
# print( calculate_final_grades({
#             'Alice': {'assignments': [80, 90, 85], 'midterm': 88, 'final': 92}
#         }))
text = "Hello!!! World??? Test... Hello, world! Test; hello."
print(word_frequency(text))
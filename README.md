# LeetCode 311 - Sparse Matrix Multiplication

## Problem Statement

Given two sparse matrices `mat1` of size `m x k` and `mat2` of size `k x n`, return the result of `mat1 x mat2`.

A sparse matrix contains many zero values, so the goal is to avoid unnecessary multiplication involving zeros.

## Example 1

### Input

```text
mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
```

### Output

```text
[[7,0,0],[-7,0,3]]
```

## Example 2

### Input

```text
mat1 = [[0]]
mat2 = [[0]]
```

### Output

```text
[[0]]
```

## Approach

Use **Sparse Matrix Multiplication** by skipping zero values.

Instead of multiplying every possible pair of elements, only perform multiplication when the value in `mat1` and the corresponding value in `mat2` are non-zero.

## Algorithm

1. Find the number of rows in `mat1`.
2. Find the number of columns in `mat2`.
3. Create a result matrix filled with zeros.
4. Traverse each row of `mat1`.
5. Check whether the current value of `mat1` is non-zero.
6. If it is non-zero, traverse the corresponding row of `mat2`.
7. Skip zero values in `mat2`.
8. Multiply the non-zero values and add them to the result matrix.
9. Return the result matrix.

## Time Complexity

`O(m × k × n)` in the worst case.

For sparse matrices, skipping zero values reduces the actual number of operations.

## Space Complexity

`O(m × n)`

## Key Concepts

* Matrix
* Array
* Sparse Matrix
* Matrix Multiplication
* Nested Loops
* Zero Optimization

## Language

Python

## LeetCode Details

* **Problem:** 311
* **Title:** Sparse Matrix Multiplication
* **Difficulty:** Medium

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`

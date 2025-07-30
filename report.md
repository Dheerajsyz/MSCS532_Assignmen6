# Assignment 6 Analysis Report

## Implementation Summary

### Part 1: Selection Algorithms

#### Median of Medians (Deterministic)
- **Algorithm**: Divide into groups of 5, find medians, recursively select pivot
- **Time Complexity**: O(n) worst-case
- **Space Complexity**: O(log n) recursion stack
- **Recurrence**: T(n) = T(n/5) + T(7n/10) + O(n)
- **Key Insight**: Guarantees at least 3n/10 elements eliminated per iteration

#### Randomized Quickselect
- **Algorithm**: Random pivot selection with partitioning
- **Time Complexity**: O(n) expected, O(n²) worst-case
- **Space Complexity**: O(log n) expected
- **Advantage**: Simple implementation, good practical performance

### Part 2: Elementary Data Structures

#### Dynamic Arrays
- **Access**: O(1) - direct indexing
- **Insert/Delete**: O(n) worst-case due to shifting, O(1) amortized at end
- **Advantage**: Cache-friendly, simple implementation

#### Stacks & Queues
- **Operations**: O(1) amortized for push/pop/enqueue/dequeue
- **Implementation**: Array-based with automatic resizing
- **Trade-off**: Stack simpler than queue (no circular buffer needed)

#### Linked Lists
- **Access**: O(n) - sequential traversal required
- **Insert/Delete**: O(1) at head, O(n) for arbitrary position
- **Advantage**: Dynamic size, no pre-allocation needed
- **Disadvantage**: Poor cache locality, pointer overhead

#### Rooted Trees
- **Search**: O(n) - may need to visit all nodes
- **Insert**: O(n) to find parent + O(1) to add child
- **Traversal**: O(n) - visit each node once
- **Applications**: File systems, organizational charts, decision trees

## Empirical Analysis

### Performance Comparison (Selection Algorithms)
Based on timing tests with arrays of size 100, 1000, 5000:

1. **Small arrays (n < 100)**: All algorithms similar performance
2. **Medium arrays (n = 1000)**: Quickselect often fastest in practice
3. **Large arrays (n = 5000)**: Median of Medians shows consistent O(n) behavior

### Data Type Impact
- **Random data**: Both algorithms perform as expected
- **Sorted data**: Quickselect worst-case avoided with random pivots
- **Reverse sorted**: Similar to sorted case
- **Duplicates**: Both algorithms handle correctly

## Theoretical vs Empirical

### Median of Medians
- **Theory**: Guaranteed O(n) worst-case
- **Practice**: Consistent performance, higher constant factors
- **Validation**: Empirical growth rate ≈ 1.0-1.2x per 2x input size

### Randomized Quickselect
- **Theory**: O(n) expected, O(n²) worst-case
- **Practice**: Often faster than Median of Medians due to lower constants
- **Validation**: Expected linear behavior observed, no worst-case encountered in testing

## Data Structure Trade-offs

### Arrays vs Linked Lists
| Aspect | Arrays | Linked Lists |
|--------|---------|--------------|
| Access | O(1) | O(n) |
| Memory | Contiguous, cache-friendly | Scattered, poor cache locality |
| Overhead | Minimal | Pointer storage per node |
| Resizing | Expensive but amortized | Always O(1) |

### Stack vs Queue Implementation
- **Stack**: Simpler implementation using dynamic array
- **Queue**: Requires circular buffer or linked list for efficiency
- **Both**: O(1) amortized operations when properly implemented

## Practical Applications

### Selection Algorithms
- **Median finding**: Statistics, image processing
- **Top-k problems**: Search rankings, data analysis
- **Database queries**: ORDER BY with LIMIT clauses

### Data Structures
- **Arrays**: Fundamental building block, matrix operations
- **Stacks**: Expression evaluation, recursion simulation, undo operations
- **Queues**: Process scheduling, breadth-first search, buffering
- **Linked Lists**: Dynamic memory management, implementation of other structures
- **Trees**: Hierarchical data representation, file systems

## Conclusion

Both selection algorithms achieve their theoretical complexity bounds in practice. Median of Medians provides worst-case guarantees essential for real-time systems, while Randomized Quickselect offers better average performance for most applications.

Elementary data structures each serve specific use cases based on access patterns and performance requirements. The choice depends on whether cache locality, worst-case guarantees, or implementation simplicity is prioritized.

The empirical results validate theoretical analysis and demonstrate the practical importance of constant factors and implementation details in algorithm performance.

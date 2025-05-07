# Getting Started with Leetcode & DSA

## What is Leetcode?
Leetcode is a platform offering coding challenges to help software engineers prepare for technical interviews. It covers data structures, algorithms, and system design, and provides mock interviews, contests, and discussion forums.

## Is Leetcode Necessary?
Not strictly. Some companies value practical experience over coding challenges. However, most large tech companies use Leetcode-style problems in interviews. Practicing on Leetcode is an effective way to improve coding and problem-solving skills.

## Which Programming Language to Start With?
Most entry-level roles allow you to use any language. If you already know one, stick with it. Otherwise, Python is recommended for its simplicity, resources, and libraries. Focus on learning built-in libraries for DSA to solve problems efficiently.

## How to Start?
- Learn basic Big O notation, time complexity, and fundamental data structures and algorithms.
- Don’t over-research resources—pick one and stick with it.
- Recommended resources:
  - Data Structures: William Fiset's YouTube channel
  - Algorithms: Abdul Bari's YouTube channel

## How to Study and Practice?
- Tackle one topic at a time: Arrays → Strings → Linked Lists → Hash Tables → Binary Trees.
- For each topic:
  - Understand the concept and implementation.
  - Solve 10–20 easy problems to build confidence.
  - Move to 5 medium problems before advancing to the next topic.
  - Skip hard problems initially; focus on mediums as most interviews do.
- Leetcode offers curated lists (e.g., Top 100 Liked, Top 150 Interview, Top 50 Google). Aim to solve these.
- Target: 300–500 problems for solid preparation.

## Problem-Solving Approach

### Visualize First
Use pen and paper to draw diagrams for problems involving trees, graphs, and other complex structures. Sketching the problem helps identify patterns and solutions that may not be obvious when reading the problem description.

### Start with Brute Force
Begin with the simplest working solution, even if inefficient. This establishes a baseline and deepens your understanding of the problem before attempting optimizations.

### Optimization Strategies
1. **Leverage Problem Constraints** - Use information given in the problem (e.g., "array is sorted" suggests binary search or two pointers)
2. **Precompute Values** - Cache repeated calculations using prefix sums or frequency counters
3. **Trade Space for Time** - Use additional data structures to improve time complexity:
   - HashMaps for O(1) lookups
   - Sets for tracking unique values
   - Arrays for indexing
4. **Data Structure Brainstorm** - Consider which structures best fit the problem:
   - HashMap/Dictionary
   - Array/List
   - Set
   - Stack/Queue
   - LinkedList
   - Tree
   - Graph
   - Heap/Priority Queue

## How to Solve Problems?
Take your time - do not rush to increase your problem count. It is better to solve 5 problems with deep understanding than 50 problems with superficial understanding.
For every problem, try to reason why the solution works. What was the one insight that would have made you solve the problem?

Instead of focusing on individual problems, try to grasp the underlying pattern that connects similar problems.

### Most Important Patterns:
1. Prefix Sum
2. Two Pointers
3. Sliding Window
4. Monotonic Stack
5. Top K Elements
6. Matrix Traversal
7. Modified Binary Search
8. Overlapping Intervals
9. Binary Tree Traversal
10. Depth First Search (DFS)
11. Breadth First Search (BFS)
12. Backtracking

## How to Approach a Problem?
- **Read the Problem Statement Twice**:
  - First pass: Understand the big picture.
  - Second pass: Focus on special conditions and constraints for optimization.
- **Analyze Input-Output Examples**:
  - Walk through examples step by step to identify solutions.
- **Use Pen and Paper to Visualize**:
  - Draw trees, graphs, or other structures to simplify problem-solving.
- **Start with Brute Force**:
  - Begin with a simple solution and optimize it later.

### Optimization Steps:
1. Use unused information from the problem statement to optimize your solution. (Eg: Array is sorted -> Binary search and two pointers)
2. Precompute information - if calculations are repeated multiple times, precompute them using prefix sums and frequency counts.
3. Make time vs space trade-offs - Sometimes using extra memory like hashmaps or arrays can help you reduce time complexity. (Eg: Hashmap to store frequency counts, or a set to store unique values)
4. Do a DS brainstorm - run through all the DS and try to apply them to the problem. (Eg: Hashmap, Array, Set, Stack, Queue, LinkedList, Tree, Graph)
5. Do not overcomplicate - at every step, ask yourself can this be done simpler? Can I use a simpler data structure? Can I use a simpler algorithm? Can I use a simpler approach? 
6. Develop a habit to analyze the time and space complexity of your solution.

## How Much Time to Spend on a Problem?
When you are starting out, even easy problems can take a while to solve. Your goal in the beginning should be to understand the problem deeply and develop intuition about data structures and algorithms. Real progress happens when you spend time to think through and wrestle with the problem, spaced repetitions, and practice.

Many problems require special tricks or patterns to solve. Spending a lot of time here is counterproductive. If you are stuck on a problem for more than 30 minutes, read the solution. Read the top-voted solutions, try to understand why they work, reason how you can apply the same trick elsewhere, and then try to implement them from scratch.

Maintain an excel sheet for all the problems you have solved by date, topic, approach, etc. Add a column for why does this solution work and what was the key insight that solved this problem. Keep revising and revisiting.

## Do Not Memorize
Memorization will cause you to forget. In the interview, the interviewer will ask you to explain your solution, approach, and delve deeper into the problem. If you have memorized, you will not be able to explain it. Instead, focus on the logic and problem-solving.



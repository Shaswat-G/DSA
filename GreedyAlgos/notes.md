# Greedy Algorithms: Theory and Fundamentals for Technical Interviews

## 1. Optimization Problems: Structure and Mathematical Formulation

### 1.1 Components of an Optimization Problem

Every optimization problem consists of five key components:

1. **Decision Variables**: What we're choosing or deciding
2. **Feasible Set**: All valid solutions that satisfy constraints
3. **Constraints**: Rules that limit our choices
4. **Objective Function**: What we're trying to optimize (maximize or minimize)
5. **Selection Procedure**: How we make choices step by step

### 1.2 Mathematical Formulation Template

```
Given: Input parameters and constraints
Find: Decision variables x₁, x₂, ..., xₙ
Subject to: Constraint₁(x₁, x₂, ..., xₙ) ≤ b₁
           Constraint₂(x₁, x₂, ..., xₙ) ≤ b₂
           ...
           Constraintₘ(x₁, x₂, ..., xₙ) ≤ bₘ
Optimize: f(x₁, x₂, ..., xₙ) → max/min
```

### 1.3 General Procedure for Problem Identification and Translation

**Step 1: Identify the Problem Type**
- Is there a clear objective to maximize or minimize?
- Are there constraints that limit valid solutions?
- Can the problem be broken into sequential decisions?

**Step 2: Extract Components**
- **What are we choosing?** → Decision variables
- **What are we optimizing?** → Objective function
- **What limits our choices?** → Constraints
- **What constitutes a valid solution?** → Feasible set

**Step 3: Mathematical Translation**
- Define variables symbolically
- Express objective as a mathematical function
- Write constraints as inequalities/equalities
- Specify variable domains (integers, reals, binary, etc.)

### 1.4 Toy Example: Fractional Knapsack

**Problem**: Given items with weights and values, and a knapsack capacity, maximize value.

**Step 1: Identify**
- Objective: Maximize total value
- Constraints: Weight limit
- Sequential decisions: Which fraction of each item to take

**Step 2: Extract Components**
- Decision variables: Fraction of each item to include
- Objective: Total value
- Constraints: Total weight ≤ capacity
- Feasible set: All combinations satisfying weight constraint

**Step 3: Mathematical Formulation**
```
Given: n items with weights w₁, w₂, ..., wₙ and values v₁, v₂, ..., vₙ
       Knapsack capacity W
Find: x₁, x₂, ..., xₙ where xᵢ = fraction of item i taken
Subject to: Σ(xᵢ × wᵢ) ≤ W for i = 1 to n
           0 ≤ xᵢ ≤ 1 for all i
Maximize: Σ(xᵢ × vᵢ) for i = 1 to n
```

## 2. Greedy Algorithms: Theory and Problem Structure

### 2.1 What is a Greedy Algorithm?

A greedy algorithm makes the **locally optimal choice** at each step, hoping to find a **globally optimal solution**. It never reconsiders previous choices.

**Key Characteristics:**
- Makes irrevocable decisions
- Each choice seems best at the moment
- No backtracking or reconsideration
- Builds solution incrementally

### 2.2 Problem Substructure for Greedy Algorithms

For a greedy algorithm to work, the problem must exhibit:

**1. Optimal Substructure**
- An optimal solution contains optimal solutions to subproblems
- If we make a greedy choice, the remaining problem is a smaller instance of the same problem

**2. Greedy Choice Property**
- A locally optimal (greedy) choice leads to a globally optimal solution
- We can make a greedy choice before solving subproblems

### 2.3 Toy Example: Activity Selection

**Problem**: Select maximum number of non-overlapping activities from a set of activities with start and end times.

**Greedy Insight**: Always pick the activity that ends earliest (among remaining activities).

**Why it works:**
- **Optimal Substructure**: If we optimally solve the remaining activities after choosing one, we get the optimal solution overall
- **Greedy Choice Property**: Choosing the earliest-ending activity leaves maximum room for future activities

**Mathematical Formulation:**
```
Given: Activities A₁, A₂, ..., Aₙ with start times s₁, s₂, ..., sₙ 
       and end times e₁, e₂, ..., eₙ
Find: Subset S ⊆ {1, 2, ..., n}
Subject to: For any i, j ∈ S, activities Aᵢ and Aⱼ don't overlap
           (eᵢ ≤ sⱼ or eⱼ ≤ sᵢ)
Maximize: |S| (number of selected activities)
```

### 2.4 Recipe to Determine if a Problem Admits Greedy Solution

**Test 1: Greedy Choice Property**
- Can you identify a locally optimal choice that's always safe?
- Does making this choice never prevent reaching a global optimum?
- Can you prove that there exists an optimal solution that includes your greedy choice?

**Test 2: Optimal Substructure**
- After making the greedy choice, is the remaining problem a smaller instance of the original?
- Can you solve the remaining problem independently?
- Does the optimal solution to the remaining problem, combined with the greedy choice, give the optimal solution to the original problem?

**Test 3: No Dependencies**
- Are current choices independent of future choices?
- Does the order of making choices not affect the final solution quality?

**Red Flags (Problem likely NOT greedy):**
- Future choices depend heavily on current choices
- Need to consider multiple alternatives simultaneously
- Local optimum conflicts with global optimum
- Problem exhibits overlapping subproblems that benefit from memoization

### 2.5 Proof Techniques for Greedy Algorithms

**Exchange Argument:**
1. Assume there's an optimal solution that differs from the greedy solution
2. Show you can "exchange" parts of the optimal solution to match the greedy choice
3. Prove this exchange doesn't worsen the solution
4. Conclude the greedy solution is also optimal

**Staying Ahead Argument:**
1. Show that after each step, the greedy solution is "at least as good" as any other solution
2. Since the greedy solution stays ahead throughout, it must be optimal

## 3. General Procedure for Creating Greedy Algorithms

### 3.1 Step-by-Step Procedure

**Step 1: Problem Analysis**
- Confirm the problem has greedy structure (use recipe from Section 2.4)
- Identify the decision points where choices must be made
- Determine what constitutes a "local optimum"

**Step 2: Design the Greedy Strategy**
- Choose the selection criterion (what makes a choice "locally optimal")
- Define the order of making decisions
- Specify how to update the problem state after each choice

**Step 3: Algorithm Framework**
```
function GreedyAlgorithm(input):
    solution = empty
    remaining_problem = input
    
    while remaining_problem is not empty:
        choice = SelectBestChoice(remaining_problem)
        if choice is feasible:
            AddToSolution(solution, choice)
            UpdateProblem(remaining_problem, choice)
        else:
            RemoveInfeasibleChoice(remaining_problem, choice)
    
    return solution
```

**Step 4: Implementation Details**
- Efficient data structures for selection and updates
- Feasibility checking mechanism
- Termination condition

**Step 5: Correctness Proof**
- Prove greedy choice property
- Prove optimal substructure
- Use exchange argument or staying ahead argument

**Step 6: Complexity Analysis**
- Time complexity (usually depends on sorting + selection operations)
- Space complexity

### 3.2 Common Greedy Strategies

**1. Earliest Deadline First**
- Used in: Activity selection, job scheduling
- Choose item with earliest deadline/end time

**2. Highest Value First**
- Used in: Fractional knapsack, Huffman coding
- Choose item with highest value or value-to-weight ratio

**3. Shortest Processing Time**
- Used in: Job scheduling to minimize completion time
- Choose job with shortest duration

**4. Largest First**
- Used in: Bin packing, some graph problems
- Choose largest remaining item

**5. Closest First**
- Used in: Minimum spanning tree, shortest path
- Choose closest/minimum weight edge or vertex

### 3.3 Complete Example: Huffman Coding Algorithm

**Problem**: Create optimal binary encoding for characters based on frequency.

**Step 1: Analysis**
- Optimal substructure: Optimal tree contains optimal subtrees
- Greedy choice: Always merge two least frequent nodes

**Step 2: Greedy Strategy**
- Selection criterion: Choose two nodes with minimum frequency
- Order: Bottom-up construction of binary tree
- Update: Replace two nodes with their merged parent

**Step 3: Algorithm**
```
function HuffmanCoding(frequencies):
    priority_queue = MinHeap()
    
    // Initialize with leaf nodes
    for each character c with frequency f:
        priority_queue.insert(Node(c, f))
    
    // Build tree bottom-up
    while priority_queue.size() > 1:
        left = priority_queue.extractMin()
        right = priority_queue.extractMin()
        
        merged = Node(null, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        priority_queue.insert(merged)
    
    return priority_queue.extractMin()  // Root of Huffman tree
```

**Step 4: Correctness**
- Greedy choice property: Merging least frequent nodes never prevents optimal solution
- Optimal substructure: Optimal tree contains optimal subtrees

**Step 5: Complexity**
- Time: O(n log n) for n characters
- Space: O(n) for the tree and priority queue

### 3.4 Template for Interview Problems

```python
def greedy_solution(input_data):
    # Step 1: Preprocess and sort if needed
    candidates = preprocess(input_data)
    candidates.sort(key=greedy_criterion)
    
    # Step 2: Initialize solution
    solution = []
    
    # Step 3: Make greedy choices
    for candidate in candidates:
        if is_feasible(candidate, solution):
            solution.append(candidate)
    
    # Step 4: Return result
    return solution

def greedy_criterion(item):
    # Define what makes a choice "locally optimal"
    pass

def is_feasible(candidate, current_solution):
    # Check if adding candidate maintains constraints
    pass
```

## 4. Summary and Key Takeaways

**When to Use Greedy Algorithms:**
- Problem has optimal substructure and greedy choice property
- Local decisions don't depend on future decisions
- Can prove correctness using exchange or staying ahead arguments

**Common Greedy Problem Types:**
- Activity/interval selection
- Scheduling problems
- Fractional optimization
- Minimum spanning trees
- Shortest path problems
- Huffman coding

**Problem-Solving Strategy:**
1. Identify optimization structure
2. Test for greedy properties
3. Design selection criterion
4. Implement with efficient data structures
5. Prove correctness
6. Analyze complexity

**Red Flags:**
- Need to consider multiple alternatives
- Future choices heavily depend on current ones
- Problem has overlapping subproblems
- Local optimum conflicts with global optimum

Remember: Not all problems that seem greedy actually are. Always verify the greedy choice property and optimal substructure before implementing a greedy solution!
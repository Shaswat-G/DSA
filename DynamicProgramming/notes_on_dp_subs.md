1. It seems to me currently that the important topics in dp are : dp on grids, dp on subsequences, knapsack, coins, partitionas and palindromes. (make this mece - complete, mutually exclusive, collectively exhaustive)

2. Subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. This is different from a subarray or substring, which require contiguous elements. This is also different from a subset, which allows for any combination of elements without regard to order.

3. For dp on sebsequences, we aready know the steps.
3.1 Express everything in terms of a state (index, target)
3.2 The possible direction of explorations are always take or not take the current element. (include vs exclude)

4. For the subset sum problem, we define a dp table with n rows and target+1 columns, where n is the number of elements in the input array. The rows represent the elements of the array, and the columns represent all possible sums from 0 to target. dp[i][j] will be true if a subset with sum j can be formed using the first i elements of the array, and false otherwise. This means that the last row of the dp table tells us all possible sums that can be formed using all elements of the array. This information can be useful for solving related problems, such as partitioning the array into two subsets with minimum difference in their sums. Similarly, if you store the count of subsets instead of a boolean value, the last row will give you the count of subsets for each possible sum.

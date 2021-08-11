# Class 3
#### 7/8/2021
#### What is Array?
An array is defined as the collection of similar type of data items stored at contiguous memory locations.

#### What is Sub Array?
A Sub Array is a contiguous memory location inside an Array. Let‘s say the array is {1,2,3} then the possible sub-array would be {1},{1,2},{1,2,3},{2},{2,3} and {3}. Note that {1,3} is not a sub-array as its elements are not contiguous in main array.

**How Many Sub-Arrays Are Possible of an Array of Size n?**
> The Number Of Possible Sub-Arrays = N*(N+1)/2

### What Is Sub Sequence?
A Sub-Sequence is a sub-set of an Array. Let’s say the array is {1,2,3} then the possible non-empty sub-sequence would be {1},{1,2},{1,2,3},{2},{2,3},{1,3} and {3}. In this case the total number of non-empty sub-sequences are 7.

**How Many Non-Empty Sub-Sequences Are Possible of an Array of Size n?**
> The number of possible non-empty sub-sequences = 2ⁿ - 1

#### Example
An Example would make it clear

Consider an array {1,2,3,4}

List of all its subarrays are {},{1},{2},{3},{4},{1,2},{2,3},{3,4},{1,2,3,4}

List of all its subsequences are {},{1},{2},{3},{4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4},{1,2,3},{1,2,4},{1,3,4},{2,3,4},{1,2,3,4}

> subarray refers to contiguous list whereas subsequence refers to non-contiguous list.


#### What is a contiguous Subarray?
A contiguous sub array can be any length, but it must be a subset of the original array and have the items in their respective order without any breaks. to access the next value in the array, we just move to the next memory address.

#### What is mean by contiguous in computer science?
In contiguous structures, terms of data are kept together in memory (either RAM or in a file). An array is an example of a contiguous structure. Since each element in the array is located next to one or two other elements.

![](https://i.ibb.co/gt5bGtJ/contiguous-array.jpg)

#### What is mean by non-contiguous in computer science?
Items in a non-contiguous structure and scattered in memory, but we linked to each other in some way. A linked list is an example of a noncontiguous data structure


### Summery
> A subarray has Order and Continuity.

> A subsequence has Order but not Continuity

> A subset does not Order nor Continuity.

#### What are Sorting Algorithms?
Sorting algorithms are ways to organize an array of items from smallest to largest.

#### Complexity of Sorting Algorithms?

![](https://i.ibb.co/54Q5jQf/timecofsalgo.png)

#### Big O Graph
![](https://i.ibb.co/kJ9vS36/Big-O-Graph.png)

### Class Work

Leet Code 53

### Home Work 
##### Leet Code 53 Try to Solve with O(n).

#### Reference
https://stackoverflow.com/questions/5298300/definition-of-subarray/45686639

https://medium.com/javarevisited/subarray-vs-subsequence-do-you-know-the-difference-3de0a2c2df52

https://www.wikiwand.com/en/Subsequence

https://stackoverflow.com/questions/26568560/difference-between-subarray-subset-subsequence

https://www.geeksforgeeks.org/sorting-algorithms
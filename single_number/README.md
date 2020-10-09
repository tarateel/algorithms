# Single Number

Given a non-empty array of integers where every element appears twice except for one. Find that single number. You may assume that there will _always_ be _one_ odd-number-out and every other number in the input shows up exactly twice.  

## Examples
```
Sample input: [2, 2, 1]
Expected output: 1
```

```
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
```

Can you implement a solution that finds the single number in _one_ pass through the input array with `O(1)` space complexity?

## Testing
Run the test file by executing `python test_single_number.py`. 

## Brainstorming
~~Make list into set? Hash can find duplicates. what about the _one_ pass requirement?~~

Tip from Bobby: dictionaries

dict.fromkeys() ---> a built-in function that generates a dictionary from the keys you have specified
dictionaries ---> cannot include duplicate keys, will also remove any duplicate values

function name single_number
takes in arr

attempted dict.fromkeys() but there appeared to be issues with converting a list of integers (vs a list of strings) to a dictionary. After wasting far too much time, I went with simple for loop with if/else (initialize an new, empty array, iterate over arr and if you find a number that isn't already in the new array, add ; if the number is already in the new array, remove it).

Not sure if this is exactly what was asked for. there is still that _one pass_ with 0(1) space complexity, which I took to mean only one loop (if any) and in-place (i.e. not creating an empty array for storage).




then convert back to a list

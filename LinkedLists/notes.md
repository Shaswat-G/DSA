Why linked lists?

Arrays gives O(1) random access time, but insertion and deletion are O(n) because you have to shift elements.
LinkedLiss sacrifice this O(1) random access time for O(1) insertion and deletion time.
Thereforre, it allows you to gorw or shrink the list withouth having to pre-allocate or reallocate memory (as opposed to static arrays whch are preallocated and dynamic arrays which are doubled in size when full)

What are linked lists?
Dynamic, linear dta structure that consists of a sequence of nodes, where each node contains a data field and a reference (or pointer) to the next node in the sequence. Can be singly or doubly linked. Can also be circular or non-circular.
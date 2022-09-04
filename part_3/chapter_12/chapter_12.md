# Hash Table
Hash table is one kind of array where data store key and value pair. Here 3 importants part of hash table : 

- **Key** - key must be unique for using as indexing element.
- **Value** - value associated with keys.
- **Hash Function** - a spacify function which convert key to array index.

![hash table with key value](./../../asset/data_structure/hash_table_with_index_number.png)

<hr />
<br />

## Hasing Function
In a hash table new index for new element generate by a function which take a key and create a positive intagare number for element index. This function called **hash function** and the process called **hashing**.

## Hash Collision
When the hash function generates the same index for multiple keys, it's called **Hash Collision**. Because in that case occur the conflict between two keys. What value store in same index. For this problem we using following techniques.

1. Collision Resolution by Chaining.
1. Open Addressing. 

### Collision Resolution by Chaining.
In this solution, if hash function produces the same index for multiple elements, these elements are stored in the same index by using linked list. Here demo diagram of collision resolution by chaining.

![Collision resolution by chaining](./../../asset/data_structure/colision_resolution_using_chaining.png)

### Open Addressing
Open address dose not store multiple element into the same slot. There are different technique used in open addressing. Here : 

1. Linear Probing.
2. Quadratic Probing.
3. Double Hashing.

#### Linear Probing
In linear probing collision is resolved by checking the next slot.Here simple diagram of linear probing :  

![Linear Probing](./../../asset/data_structure/open_addressing.png)

### Quarding Probing
It similar to linear probing but difference is that, spacing between slots is greater than one. 

### Double Hashing
If collision occurs after appling hash function then apply the hash function again or apply different hash function to produce new index. It's called double hashing.

**Program : hash table**
```python
```
# 0x02. Redis basic

## Tasks
### 0. Writing strings to Redis
- Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

### 1. Reading from Redis and recovering original type
- In this exercise we will create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

### 2. Incrementing values
- Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.

### 3. Storing lists
- In this task, we will define a call_history decorator to store the history of inputs and outputs for a particular function.

### 4. Retrieving lists
- In this tasks, we will implement a replay function to display the history of calls of a particular function.

### 5. Implementing an expiring web cache and tracker
- In this tasks, we will implement a get_page function (prototype: def get_page(url: str) -> str:). The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.

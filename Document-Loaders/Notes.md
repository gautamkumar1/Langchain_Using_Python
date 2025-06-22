### Load vs Lazy Load

| Feature          | `load()` (Eager Load)                     | Lazy Load                                   |
| ---------------- | ----------------------------------------- | ------------------------------------------- |
| When it loads | Loads Everything at once       | Loads on demand    |
| Memory usage  | Uses more memory upfront                  | Saves memory until needed                   |
| Speed         | Slower startup (loads everything now)     | Faster startup (waits until needed)         |
| Use case      | Small workflows or components always used | Large apps or optional tools/chains         |
| Reactivity    | Loaded and ready at app start             | Loaded on-demand (dynamic)                  |

**1. Text Loader**

- It is use to simple load text based file.

**2. Pdf Loader**

- It is use to load to pdf file. it will load pdf file in pages means if in ur pdf we have 20 pages then it will load one by one 20 pages. 

- It is only use for simple pdf not for complex pdf structure.

- We can use this pyloader when u have text data in ur pdf file.

**3. Directory Loader**

- It is help to load whole directory(floder) means if any floder we have multiple pdf , text then we can able to load whole floder using directory loader

**4. Web base Loader**

- It is used to load static web page like blog , news articles etc..







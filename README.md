# DevToolkit 🧰

A high-performance Python utility library containing data structures, string manipulation helpers, algorithmic utilities, and mathematical operations.

## Features

- **String Utilities**: Fast string formatting, slugification, and pattern matching.
- **Data Structures**: Efficient implementations of LRU Cache, Trie, Segment Tree, and Priority Queue.
- **Algorithmic Helpers**: Graph algorithms, binary search helpers, and array chunking.
- **Math Utilities**: Matrix operations, prime generators, and statistical functions.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from dev_toolkit.string_utils import slugify, truncate_words
from dev_toolkit.data_structures import LRUCache

# String formatting
print(slugify("DevToolkit Python Library"))  # devtoolkit-python-library

# Cache usage
cache = LRUCache(capacity=100)
cache.put("key", "value")
```

## Running Tests

```bash
pytest tests/
```

## License

MIT License © 2026 Rahil (thecodex110)

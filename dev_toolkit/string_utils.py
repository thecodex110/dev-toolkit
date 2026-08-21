import re

def slugify(text: str) -> str:
    """Convert text into URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[\s_-]+', '-', text)

def truncate_words(text: str, num_words: int) -> str:
    """Truncate a string to a maximum number of words."""
    words = text.split()
    if len(words) <= num_words:
        return text
    return " ".join(words[:num_words]) + "..."

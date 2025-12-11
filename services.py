from typing import List, Optional

from models import Recipe
from config import TAGS

def normalize_tags(tag_list: List[str], all_tags: List[str] = TAGS) -> List[str]:
    """
    clean up a list of tags from a form: 
    - strips whitespace
    - lowercase for matching 
    - keep only tags that exist in all_tags
    - remove duplicates 
    """
    cleaned = []
    allowed = {t.lower(): t for t in all_tags}

    for raw in tag_list:
        if raw is None:
            continue
        key = raw.strip().lower()
        if not key:
            continue
        if key in allowed:
            tag = allowed[key]
            if tag not in cleaned:
                cleaned.append(tag)
    
    return cleaned


def filter_recipes(): 
    pass


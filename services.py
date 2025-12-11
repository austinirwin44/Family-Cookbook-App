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


def filter_recipes(recipes: List[Recipe], query: Optional[str], selected_tags: List[str]) -> List[str]: 
    """
    Filter recipes by:
    - keyword query in recipe name or ingredients (case-insensitive)
    - tag filtering (AND logic: recipe must contain ALL selected tags)
    """
    # normalize the query
    q = (query or "").strip().lower()
    use_query = bool(q)

    # normalize tags agains TAGS list
    tags = normalize_tags(selected_tags)

    filtered: List[Recipe] = []

    for recipe in recipes:
        # keyword match: recipe name OR any ingredient
        if use_query:
            name_match = q in recipe.recipe_name.lower()
            ingredient_match = any(q in ing.lower() for ing in recipe.ingredients)
            if not (name_match or ingredient_match):
                continue # skip, does not match search query

        # tag filtering (AND logic)
        if tags:
            if not all(tag in recipe.tags for tag in tags):
                continue
        
        filtered.append(recipe)
    
    return filtered



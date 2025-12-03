import json
from pathlib import Path
from typing import List, Optional

from models import Recipe
from config import DATA_DIR

DATA_DIR_PATH = Path(DATA_DIR)

def _ensure_data_dir() -> None:
    """Make sure the data directory exists, creates one if not"""
    DATA_DIR_PATH.mkdir(parents=True, exist_ok=True)

def _get_recipe_path(recipe_id: str) -> Path:
    """Return the filesystem path for a given recipe id"""
    return DATA_DIR_PATH / f'{recipe_id}.json'

def load_all_recipes() -> List[Recipe]:
    """Load all recipes from JSON files in DATA_DIR, so they can be searched / filtered over"""
    _ensure_data_dir()
    recipes: List[Recipe] = []
    for path in DATA_DIR_PATH.glob('*.json'):
        try:
            with path.open('r', encoding='utf-8') as f:
                data = json.load(f)
            recipes.append(Recipe.from_dict(data))
        except:
            # in case try block fails, exception will be raised and then continue to next block
            continue
    return recipes

def load_recipe(recipe_id: str) -> Optional[Recipe]:
    """Load a single recipe by id, or return None if it doesn't exist"""
    _ensure_data_dir()
    path = _get_recipe_path(recipe_id)
    if not path.exists():
        return None
    with path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    return Recipe.from_dict(data)

def save_recipe(recipe: Recipe) -> None:
    """Save (create or update) a recipe to its JSON file"""
    _ensure_data_dir()
    path = _get_recipe_path(recipe.id)
    with path.open('w', encoding='utf-8') as f:
        json.dump(recipe.to_dict(), f, ensure_ascii=False, indent=2)
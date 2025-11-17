# models.py
from __future__ import annotations
from typing import List, Optional
import uuid


class Recipe:
    """
    Recipe model.

    - id: unique string id (UUID4)
    - recipe_name: name/title of the recipe
    - author: who contributed the recipe
    - tags: list of tag strings
    - ingredients: list of ingredient strings
    - instructions: list of instruction strings
    - prep_time: prep time in minutes (int)
    - photo: optional filename or URL (string or None)
    """

    def __init__(
        self,
        recipe_name: str,
        author: str,
        tags: List[str],
        ingredients: List[str],
        instructions: List[str],
        prep_time: int,
        recipe_id: Optional[str] = None,
        photo: Optional[str] = None,
    ):
        self.id = recipe_id or str(uuid.uuid4())
        self.recipe_name = recipe_name
        self.author = author
        self.tags = [t.strip() for t in tags if t is not None and t != ""]
        self.ingredients = [i.strip() for i in ingredients if i is not None and i != ""]
        self.instructions = [s.strip() for s in instructions if s is not None and s != ""]
        self.prep_time = int(prep_time)
        self.photo = photo  # filename or URL or None

    def recipe_summary(self) -> str:
        """Short one-line summary suitable for lists."""
        tags_str = ", ".join(self.tags) if self.tags else "no tags"
        return (
            f"{self.recipe_name} by {self.author}: "
            f"{len(self.ingredients)} ingredients, {self.prep_time} min prep, tags: {tags_str}"
        )

    def display_recipe(self) -> str:
        """Readable, multi-line recipe for large-screen display."""
        ingredients_str = "\n".join(f"- {item}" for item in self.ingredients) or "- (no ingredients)"
        instructions_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(self.instructions)) or "No instructions provided."
        photo_line = f"\nPhoto: {self.photo}\n" if self.photo else ""
        return (
            f"{self.recipe_name}\nby {self.author} — {self.prep_time} minute prep\n"
            f"{photo_line}\n"
            f"Ingredients:\n{ingredients_str}\n\n"
            f"Instructions:\n{instructions_str}"
        )

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dictionary."""
        return {
            "id": self.id,
            "recipe_name": self.recipe_name,
            "author": self.author,
            "tags": self.tags,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "prep_time": self.prep_time,
            "photo": self.photo,
        }

    @staticmethod
    def from_dict(data: dict) -> "Recipe":
        """Create a Recipe object from a dict (e.g., loaded from JSON)."""
        return Recipe(
            recipe_name=data.get("recipe_name", ""),
            author=data.get("author", ""),
            tags=data.get("tags", []) or [],
            ingredients=data.get("ingredients", []) or [],
            instructions=data.get("instructions", []) or [],
            prep_time=data.get("prep_time", 0),
            recipe_id=data.get("id"),
            photo=data.get("photo"),
        )

    @staticmethod
    def from_comma_separated(
        recipe_name: str,
        author: str,
        tags_csv: str,
        ingredients_csv: str,
        instructions_csv: str,
        prep_time: int,
        photo: Optional[str] = None,
    ) -> "Recipe":
        """
        Convenience constructor for form data where tags/ingredients/instructions are
        submitted as comma-separated strings.
        """
        def split_csv(s: str) -> List[str]:
            if s is None:
                return []
            # split on commas, strip whitespace, ignore empty items
            return [part.strip() for part in s.split(",") if part.strip()]

        tags = split_csv(tags_csv)
        ingredients = split_csv(ingredients_csv)
        instructions = split_csv(instructions_csv)
        return Recipe(
            recipe_name=recipe_name,
            author=author,
            tags=tags,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=int(prep_time),
            photo=photo,
        )
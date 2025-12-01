# import required packages
import uuid
from typing import List, Optional

# define the class 'Recipe'
class Recipe:
    """
    Recipe model

    - id:
    - recipe_name: name/title of the recipe
    - author: creator of the recipe
    - tags: list of tag strings (i.e., gluten-free, breakfast, quick)
    - ingredients: list of ingredient strings
    - instructions: list of instruction strings 
    - prep_time: prep time in minues (int)
    """
    def __init__(
        self, 
        recipe_name: str, 
        author: str, 
        tags: List[str], 
        ingredients: List[str], 
        instructions: List[str], 
        prep_time: int,
        recipe_id: Optional[str] = None, # this type hint 'Optional' is here as you don't have to specify an id when you create a Recipe object  
    ):
        self.id = recipe_id or str(uuid.uuid4()) # use recipe_id if it is provided, otherwise create a unique one
        self.recipe_name = recipe_name.strip()
        self.author = author.strip()                
        self.tags = [t.strip() for t in tags if t is not None and t != ""] # removes whitespace, empty and null entries                 
        self.ingredients = [i.strip() for i in ingredients if i is not None and i != ""]       
        self.instructions = [s.strip() for s in instructions if s is not None and s != ""]   
        self.prep_time = prep_time      

    def __repr__(self):
        return f'<Recipe {self.recipe_name!r} by {self.author!r}>'   
    
    def recipe_summary(self) -> str:
        """
        creates a short one-line summary for the recipe
        """
        tags_str = ", ".join(self.tags) if self.tags else 'no tags available'
        return (
            f'{self.recipe_name} by {self.author}: '
            f'{len(self.ingredients)} ingredients, {self.prep_time} min prep, tags: {tags_str}'
        )
    
    def display_recipe(self) -> str:
        """
        displays the entire recipe in large format for readability 
        """
        ingredients_str = '\n'.join(self.ingredients) if self.ingredients else 'no ingredients listed'
        instructions_str = '\n'.join(self.instructions) if self.instructions else 'no instructions listed'
        return (
            f'{self.recipe_name}\nby {self.author} - {self.prep_time} minute prep\n'
            f'Ingredients:\n{ingredients_str}'
            f'\n\nInstructions:\n{instructions_str}'
        )
    
    @staticmethod
    def from_dict(data: dict) -> 'Recipe':
        """
        create a Recipe object from a dict, loaded from a .json file
        """
        return Recipe(
            recipe_name=data.get('recipe_name', ''),
            author=data.get('author', ''),
            tags=data.get('tags', []) or [],
            ingredients=data.get('ingredients', []) or [],
            instructions=data.get('instructions', []) or [],
            prep_time=data.get('prep_time', 0),
            recipe_id=data.get('id'),
        )

    def to_dict(self) -> dict:
        """
        converts a recipe object to a dictionary for storage as a .json file
        """
        return {
            'id': self.id,
            'recipe_name': self.recipe_name,
            'author': self.author,
            'tags': self.tags,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'prep_time': self.prep_time,
        }

    @staticmethod
    def from_comma_separated(
        recipe_name: str,
        author: str,
        tags_csv: str,
        ingredients_csv: str,
        instructions_csv: str,
        prep_time: int,
    ) -> 'Recipe':
        """
        creates a Recipe object from strings, rather than lists of strings
        """
        def split_comma_separated(s: str) -> list[str]:
            if s is None:
                return []
            return [part.strip() for part in s.split(',') if part.strip()]
        
        tags = split_comma_separated(tags_csv)
        ingredients = split_comma_separated(ingredients_csv)
        instructions = split_comma_separated(instructions_csv)
        return Recipe(
            recipe_name=recipe_name,
            author=author,
            tags=tags,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time
        )
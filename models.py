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
    - photo: optional filename (str or None)
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
        photo: Optional[str] = None, # this type hint 'Optional' is here because you don't have to include a photo, photo=None if you don't include one
    ):
        self.id = recipe_id or str(uuid.uuid4()) # use recipe_id if it is provided, otherwise create a unique one
        self.recipe_name = recipe_name.strip()
        self.author = author.strip()                
        self.tags = [t.strip() for t in tags if t is not None and t != ""] # removes whitespace, empty and null entries                 
        self.ingredients = [i.strip() for i in ingredients if i is not None and i != ""]       
        self.instructions = [s.strip() for s in instructions if s is not None and s != ""]   
        self.prep_time = prep_time   
        self.photo = photo    

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
        photo_line = f'Photo: {self.photo}\n' if self.photo else ""
        ingredients_str = '\n'.join(self.ingredients) if self.ingredients else 'no ingredients listed'
        instructions_str = '\n'.join(self.instructions) if self.instructions else 'no instructions listed'
        return (
            f'{self.recipe_name}\nby {self.author} - {self.prep_time} minute prep\n'
            f'{photo_line}'
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
            photo=data.get('photo'),
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
            'photo': self.photo,
        }

    @staticmethod
    def from_csv() -> 'Recipe':
        pass
    
    
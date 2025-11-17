# import required packages
import uuid
from typing import Optional

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
        tags: list[str], 
        ingredients: list[str], 
        instructions: list[str], 
        prep_time: int,
        recipe_id: Optional[str] = None, # this type hint 'Optional' is here as you don't have to specify an id when you create a Recipe object  
        photo: Optional[str] = None, # this type hint 'Optional' is here because you don't have to include a photo, photo=None if you don't include one
    ):
        self.id = recipe_id or str(uuid.uuid4()) # use recipe_id if it is provided, otherwise create a unique one
        self.recipe_name = recipe_name
        self.author = author                
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
            f'{self.recipe_name} by {self.author}:'
            f'{len(self.ingredients)} ingredients, {self.prep_time} min prep, tags: {tags_str}'
        )
    
    def display_recipe(self) -> str:
        """
        displays the entire recipe in large format for readability 
        """
        photo_line = f'\nPhoto: {self.photo}\n' if self.photo else ""
        ingredients_str = '\n'.join(self.ingredients) if self.ingredients else 'no ingredients listed'
        instructions_str = '\n'.join(self.instructions) if self.instructions else 'no instructions listed'
        return (
            f'{self.recipe_name}\nby {self.author} - {self.prep_time} minute prep\n'
            f'{photo_line}\n'
            f'Ingredients:\n{ingredients_str}'
            f'Instructions:\n{instructions_str}'
        )
    
    @staticmethod
    def from_dict(data: dict) -> 'Recipe':
        pass

    def to_dict(self) -> dict:
        pass

    @staticmethod
    def from_csv() -> 'Recipe':
        pass
    
    
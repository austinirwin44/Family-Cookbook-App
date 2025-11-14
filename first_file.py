class Recipe:

    def __init__(self, recipe_name: str, author: str, tags: list[str], ingredients: list[str], instructions: list[str], prep_time: int):
        self.recipe_name = recipe_name
        self.author = author                # who made the dish?
        self.tags = tags                    # ex: gluten-free, soup, dessert
        self.ingredients = ingredients      # list of strings
        self.instructions = instructions    # list of strings
        self.prep_time = prep_time          # prep time in minutes
    
    def recipe_summary(self):
        return f'{self.recipe_name} by {self.author}: {len(self.ingredients)} ingredients, {self.prep_time} minute prep time, tags: {self.tags}'
    
    def display_recipe(self):
        return (
            f'{self.recipe_name} by {self.author}, {self.prep_time} minute prep time\n\n'
            f'Ingredients:\n{self.ingredients}\n\n'
            f'Instructions:\n{self.instructions}'
        )


class Cookbook:

    def __init__(self, book_name: str, author: str):
        self.book_name = book_name  
        self.author = author        # who owns the book?
        self.recipes = []           # initialize an empty list for storing recipes in the cookbook
    
    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)
    
    def remove_recipe(self, recipe: Recipe):
        self.recipes.remove(recipe)

    def list_recipes(self):
        return [r.recipe_name for r in self.recipes]
    
    def book_summary(self):
        return f'{self.book_name} by {self.author}, {len(self.recipes)} recipes'
    
    def find_recipes_by_tag(self, tag: str):
        return [r.recipe_name for r in self.recipes if tag in r.tags]

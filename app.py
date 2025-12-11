from flask import Flask, render_template, request

from storage import load_all_recipes
from services import filter_recipes
from config import TAGS

app = Flask(__name__)


@app.route("/")
def index():
    # load all recipes from JSON files
    all_recipes = load_all_recipes()

    # get any search query and selected tags from the URL query params
    query = request.args.get('q', '')
    selected_tags = request.args.getlist('tags')

    # filter recipes
    recipes = filter_recipes(all_recipes, query, selected_tags)

    # render the index page 
    return render_template(
        'index.html', 
        recipes=recipes,
        q=query,
        all_tags=TAGS,
        selected_tags=selected_tags
    )

if __name__ == '__main__':
    app.run(debug=True)
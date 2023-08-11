import tkinter as tk
from tkinter import ttk, scrolledtext

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Book")

        self.recipe_book = RecipeBook()

        self.recipe_name_var = tk.StringVar()
        self.ingredient_name_var = tk.StringVar()
        self.ingredient_measurement_var = tk.StringVar()
        self.step_var = tk.StringVar()

        self.create_gui()

    def create_gui(self):
        recipe_label = tk.Label(self.root, text="Recipe Name:")
        recipe_label.pack()

        recipe_entry = tk.Entry(self.root, textvariable=self.recipe_name_var)
        recipe_entry.pack()

        ingredient_label = tk.Label(self.root, text="Ingredient:")
        ingredient_label.pack()

        ingredient_name_entry = tk.Entry(self.root, textvariable=self.ingredient_name_var)
        ingredient_name_entry.pack()

        ingredient_measurement_entry = tk.Entry(self.root, textvariable=self.ingredient_measurement_var)
        ingredient_measurement_entry.pack()

        add_ingredient_button = tk.Button(self.root, text="Add Ingredient", command=self.add_ingredient)
        add_ingredient_button.pack()

        step_label = tk.Label(self.root, text="Step:")
        step_label.pack()

        step_entry = tk.Entry(self.root, textvariable=self.step_var)
        step_entry.pack()

        add_step_button = tk.Button(self.root, text="Add Step", command=self.add_step)
        add_step_button.pack()

        add_recipe_button = tk.Button(self.root, text="Add Recipe", command=self.add_recipe)
        add_recipe_button.pack()

        self.recipe_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
        self.recipe_display.pack()

        display_button = tk.Button(self.root, text="Display Recipes", command=self.display_recipes)
        display_button.pack()

    def add_ingredient(self):
        ingredient_name = self.ingredient_name_var.get()
        ingredient_measurement = self.ingredient_measurement_var.get()
        ingredient = Ingredient(ingredient_name, ingredient_measurement)
        self.current_recipe.add_ingredient(ingredient)
        self.clear_ingredient_fields()

    def add_step(self):
        step = self.step_var.get()
        self.current_recipe.add_step(step)
        self.step_var.set("")

    def add_recipe(self):
        recipe_name = self.recipe_name_var.get()
        self.current_recipe = Recipe(recipe_name)
        self.recipe_book.add_recipe(self.current_recipe)
        self.clear_recipe_fields()

    def display_recipes(self):
        self.recipe_display.delete(1.0, tk.END)
        recipe_names = self.recipe_book.get_recipe_names()
        for name in recipe_names:
            recipe = self.recipe_book.get_recipe_by_name(name)
            self.recipe_display.insert(tk.END, str(recipe) + "\n\n")

    def clear_recipe_fields(self):
        self.recipe_name_var.set("")
        self.current_recipe = None

    def clear_ingredient_fields(self):
        self.ingredient_name_var.set("")
        self.ingredient_measurement_var.set("")

    def hide_add_recipe_widgets(self):
        for widget in self.add_recipe_widgets:
            widget.pack_forget()

class Ingredient:
    def __init__(self, name, measurement):
        self.name = name
        self.measurement = measurement

class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.steps = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_step(self, step):
        self.steps.append(step)

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join([f'{i.name} ({i.measurement})' for i in self.ingredients])}\nSteps:\n{self.format_steps()}"

    def format_steps(self):
        return "\n".join([f"{index + 1}. {step}" for index, step in enumerate(self.steps)])

class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipe_names(self):
        return [recipe.name for recipe in self.recipes]

    def get_recipe_by_name(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, ttk

# Dictionary containing 5 languages with 20 words each and their meanings
language_dict = {
    "English": {
        "Hello": "A greeting",
        "World": "The Earth",
        "Python": "A programming language",
        "Love": "An intense feeling of deep affection",
        "Friend": "A person whom one knows and has a bond with",
        "Book": "A set of written or printed pages",
        "Computer": "An electronic device for processing data",
        "Music": "Vocal or instrumental sounds combined to produce harmony",
        "Food": "Any substance consumed to provide nutrition",
        "Family": "A group consisting of parents and children",
        "Water": "A transparent, tasteless liquid essential for life",
        "Animal": "A living organism that feeds on organic matter",
        "House": "A building for human habitation",
        "School": "An institution for educating children",
        "Work": "Activity involving mental or physical effort",
        "Game": "A structured form of play or activity",
        "City": "A large town",
        "Sky": "The region of the atmosphere above the Earth",
        "Ocean": "A large body of salt water",
        "Story": "A narrative of events"
    },
    "Spanish": {
        "Hola": "Hello",
        "Mundo": "World",
        "Amor": "Love",
        "Amigo": "Friend",
        "Libro": "Book",
        "Computadora": "Computer",
        "Música": "Music",
        "Comida": "Food",
        "Familia": "Family",
        "Agua": "Water",
        "Animal": "Animal",
        "Casa": "House",
        "Escuela": "School",
        "Trabajo": "Work",
        "Juego": "Game",
        "Ciudad": "City",
        "Cielo": "Sky",
        "Océano": "Ocean",
        "Historia": "Story",
        "Niño": "Child"
    },
    "French": {
        "Bonjour": "Hello",
        "Monde": "World",
        "Amour": "Love",
        "Ami": "Friend",
        "Livre": "Book",
        "Ordinateur": "Computer",
        "Musique": "Music",
        "Nourriture": "Food",
        "Famille": "Family",
        "Eau": "Water",
        "Animal": "Animal",
        "Maison": "House",
        "École": "School",
        "Travail": "Work",
        "Jeu": "Game",
        "Ville": "City",
        "Ciel": "Sky",
        "Océan": "Ocean",
        "Histoire": "Story",
        "Enfant": "Child"
    },
    "German": {
        "Hallo": "Hello",
        "Welt": "World",
        "Liebe": "Love",
        "Freund": "Friend",
        "Buch": "Book",
        "Computer": "Computer",
        "Musik": "Music",
        "Essen": "Food",
        "Familie": "Family",
        "Wasser": "Water",
        "Tier": "Animal",
        "Haus": "House",
        "Schule": "School",
        "Arbeit": "Work",
        "Spiel": "Game",
        "Stadt": "City",
        "Himmel": "Sky",
        "Ozean": "Ocean",
        "Geschichte": "Story",
        "Kind": "Child"
    },
    "Italian": {
        "Ciao": "Hello",
        "Mondo": "World",
        "Amore": "Love",
        "Amico": "Friend",
        "Libro": "Book",
        "Computer": "Computer",
        "Musica": "Music",
        "Cibo": "Food",
        "Famiglia": "Family",
        "Acqua": "Water",
        "Animale": "Animal",
        "Casa": "House",
        "Scuola": "School",
        "Lavoro": "Work",
        "Gioco": "Game",
        "Città": "City",
        "Cielo": "Sky",
        "Oceano": "Ocean",
        "Storia": "Story",
        "Bambino": "Child"
    }
}

def display_language(language):
    """Display all words and meanings in the selected language."""
    if language in language_dict:
        words = language_dict[language]
        display_text = f"{language} Dictionary:\n\n"
        for word, meaning in words.items():
            display_text += f"{word}: {meaning}\n"
        messagebox.showinfo(f"{language} Dictionary", display_text)
    else:
        messagebox.showerror("Error", f"'{language}' not found!")

def search_language():
    """Search for a word in all languages."""
    query = search_entry.get().capitalize()
    results = []
    for language, words in language_dict.items():
        if query in words:
            results.append(f"{query} in {language}: {words[query]}")
    if results:
        messagebox.showinfo("Search Results", "\n".join(results))
    else:
        messagebox.showerror("No Results", f"'{query}' not found in any language!")

# Create the tkinter application
root = tk.Tk()
root.title("Tkinter Language Dictionary")
root.geometry("500x400")

# Welcome message
welcome_label = tk.Label(root, text="Welcome to the Tkinter Language Dictionary", font=("Arial", 14), pady=10)
welcome_label.pack()

# Search bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
search_label = tk.Label(search_frame, text="Search Word:")
search_label.pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(search_frame, width=20)
search_entry.pack(side=tk.LEFT, padx=5)
search_button = tk.Button(search_frame, text="Search", command=search_language)
search_button.pack(side=tk.LEFT, padx=5)

# Language buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=20)

for language in language_dict.keys():
    button = tk.Button(buttons_frame, text=language, width=15, command=lambda lang=language: display_language(lang))
    button.pack(pady=5)

# Run the tkinter main loop
root.mainloop()
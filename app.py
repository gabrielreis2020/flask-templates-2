from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    pokemons = [
        ['Bulbasaur', 'https://i.imgur.com/ntcCJr4.png'],
        ['Charmander', 'https://i.imgur.com/5HmVqlW.png'],
        ['Squirtle', 'https://i.imgur.com/h2aCkl3.png'],
        ['Pikachu', 'https://i.imgur.com/soCJ6J5.png'],
    ]
    return render_template(
        'index.html',
         titulo='Pokedex',
        pokemons=pokemons
    )
if __name__ == '__main__':
 app.run()
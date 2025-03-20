import sqlite3

connection = sqlite3.connect('library.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

#Création d'un utilisateur
cur.execute("INSERT INTO Users (nom, email, mot_de_passe, statut) VALUES (?, ?, ?, ?)",('Alice', 'alice@factice.com', '1234567', 'user')),
cur.execute("INSERT INTO Users (nom, email, mot_de_passe, statut) VALUES (?, ?, ?, ?)",('Jojo', 'jojo@factice.com', '12345678', 'admin')),

#Création des livres de la Bibliothèques
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('1984', 'George Orwell', 1949, 'Science-fiction', 5))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 3))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('Harry Potter à l école des sorciers', 'J.K. Rowling', 1997, 'Fantasy', 10))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('Les Misérables', 'Victor Hugo', 1862, 'Roman historique', 4))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('L Alchimiste', 'Paulo Coelho', 1988, 'Développement personnel', 6))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('Dune', 'Frank Herbert', 1965, 'Science-fiction', 7))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('Fondation', 'Isaac Asimov', 1951, 'Science-fiction', 8))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('La Peste', 'Albert Camus', 1947, 'Philosophique', 5))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('Pride and Prejudice', 'Jane Austen', 1813, 'Romance', 4))
cur.execute("INSERT INTO Livres (titre, auteur, annee_publication, categorie, stock) VALUES (?, ?, ?, ?, ?)",('Le Nom de la Rose', 'Umberto Eco', 1980, 'Policier / Historique', 6))
    
connection.commit()
connection.close()

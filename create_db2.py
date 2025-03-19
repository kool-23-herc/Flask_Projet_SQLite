import sqlite3

def create_connection():
    connection = sqlite3.connect('bibliotheque.db')
    return connection

def execute_script_from_file(connection, file_path):
    with open(file_path, 'r') as f:
        script = f.read()
    cursor = connection.cursor()
    cursor.executescript(script)
    connection.commit()
    print("Script SQL exécuté avec succès")

def insert_clients(connection):
    clients = [
        ('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'),
        ('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'),
        ('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'),
        ('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'),
        ('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'),
        ('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'),
        ('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'),
        ('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris')
    ]
    query = "INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)"
    cursor = connection.cursor()
    cursor.executemany(query, clients)
    connection.commit()
    print("Clients insérés avec succès")

def create_tables(connection):
    cursor = connection.cursor()
    
    # Table des utilisateurs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        mot_de_passe TEXT NOT NULL,
        date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Table des livres
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Livres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        auteur TEXT NOT NULL,
        annee_publication INTEGER,
        genre TEXT,
        quantite INTEGER DEFAULT 1
    );
    """)

    # Table des prêts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Prets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_utilisateur INTEGER,
        id_livre INTEGER,
        date_emprunt DATE NOT NULL,
        date_retour DATE,
        statut TEXT DEFAULT 'emprunté',
        FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id) ON DELETE CASCADE,
        FOREIGN KEY (id_livre) REFERENCES Livres(id) ON DELETE CASCADE
    );
    """)

    # Index pour optimiser les recherches
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_titre ON Livres(titre);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_auteur ON Livres(auteur);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Utilisateurs(email);")
    
    connection.commit()

def insert_data_example(connection):
    cursor = connection.cursor()

    # Ajout d'utilisateurs
    cursor.execute("INSERT INTO Utilisateurs (nom, email, mot_de_passe) VALUES ('Alice Dupont', 'alice.dupont@email.com', 'password123');")
    cursor.execute("INSERT INTO Utilisateurs (nom, email, mot_de_passe) VALUES ('Bob Martin', 'bob.martin@email.com', 'securepass');")
    cursor.execute("INSERT INTO Utilisateurs (nom, email, mot_de_passe) VALUES ('Charlie Durand', 'charlie.durand@email.com', 'mypassword');")

    # Ajout de livres
    cursor.execute("INSERT INTO Livres (titre, auteur, annee_publication, genre, quantite) VALUES ('Les Misérables', 'Victor Hugo', 1862, 'Roman', 5);")
    cursor.execute("INSERT INTO Livres (titre, auteur, annee_publication, genre, quantite) VALUES ('1984', 'George Orwell', 1949, 'Science-fiction', 3);")
    cursor.execute("INSERT INTO Livres (titre, auteur, annee_publication, genre, quantite) VALUES ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 7);")
    cursor.execute("INSERT INTO Livres (titre, auteur, annee_publication, genre, quantite) VALUES ('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 1997, 'Fantasy', 4);")
    cursor.execute("INSERT INTO Livres (titre, auteur, annee_publication, genre, quantite) VALUES ('L\'Étranger', 'Albert Camus', 1942, 'Philosophie', 6);")

    # Ajout de prêts
    cursor.execute("INSERT INTO Prets (id_utilisateur, id_livre, date_emprunt, statut) VALUES (1, 2, '2024-03-01', 'emprunté');")
    cursor.execute("INSERT INTO Prets (id_utilisateur, id_livre, date_emprunt, statut) VALUES (2, 3, '2024-03-02', 'retourné');")
    cursor.execute("INSERT INTO Prets (id_utilisateur, id_livre, date_emprunt, statut) VALUES (3, 1, '2024-03-05', 'emprunté');")

    connection.commit()
    print("Données d'exemple insérées avec succès")



    conn.close()

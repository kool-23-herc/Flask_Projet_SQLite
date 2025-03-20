DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    statut TEXT CHECK( statut IN ('user','admin' )) NOT NULL DEFAULT 'user'
);

DROP TABLE IF EXISTS Livres;
CREATE TABLE Livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre VARCHAR(255) NOT NULL,
    auteur VARCHAR(255) NOT NULL,
    annee_publication INT,
    categorie VARCHAR(100),
    stock INT NOT NULL DEFAULT 1
);

DROP TABLE IF EXISTS Emprunts;
CREATE TABLE Emprunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    livre_id INT,
    date_emprunt DATE NOT NULL,
    date_retour_prevue DATE NOT NULL,
    date_retour_effective DATE,
    statut TEXT CHECK( statut IN ('En emprunt', 'Retour', 'en retard')) NOT NULL DEFAULT 'En emprunt',
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (livre_id) REFERENCES Livres(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Notifications;
CREATE TABLE Notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    message TEXT NOT NULL,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Recommandations;
CREATE TABLE Recommandations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    livre_id INT,
    date_recommandation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (livre_id) REFERENCES Livres(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Statistiques;
CREATE TABLE Statistiques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livre_id INT,
    nombre_emprunts INT DEFAULT 0,
    dernier_emprunt DATE,
    FOREIGN KEY (livre_id) REFERENCES Livres(id) ON DELETE CASCADE
);

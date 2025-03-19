CREATE DATABASE IF NOT EXISTS Bibliotheque;
USE Bibliotheque;

-- Table des utilisateurs
CREATE TABLE Utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des livres
CREATE TABLE Livres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(255) NOT NULL,
    auteur VARCHAR(255) NOT NULL,
    annee_publication INT,
    genre VARCHAR(100),
    quantite INT DEFAULT 1
);

-- Table des prêts
CREATE TABLE Prets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_utilisateur INT,
    id_livre INT,
    date_emprunt DATE NOT NULL,
    date_retour DATE,
    statut ENUM('emprunté', 'retourné') DEFAULT 'emprunté',
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id) ON DELETE CASCADE,
    FOREIGN KEY (id_livre) REFERENCES Livres(id) ON DELETE CASCADE
);

-- Ajout de quelques index pour optimiser les recherches
CREATE INDEX idx_titre ON Livres(titre);
CREATE INDEX idx_auteur ON Livres(auteur);
CREATE INDEX idx_email ON Utilisateurs(email);

-- Trigger pour gérer les stocks lors d'un emprunt
DELIMITER //
CREATE TRIGGER before_emprunt
BEFORE INSERT ON Prets
FOR EACH ROW
BEGIN
    DECLARE stock INT;
    SELECT quantite INTO stock FROM Livres WHERE id = NEW.id_livre;
    IF stock <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Stock insuffisant pour cet emprunt';
    ELSE
        UPDATE Livres SET quantite = quantite - 1 WHERE id = NEW.id_livre;
    END IF;
END;//
DELIMITER ;

-- Trigger pour gérer le retour des livres
DELIMITER //
CREATE TRIGGER after_retour
AFTER UPDATE ON Prets
FOR EACH ROW
BEGIN
    IF NEW.statut = 'retourné' THEN
        UPDATE Livres SET quantite = quantite + 1 WHERE id = NEW.id_livre;
    END IF;
END;//
DELIMITER ;

-- Insertion de données d'exemple

-- Ajout d'utilisateurs
INSERT INTO Utilisateurs (nom, email, mot_de_passe) VALUES
('Alice Dupont', 'alice.dupont@email.com', 'password123'),
('Bob Martin', 'bob.martin@email.com', 'securepass'),
('Charlie Durand', 'charlie.durand@email.com', 'mypassword');

-- Ajout de livres
INSERT INTO Livres (titre, auteur, annee_publication, genre, quantite) VALUES
('Les Misérables', 'Victor Hugo', 1862, 'Roman', 5),
('1984', 'George Orwell', 1949, 'Science-fiction', 3),
('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 7),
('Harry Potter à l'école des sorciers', 'J.K. Rowling', 1997, 'Fantasy', 4),
('L'Étranger', 'Albert Camus', 1942, 'Philosophie', 6);

-- Ajout de prêts
INSERT INTO Prets (id_utilisateur, id_livre, date_emprunt, statut) VALUES
(1, 2, '2024-03-01', 'emprunté'),
(2, 3, '2024-03-02', 'retourné'),
(3, 1, '2024-03-05', 'emprunté');

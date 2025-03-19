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

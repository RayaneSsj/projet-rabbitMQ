# Projet RabbitMQ – Calcul distribué

## Présentation

Ce projet simule un système de calcul distribué. 

Un client envoie automatiquement toutes les 5 secondes des opérations mathématiques (add, sub, mul, div, ou all).  
Des workers spécialisés effectuent les calculs et renvoient les résultats.  
Un autre client lit et affiche les résultats.

## Prérequis

- Python 3
- Docker
- Installer la bibliothèque Pika avec la commande suivante :
  ```
  pip install pika
  ```

## Lancer le serveur RabbitMQ

Ce projet nécessite un serveur RabbitMQ.

Pour cela, utilisez Docker avec la commande suivante :
```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Le serveur RabbitMQ sera disponible :
- AMQP : localhost:5672
- Interface Web : http://localhost:15672  
  Identifiant : guest  
  Mot de passe : guest

Lorsque le serveur a déjà été lancé une première fois, vous pouvez simplement le redémarrer avec :
```
docker start rabbitmq
```

## Lancer le projet

1. Ouvrir plusieurs terminaux et se placer dans le dossier du projet.

2. Dans un premier terminal, lancer le client émetteur :
   ```
   python client_send.py
   ```

3. Dans quatre autres terminaux, lancer les workers :
   ```
   python worker.py add
   python worker.py sub
   python worker.py mul
   python worker.py div
   ```

4. Dans un dernier terminal, lancer le client qui reçoit les résultats :
   ```
   python client_receive.py
   ```

## Description des fichiers

- client_send.py : envoie des opérations toutes les 5 secondes
- worker.py : exécute l'opération demandée (addition, soustraction, multiplication, division)
- client_receive.py : lit et affiche les résultats renvoyés
- README.txt : fichier d'explication

## Fonctionnalité supplémentaire

Si l'opération envoyée est "all", tous les workers exécutent leur opération sur les mêmes nombres.

## Auteur

Projet réalisé par Rayane étudiant en dev management full stack groupe 3. Mail : rayane.rostane@hotmail.com

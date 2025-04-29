# Projet RabbitMQ – Calcul distribué

## Description

Ce projet simule un système de calcul distribué :
- Un client envoie automatiquement des opérations mathématiques toutes les 5 secondes.
- Des workers spécialisés (`add`, `sub`, `mul`, `div`) réalisent les calculs.
- Un client affiche les résultats en temps réel.

Les opérations peuvent aussi être de type `"all"`, où tous les workers réalisent leur calcul.

## Prérequis

- Docker
- Python 3
- pip install pika

## Installation

1. Lancer Docker.
2. Lancer un serveur RabbitMQ :
    ```bash
    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
    ```
3. Installer la dépendance Python :
    ```bash
    pip install pika
    ```

## Utilisation

1. Lancer le client émetteur :
    ```bash
    python client_send.py
    ```
2. Lancer 4 workers (dans 4 terminaux différents) :
    ```bash
    python worker.py add
    python worker.py sub
    python worker.py mul
    python worker.py div
    ```
3. Lancer le client récepteur :
    ```bash
    python client_receive.py
    ```

## Fonctionnalité spéciale

- Le client peut envoyer une opération `"all"` : dans ce cas, **tous** les workers (`add`, `sub`, `mul`, `div`) exécutent chacun leur opération sur les mêmes nombres.

## Auteurs

Projet réalisé dans le cadre d'un exercice de calcul distribué avec RabbitMQ.
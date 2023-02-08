# MultiPwn

## Introduction

multipwn est un outil de réseau de base qui écoute sur un port donné et exécute une commande sur toutes les connexions entrantes. Il est écrit en Python et utilise les sockets pour effectuer ses tâches.
Prérequis

Avant d'installer et d'utiliser multipwn, assurez-vous d'avoir installé Python 3 sur votre ordinateur.
Installation

Pour installer multipwn, téléchargez le code source de ce dépôt et exécutez la commande suivante pour installer les dépendances nécessaires :
```bash
pip install -r requirements.txt
```
## Utilisation

multipwn peut être utilisé en ligne de commande en fournissant le port à écouter et la commande à exécuter. La commande par défaut est id.
```bash
python multipwn.py <port> [-c <command>]
```
## Exemple :
```bash
python multipwn.py 8080 -c 'uname -a'
```
Cela démarre un serveur qui écoute sur le port 8080 et exécute la commande uname -a sur toutes les connexions entrantes.
Notes

L'utilisation de ce logiciel peut être illégale selon les lois et les réglementations en vigueur dans votre pays. Assurez-vous de comprendre les conséquences potentielles et utilisez ce logiciel à vos propres risques.

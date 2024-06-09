from django.core.management.base import BaseCommand
from portfolio_app.models import Project, Competence, ApprentissageCritique, TextField

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Find the existing project
        try:
            project = Project.objects.get(title='Pillage')
        except Project.DoesNotExist:
            self.stdout.write(self.style.ERROR('Project not found'))
            return

        # Create or get competencies
        comp1, created = Competence.objects.get_or_create(name="Réaliser un développement d’application", defaults={'description': 'Développer des applications informatiques simples'})
        comp2, created = Competence.objects.get_or_create(name="Optimiser des applications", defaults={'description': 'Appréhender et construire des algorithmes'})
        comp3, created = Competence.objects.get_or_create(name="Administrer des systèmes informatiques communicants complexes", defaults={'description': 'Installer et configurer un poste de travail'})
        comp4, created = Competence.objects.get_or_create(name="Gérer des données de l’information", defaults={'description': 'Concevoir et mettre en place une base de données à partir d’un cahier des charges client'})
        comp5, created = Competence.objects.get_or_create(name="Conduire un projet", defaults={'description': 'Identifier les besoins métiers des clients et des utilisateurs'})
        comp6, created = Competence.objects.get_or_create(name="Collaborer au sein d’une équipe informatique", defaults={'description': 'Identifier ses aptitudes pour travailler dans une équipe'})

        # Create or get apprentissage critiques
        ac1_1, created = ApprentissageCritique.objects.get_or_create(competence=comp1, title="Implémenter des conceptions simples", defaults={'description': 'AC 1'})
        ac1_2, created = ApprentissageCritique.objects.get_or_create(competence=comp1, title="Élaborer des conceptions simples", defaults={'description': 'AC 2'})
        ac2_1, created = ApprentissageCritique.objects.get_or_create(competence=comp2, title="Analyser un problème avec méthode", defaults={'description': 'AC 1'})
        ac2_2, created = ApprentissageCritique.objects.get_or_create(competence=comp2, title="Comparer des algorithmes pour des problèmes classiques", defaults={'description': 'AC 2'})
        ac3_1, created = ApprentissageCritique.objects.get_or_create(competence=comp3, title="Identifier les différents composants", defaults={'description': 'AC 1'})
        ac3_2, created = ApprentissageCritique.objects.get_or_create(competence=comp3, title="Utiliser les fonctionnalités de base d’un système multitâches / multiutilisateurs", defaults={'description': 'AC 2'})
        ac4_1, created = ApprentissageCritique.objects.get_or_create(competence=comp4, title="Mettre à jour et interroger une base de données relationnelle", defaults={'description': 'AC 1'})
        ac4_2, created = ApprentissageCritique.objects.get_or_create(competence=comp4, title="Visualiser des données", defaults={'description': 'AC 2'})
        ac5_1, created = ApprentissageCritique.objects.get_or_create(competence=comp5, title="Appréhender les besoins du client et de l’utilisateur", defaults={'description': 'AC 1'})
        ac5_2, created = ApprentissageCritique.objects.get_or_create(competence=comp5, title="Mettre en place les outils de gestion de projet", defaults={'description': 'AC 2'})
        ac6_1, created = ApprentissageCritique.objects.get_or_create(competence=comp6, title="Appréhender l’écosystème numérique", defaults={'description': 'AC 1'})
        ac6_2, created = ApprentissageCritique.objects.get_or_create(competence=comp6, title="Découvrir les aptitudes requises selon les différents secteurs informatiques", defaults={'description': 'AC 2'})

        # Define the content to be split into text fields
        texts = [
            {
                'title': 'Introduction',
                'content': (
                    'Lors de mon stage de deuxième année en BUT Informatique, j\'ai mené à bien le projet "Pillage", '
                    'visant à moderniser un site web interne de gestion de packages pour un framework spécifique de '
                    'l\'entreprise. Ce site, initialement conçu comme un simple cache du site Subversion interne, a '
                    'été transformé en une plateforme autonome, comparable à GitHub, mais spécifiquement adaptée à '
                    'SVN pour ce framework particulier.'
                ),
                'competences': [comp1],
                'apprentissages_critiques': [ac1_1, ac1_2]
            },
            {
                'title': 'Contexte et Objectifs',
                'content': (
                    'L\'objectif principal était de migrer l\'infrastructure de RedHat 7 vers RedHat 8 et de mettre à jour '
                    'Python de la version 3.7 à 3.10, en alignement avec les standards de l\'entreprise. En parallèle, la base '
                    'de données a été migrée de SQLite vers MariaDB pour améliorer la gestion des données et les performances. '
                    'Cette migration a également inclus la mise à jour des packages vers des versions plus récentes et stables.'
                ),
                'competences': [comp4],
                'apprentissages_critiques': [ac4_1, ac4_2]
            },
            {
                'title': 'Fonctionnement Avant Mon Intervention',
                'content': (
                    'Avant mon intervention, les releases de packages étaient réalisées sur Jenkins et publiées sur Codex, '
                    'une implémentation interne de Tuleap. Lorsqu\'un utilisateur avait besoin d\'un package, il le téléchargeait '
                    'depuis Pillage. À terme, le processus sera amélioré pour permettre de lancer les releases directement depuis '
                    'Pillage, avec Jenkins se chargeant ensuite de publier les packages sur Codex et Pillage.'
                ),
                'competences': [comp3],
                'apprentissages_critiques': [ac3_1, ac3_2]
            },
            {
                'title': 'Création et Implémentation de l\'API REST',
                'content': (
                    'L\'un des grands défis de ce projet a été la création d\'une API REST avec plusieurs objectifs :\n\n'
                    '- Améliorer la performance du site en permettant de récupérer les données après le rendu des pages.\n'
                    '- Faciliter l\'utilisation du site en permettant aux utilisateurs de récupérer les données uniquement via l\'API.\n'
                    '- Intégrer avec Jenkins pour remplir directement la base de données de l\'application web via des scripts Python.\n\n'
                    'L\'ancienne API a été maintenue pour la compatibilité avec d\'autres applications. La nouvelle API a été documentée '
                    'avec Swagger, offrant une documentation interactive pour faciliter les tests et l\'utilisation de l\'API directement sur le site.'
                ),
                'competences': [comp1],
                'apprentissages_critiques': [ac1_1, ac1_2]
            },
            {
                'title': 'Gestion des Téléchargements en Environnement à Faible Connectivité',
                'content': (
                    'Le site étant utilisé dans plusieurs régions du monde, y compris des zones avec une connexion internet instable, '
                    'une fonctionnalité d\'upload en chunks a été implémentée. Cette fonctionnalité permet d\'envoyer des segments de '
                    'fichiers et de reconstituer le fichier final, avec l\'algorithme MD5 utilisé pour vérifier l\'intégrité de chaque chunk '
                    'ainsi que du fichier complet. Cette fonctionnalité sera également étendue au téléchargement pour les mêmes raisons de fiabilité.'
                ),
                'competences': [comp6],
                'apprentissages_critiques': [ac6_1, ac6_2]
            },
            {
                'title': 'Corrections de Bugs et Améliorations Fonctionnelles',
                'content': (
                    'Dès le début de mon stage, j\'ai corrigé un maximum de bugs dans l\'application existante avant d\'entreprendre des '
                    'modifications plus importantes. Cela m\'a permis de travailler sur une base stable. J\'ai ensuite implémenté diverses '
                    'fonctionnalités, dont une barre de recherche avec autocomplétion sur la page principale.'
                ),
                'competences': [comp1],
                'apprentissages_critiques': [ac1_1, ac1_2]
            },
            {
                'title': 'Optimisation des Performances',
                'content': (
                    'Après avoir développé l\'API, j\'ai optimisé les performances du site en utilisant des outils de profilage comme Google '
                    'Lighthouse. Cette optimisation a permis d\'identifier et de corriger les points de ralentissement, améliorant ainsi '
                    'significativement les temps de chargement et la réactivité du site.'
                ),
                'competences': [comp2],
                'apprentissages_critiques': [ac2_1, ac2_2]
            },
            {
                'title': 'Tests Unitaires et Sécurité',
                'content': (
                    'Pour garantir la fiabilité de l\'application, des tests unitaires ont été réalisés sur la majorité des routes de l\'API, '
                    'utilisant les modules de test de Django. Les tests ont été particulièrement rigoureux pour les fonctionnalités critiques '
                    'comme l\'upload en chunks. De plus, chaque utilisation de l\'API nécessite une connexion, et toutes les requêtes sont loggées '
                    'pour renforcer la sécurité, bien que le site soit limité au réseau interne.'
                ),
                'competences': [comp4],
                'apprentissages_critiques': [ac4_1, ac4_2]
            },
            {
                'title': 'Collaboration et Intégration dans l\'Équipe',
                'content': (
                    'Malgré mon caractère introverti, je me suis bien intégré dans l\'équipe en partageant régulièrement mes idées et réalisations '
                    'avec les autres développeurs. J\'ai également collaboré étroitement avec Bryan, un autre développeur, pour la création et la migration '
                    'de la base de données, surmontant des défis techniques comme les problèmes d\'encodage et de casse des caractères.'
                ),
                'competences': [comp6],
                'apprentissages_critiques': [ac6_1, ac6_2]
            },
            {
                'title': 'Apprentissage et Utilisation de Django',
                'content': (
                    'Ne connaissant pas Django avant ce stage, j\'ai rapidement acquis les compétences nécessaires grâce à des tutoriels en ligne. '
                    'Mon expérience préalable avec Vue.js, Node.js, Flask, Python et Jinja a facilité mon adaptation à Django.'
                ),
                'competences': [comp1],
                'apprentissages_critiques': [ac1_1, ac1_2]
            },
            {
                'title': 'Fonctionnalités du Site Web',
                'content': (
                    'Le site web offre de nombreuses fonctionnalités :\n\n'
                    '- Page d\'accueil : Liste les 10 derniers packages, les 10 packages les plus récemment modifiés, et les 10 packages les plus référencés. '
                    'Comprend une barre de recherche avec autocomplétion.\n'
                    '- Page de recherche : Permet de visualiser et de filtrer les packages selon différents critères (groupe, tag, auteur, etc.).\n'
                    '- Pages des packages : Chaque package a sa propre page avec des options de favori, des liens vers d\'autres pages, des statistiques, '
                    'et des vues des dépendances et dépendants. Un bouton permet de générer un arbre de nœuds de dépendances ou de dépendants.\n'
                    '- Profils utilisateurs : Les utilisateurs peuvent voir tous les packages auxquels ils ont contribué, leur liste de favoris, et leurs données personnelles.'
                ),
                'competences': [comp5],
                'apprentissages_critiques': [ac5_1, ac5_2]
            },
            {
                'title': 'Gestion des Tâches et Organisation du Travail',
                'content': (
                    'Pour m\'organiser, j\'ai utilisé des post-it pour noter et trier mes tâches par priorité. Cette méthode simple mais efficace m\'a aidé '
                    'à rester organisé et à prioriser les tâches selon les besoins du projet. Tout au long du stage, j\'ai consulté Jérôme, un développeur expérimenté '
                    'de l\'équipe, pour discuter de mes idées et faire le point sur mes réalisations.'
                ),
                'competences': [comp6],
                'apprentissages_critiques': [ac6_1, ac6_2]
            },
            {
                'title': 'Conclusion',
                'content': (
                    'Ce stage m\'a permis d\'acquérir de solides compétences en développement web et en gestion de projets informatiques complexes. J\'ai également '
                    'amélioré mes capacités d\'intégration et de collaboration au sein d\'une équipe professionnelle, tout en développant une application web robuste '
                    'et performante. Les défis techniques rencontrés et surmontés ont enrichi mon expérience et m\'ont préparé à des projets encore plus complexes à l\'avenir.'
                ),
                'competences': [comp5],
                'apprentissages_critiques': [ac5_1, ac5_2]
            }
        ]

        # Create text fields and associate them with the project
        for text in texts:
            text_field = TextField.objects.create(
                project=project,
                content=text['content']
            )
            text_field.competences.set(text['competences'])
            text_field.apprentissages_critiques.set(text['apprentissages_critiques'])

        self.stdout.write(self.style.SUCCESS('Database has been populated with initial data.'))

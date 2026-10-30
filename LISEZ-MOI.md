# Entretien Ferme — projet Android

Ce dossier produit un fichier APK à installer sur ton téléphone Android.
Tu n'as rien à installer sur ton ordinateur : GitHub (gratuit) compile l'app pour toi.

## Étapes (environ 15 minutes)

1. Crée un compte gratuit sur https://github.com
2. Clique sur **+ → New repository**. Nom : `entretien-ferme`. Choisis **Private**. Crée-le.
3. Dézippe ce dossier sur ton ordinateur. Dans ton dépôt, clique **uploading an existing file**
   et glisse **tout le contenu** du dossier (www, package.json, capacitor.config.json, debug.keystore…).
4. Le dossier caché `.github` est parfois ignoré par le glisser-déposer. Vérifie qu'il apparaît dans le dépôt.
   S'il manque : **Add file → Create new file**, tape le nom `.github/workflows/build-apk.yml`
   et colle le contenu du fichier du même nom.
5. Clique **Commit changes**. Va dans l'onglet **Actions** : la compilation démarre toute seule (3 à 6 minutes).
6. Quand c'est vert, ouvre l'exécution, descends à **Artifacts** et télécharge `entretien-ferme-apk`.
   Dézippe-le : tu obtiens `app-debug.apk`.
7. Envoie l'APK sur ton téléphone (courriel, Google Drive, câble) et ouvre-le.
   Android demandera d'autoriser « l'installation d'apps inconnues » pour l'app utilisée : accepte.

## Premier lancement
- Accepte les notifications.
- ⚙ Réglages → colle ta clé Gemini (nouvelle clé, pas celle partagée dans la conversation) → Enregistrer.
- ⚙ → « Notification test » pour vérifier que les rappels fonctionnent.
- Dans une fiche d'équipement : ✨ Suggérer des entretiens → « Chercher avec Gemini ».

## À savoir
- Les données sont stockées sur le téléphone. **Fais une sauvegarde** (⚙ → Copier une sauvegarde) de temps en temps.
- Pour mettre à jour l'app : remplace des fichiers dans le dépôt, l'APK se recompile. Il s'installe par-dessus l'ancien
  sans perdre les données (la signature est fixe). Garde le dépôt **privé**.
- Les rappels : une notification à 8 h la veille/le jour de l'échéance (entretiens en jours), et un résumé quotidien à 8 h
  des entretiens à faire (3 prochains jours, recalculé à chaque ouverture de l'app).
  Les entretiens en heures sont comparés au compteur quand tu l'ouvres ou le mets à jour.
- Si la compilation échoue (croix rouge), clique sur l'étape en erreur, copie le message et envoie-le-moi.

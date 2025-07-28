# invoice-app

3. 🛠️ Dans ton terminal PowerShell
Active l’environnement virtuel :
bash
Copier
Modifier
.venv\Scripts\activate
Dis à Flask d’utiliser manage.py :
bash
Copier
Modifier
$env:FLASK_APP = "manage.py"
4. 🧪 Lance les migrations
bash
Copier
Modifier
flask db init                       # une seule fois
flask db migrate -m "Ajout des snapshots, TVA, etc."
flask db upgrade

✅ Résultat
Tu peux maintenant modifier tes modèles, et exécuter :

bash
Copier
Modifier
flask db migrate -m "Tes changements"
flask db upgrade
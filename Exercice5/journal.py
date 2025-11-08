from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self.fichier = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        horodatage = datetime.now().isoformat()
        self.fichier.write(f"{horodatage} — {tache}\n")

    def __exit__(self, exc_type, exc, tb):
        self.fichier.close()
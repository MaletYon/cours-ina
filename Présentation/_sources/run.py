"""Construit les présentations : python run.py GCI 1 3 5   (ou: python run.py GCI all)."""
import sys, os, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slides import Deck
from courses import ALL

LABS = {
    "INA": {
        "LAB-01": "Forensique système : timeline Linux et Windows",
        "LAB-02": "Forensique réseau opérationnelle : beaconing et courriel frauduleux",
        "LAB-03": "Journaux réseau sans capture : DNS, proxy, pare-feu",
        "LAB-04": "Forensique mobile : SMS, appels, EXIF",
        "LAB-05": "Forensique cloud : CloudTrail et fenêtre aveugle",
        "LAB-06": "Forensique IoT : firmware de routeur et NVR",
        "LAB-07": "OSINT : domaines, profils, cryptoactifs",
        "LAB-08": "Le rapport forensique : relecture avant dépôt",
        "LAB-09": "Anti-forensique : timestomping et journaux effacés",
        "LAB-10": "L'IA en forensique : mesurer un outil, examiner des clips",
        "LAB-11": "Conteneurs : audit Kubernetes et conteneur évincé",
        "LAB-12": "Synthèse : du dossier intégrateur à la preuve vérifiable (3 h)",
    },
}

HERE = os.path.dirname(os.path.abspath(__file__))


def load(sigle, name):
    path = os.path.join(HERE, "specs", sigle, name + ".py")
    spec = importlib.util.spec_from_file_location(f"{sigle}_{name}", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SPEC


def complete(sigle, day, spec):
    c = ALL[sigle]
    theme, contenu, ateliers, labs = c["jours"][day]
    for d in spec:
        if d["k"] == "maison":
            d.setdefault("ateliers", [f"**Atelier {a}** : fiche {sigle}-FICHE-{a}" for a in ateliers])
            d.setdefault("labs", [f"**{sigle}-{l}** : {LABS[sigle][l]}" for l in labs])
    return spec


def build_day(sigle, day):
    c = ALL[sigle]
    spec = complete(sigle, day, load(sigle, f"J{day:02d}"))
    deck = Deck(c, day)
    out = os.path.join(c["dossier"], f"{sigle}_J{day:02d}.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


def build_global(sigle):
    c = ALL[sigle]
    spec = load(sigle, "J00")
    deck = Deck(c, None)
    out = os.path.join(c["dossier"], f"{sigle}_00_vision_globale.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


if __name__ == "__main__":
    sigle = sys.argv[1]
    days = sys.argv[2:]
    if days == ["all"]:
        days = ["0"] + [str(i) for i in range(1, ALL[sigle].get("n_jours", 15) + 1)]
    for dd in days:
        if int(dd) == 0:
            build_global(sigle)
        else:
            build_day(sigle, int(dd))

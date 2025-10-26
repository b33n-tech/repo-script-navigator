import streamlit as st

# Titre de l'app
st.title("Checklist Repo GitHub Interactive")

# Zone de texte pour coller la structure du repo
repo_structure = st.text_area(
    "Collez ici la structure de votre repo (comme générée par GPT) :",
    height=300
)

def parse_structure(structure_text):
    """
    Parse le texte de structure de repo pour obtenir une liste plate de fichiers/dossiers.
    """
    items = []
    for line in structure_text.splitlines():
        line = line.strip()
        if line.startswith("├─") or line.startswith("└─"):
            # Supprime les symboles graphiques et les commentaires
            clean_line = line[2:].split("←")[0].strip()
            items.append(clean_line)
    return items

if repo_structure:
    items = parse_structure(repo_structure)
    
    st.subheader("Checklist du repo")
    checked_items = {}
    
    # Crée une case à cocher pour chaque item
    for item in items:
        checked_items[item] = st.checkbox(item, key=item)
    
    # Calcul de l'avancement
    total = len(items)
    done = sum(checked_items.values())
    st.progress(done / total if total > 0 else 0)
    
    st.write(f"✅ {done}/{total} éléments terminés")

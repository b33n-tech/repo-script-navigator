import streamlit as st

st.title("Checklist Repo GitHub Avancée")

# Zone de texte pour coller la structure
repo_structure = st.text_area(
    "Collez la structure du repo ici :",
    height=300
)

def parse_structure_by_folder(structure_text):
    """
    Transforme le texte de structure en dict {dossier: [fichiers]}.
    Les fichiers hors dossier sont sous clé "root".
    """
    structure = {}
    current_folder = "root"
    structure[current_folder] = []
    
    for line in structure_text.splitlines():
        line = line.strip()
        if line.startswith("├─") or line.startswith("└─"):
            clean_line = line[2:].split("←")[0].strip()
            # Détecte si c'est un dossier
            if clean_line.endswith("/"):
                current_folder = clean_line[:-1]  # enlève le "/"
                structure[current_folder] = []
            else:
                structure[current_folder].append(clean_line)
    return structure

if repo_structure:
    repo_dict = parse_structure_by_folder(repo_structure)
    
    st.subheader("Checklist interactive par dossier")
    total_items = 0
    total_done = 0
    
    for folder, files in repo_dict.items():
        if folder != "root":
            exp = st.expander(f"Dossier : {folder}", expanded=True)
        else:
            exp = st.container()
        
        folder_done = 0
        folder_total = len(files)
        
        with exp:
            for f in files:
                key = f"{folder}_{f}"
                checked = st.checkbox(f, key=key)
                if checked:
                    folder_done += 1
        
        # Affiche l'avancement par dossier
        if folder_total > 0:
            exp.progress(folder_done / folder_total)
            exp.write(f"✅ {folder_done}/{folder_total} fichiers terminés")
        
        total_items += folder_total
        total_done += folder_done
    
    # Avancement global
    if total_items > 0:
        st.subheader("Avancement global")
        st.progress(total_done / total_items)
        st.write(f"📊 {total_done}/{total_items} fichiers terminés dans tout le repo")

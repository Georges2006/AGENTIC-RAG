Structure d'un chunk 
Chaque enregistrement peut contenir :
- un id : identifiant unique du chunk ;
- un document : le texte du chunk ;
- des metadatas : informations sur ce chunk, par exemple source, section, spec, release ;
- un embedding : représentation numérique du texte pour la recherche sémantique ;
- parfois une URI ou d’autres données associées.

Élément / chunk
├── id
├── document
├── metadata
└── embedding

modèle par défaut de ChromaDB, qui est all-MiniLM-L6-v2.

Pour la question de l'utilisateur (Query) : Vous devez coller cette phrase exacte juste devant sa question :
"Represent this sentence for searching relevant passages: "
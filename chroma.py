import os
import chromadb

CHROMA_PATH = r"C:\Users\georg\OneDrive\Bureau\ISEP\Final Project Research\projectFINAL\chroma_3gpp_rel18"

print("Chemin utilisé :", CHROMA_PATH)
print("Existe :", os.path.exists(CHROMA_PATH))

print("\nContenu du dossier :")
for item in os.listdir(CHROMA_PATH):
    print("-", item)

client = chromadb.PersistentClient(path=CHROMA_PATH) # initialiser la connexion avec la base de données.


collections = client.list_collections() # ce qui se trouve à l'intérieur de la base de données.


print("\nNombre de collections :", len(collections))
print(collections)

#On cherhce à affiché les éléments dans la collection 
ma_collection = client.get_collection("3gpp_rel18_collection")
print(ma_collection)
print("\nNombre de chunk :" , ma_collection.count())

#10 premiers chunk de la collection
apperçu = ma_collection.peek()
print(apperçu)
print(apperçu['embeddings'].shape)
print(apperçu['embeddings'][:5]) # 384 la dimensiosn des embeddings

#On interogge la base pour evaluer la similartité
questions = ma_collection.query(
    query_texts = [ "What is a Change Request"] ,
    n_results = 3 ,
    include=["documents", "metadatas", "distances", "embeddings"]
)

print(questions)

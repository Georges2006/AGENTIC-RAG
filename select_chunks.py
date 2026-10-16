# Choise 20 chunks random with long text
import random
from chroma import ma_collection

chunks_filtres = []

total = ma_collection.count()
batch_size = 5000

for offset in range(0, total, batch_size):

    batch = ma_collection.get(
        limit=batch_size,
        offset=offset,
        include=["documents", "metadatas"]
    )

    documents = batch["documents"]
    metadatas = batch["metadatas"]
    ids = batch["ids"]

    for i, doc in enumerate(documents):
        if len(doc) > 400:
            chunks_filtres.append({
                "id": ids[i],
                "document": doc,
                "metadata": metadatas[i]
            })

print("Nombre de chunks filtrés :", len(chunks_filtres))

N_CHUNKS = 50
selection = random.sample(chunks_filtres, N_CHUNKS)

for i, chunk in enumerate(selection, start=1):
    print("=" * 80)
    print("CHUNK", i)
    print("ID :", chunk["id"])
    print("SPEC :", chunk["metadata"].get("spec"))
    print("SECTION :", chunk["metadata"].get("section"))
    print("\nDOCUMENT :")
    print(chunk["document"])
    print()
from chroma import ma_collection


data = ma_collection.get(
    limit=5000,
    include=["documents"]
)
corpus = data["documents"]





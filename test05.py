import duckdb

# On cree une relation depuis la connexion, puis on montre qu'elle n'existe plus apres fermeture.
conn = duckdb.connect(database="presidents.duckdb")

presidents_relation = conn.read_parquet("presidents.parquet")
print("Avant la fermeture :")
print(presidents_relation.limit(2))

conn.close()

print("\nApres la fermeture du cursor/connexion :")
try:
    print(presidents_relation.limit(2))
except Exception as e:
    print(type(e).__name__, e)

print("\nLa table est quand meme sauvegardee dans la base et accessible avec une nouvelle connexion :")
new_conn = duckdb.connect(database="presidents.duckdb")
print(new_conn.sql("SELECT COUNT(*) AS nb_presidents FROM presidents"))
new_conn.close()

from Bio import Entrez
import time

Entrez.email = "your_email@example.com"

query = "Cas9 AND (bacteria[Organism] OR archaea[Organism]) NOT partial AND 800:1800[SLEN]"

handle = Entrez.esearch(db="protein", term=query, retmax=50000)
record = Entrez.read(handle)
ids = record["IdList"]

print(f"Total sequences: {len(ids)}")

batch_size = 2000

for i in range(0, len(ids), batch_size):
    batch_ids = ids[i:i+batch_size]

    fetch = Entrez.efetch(
        db="protein",
        id=",".join(batch_ids),
        rettype="fasta",
        retmode="text"
    )

    filename = f"cas9_batch_{i//batch_size + 1}.fasta"

    with open(filename, "w") as f:
        f.write(fetch.read())

    print(f"Saved {filename}")

    time.sleep(0.5)

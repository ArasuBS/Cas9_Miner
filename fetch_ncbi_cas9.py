from Bio import Entrez
import time

# Always set your email
Entrez.email = "your_email@example.com"

# Your query
query = "Cas9 AND (bacteria[Organism] OR archaea[Organism]) NOT partial AND 800:1800[SLEN]"

# Step 1: get all IDs
handle = Entrez.esearch(db="protein", term=query, retmax=50000)
record = Entrez.read(handle)
ids = record["IdList"]

print(f"Total sequences: {len(ids)}")

# Step 2: batch download (smaller batch size for stability)
batch_size = 500

for i in range(0, len(ids), batch_size):
    batch_ids = ids[i:i+batch_size]

    success = False
    attempts = 0

    while not success and attempts < 3:
        try:
            fetch = Entrez.efetch(
                db="protein",
                id=",".join(batch_ids),
                rettype="fasta",
                retmode="text"
            )

            data = fetch.read()

            filename = f"cas9_batch_{i//batch_size + 1}.fasta"

            with open(filename, "w") as f:
                f.write(data)

            print(f"Saved {filename}")
            success = True

        except Exception as e:
            attempts += 1
            print(f"Retry {attempts} for batch {i//batch_size + 1}")
            time.sleep(2)

    # small delay to respect NCBI limits
    time.sleep(0.5)

print("Download complete ✅")

from Bio import SeqIO

input_file = "cas9_all_raw.fasta"
output_file = "cas9_deduplicated.fasta"

seen = set()
unique_records = []

for record in SeqIO.parse(input_file, "fasta"):
    seq = str(record.seq)
    if seq not in seen:
        seen.add(seq)
        unique_records.append(record)

print(f"Original: {len(seen)} unique sequences")

SeqIO.write(unique_records, output_file, "fasta")

print("Deduplication complete ✅")
``

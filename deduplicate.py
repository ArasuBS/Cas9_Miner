from Bio import SeqIO

input_file = "cas9_all_raw.fasta"
output_file = "cas9_deduplicated.fasta"

seen = set()
unique_records = []
total = 0

for record in SeqIO.parse(input_file, "fasta"):
    total += 1
    seq = str(record.seq)
    if seq not in seen:
        seen.add(seq)
        unique_records.append(record)

print(f"Total sequences BEFORE deduplication: {total}")
print(f"Total sequences AFTER deduplication: {len(unique_records)}")

SeqIO.write(unique_records, output_file, "fasta")

print("Deduplication complete")

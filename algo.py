#Importer le texte depuis le fichier
f = open("sequence_adn", "r")
sequence = f.read() #taille 14813
f.close()


sequence = list(sequence)
def find_motif(sequence, motif):
    indices = []
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == list(motif):
            indices.append(i)
    return indices

#2.1 Algorithme de recherche de motif

motif_to_find = "AAATTCG"
motif_indices = find_motif(sequence, motif_to_find)
print(f"L'indices du motif est '{motif_to_find}': {motif_indices}")


def compress_adn(sequence):
    compressed_sequence = []
    i = 0
    while i < len(sequence):
        count = 1
        while i < len(sequence) - 1 and sequence[i] == sequence[i + 1]:
            i += 1
            count += 1
        compressed_sequence.extend([sequence[i], str(count)])
        i += 1
    return compressed_sequence


compressed_sequence = compress_adn(sequence)
print(f" la séquence compressée est: {compressed_sequence}")
print(f" la taille de la séquence compressée est: {len(compressed_sequence)}")

def calculate_average_occurrences(occurrences):
    return sum(occurrences) / len(occurrences)

def count_single_occurrences(occurrences):
    return occurrences.count(1)

#2.2 Algorithme de compression naïf


def compression_occurrences(sequence):
    list_occurrence = []
    i = 0
    while i < len(sequence):
        count = 1
        while i < len(sequence) - 1 and sequence[i] == sequence[i + 1]:
            i += 1
            count += 1
        list_occurrence.append(count)
        i += 1
    return list_occurrence

#2.3 Le nombre de suites de caractères uniques

def calculate_average_occurrences(occurrences):
    return sum(occurrences) / len(occurrences)

def count_single_occurrences(occurrences):
    return occurrences.count(1)

occurrences = compression_occurrences(sequence)

average_occurrences = calculate_average_occurrences(occurrences)
single_occurrences_count = count_single_occurrences(occurrences)
print(f" le moyenne des occurrences successives est : {average_occurrences}")
print(f"le nombre d'occurrences successives égal à 1 est : {single_occurrences_count}")

#2.4 nouvel algorithme de compression
#la nouvelle sequence


new_sequence = sequence.copy()
for i in range(len(new_sequence) - 2):
    if new_sequence[i:i+3] == ["A", "A", "A"]:
        new_sequence[i:i+3] = ["X"]

print(f"la nouvelle séquence : {new_sequence}")
print(f"la taille de la nouvelle séquence est: {len(new_sequence)}")



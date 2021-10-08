DNA_RNA = str.maketrans('GCTA', 'CGAU')


def to_rna(dna: str) -> str:
    return dna.translate(DNA_RNA)
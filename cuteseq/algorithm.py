COMPLEMENT = {"A": "T", "C": "G", "G": "C", "T": "A"}


def reverse(seq: str) -> str:
    return "".join(reversed(seq))


def complement(seq: str) -> str:
    return "".join(COMPLEMENT[n] for n in seq)


def reverse_complement(seq: str) -> str:
    return "".join(COMPLEMENT[n] for n in reversed(seq))

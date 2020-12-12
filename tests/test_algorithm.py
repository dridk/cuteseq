from cuteseq import algorithm


def test_complement():
    """ test complement """
    assert algorithm.complement("ACGT") == "TGCA"


def test_reverse():
    """ test reverse """
    assert algorithm.reverse("ACGTTT") == "TTTGCA"


def test_reverse_complement():
    """ test reverse complement """
    assert algorithm.reverse_complement("ACGTT") == "AACGT"

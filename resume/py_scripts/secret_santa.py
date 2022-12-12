from random import shuffle
from typing import List, Tuple

def get_santa_list(participants: List[tuple]) -> List[Tuple[Tuple[str]]]:
    listi = participants
    # listi = ['Atli', 'Teitur', 'Johann', 'Danni', 'Dóri', 'Siggi', 'Elvar']
    shuffle(listi)
    # print(*[f"{listi[i]}->{listi[(i+1)%len(listi)]}" for i in range(len(listi))], sep="\n")
    # return "<br>".join([f"{listi[i]}->{listi[(i+1)%len(listi)]}" for i in range(len(listi))])
    return [(listi[i], listi[(i+1)%len(listi)]) for i in range(len(listi))]
    # return [f"{listi[i]} -> {listi[(i+1)%len(listi)]}" for i in range(len(listi))]
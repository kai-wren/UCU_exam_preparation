sequence_full = ['A','B','C','B','B','D']
sequence = ['B','C','B','D']


def compareSequences(seq, seqFull):
    
    lastHitIndex = 0
    noSeq = False
    retSeq = {}

    for s in seq:
        try:
            lastHitIndex = seqFull.index(s,lastHitIndex)
            retSeq[lastHitIndex] = s
        except ValueError:
            noSeq = True
            break
    if noSeq:
        return 'Sequence S is not part of SF!'
    else:
        return 'Sequence S part of SF. Details: ', retSeq
            
print(compareSequences(sequence, sequence_full))
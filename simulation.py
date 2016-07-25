import random

def simulate_random(turns):
    ret = 0
    current = 0
    for job in xrange(turns):
        if job % 2 == current:
           ret += 1
        else:
            current = random.randint(0, 1)
    return ret

def simulate_alternations(turns, alt_len):

    ret = 0
    cur = 0
    for job in xrange(turns):
        job = (job % (alt_len * 2)) / alt_len
        if cur == job:
            ret += 1
        else:
            cur = random.randint(0, 1)

    return ret

def simulate_sequence(turns, seq):

    ret = 0
    cur = 0
    for job in xrange(turns):
        job = seq[job % len(seq)]
        if cur == job:
            ret += 1
        else:
            cur = random.randint(0, 1)

    return ret

def simulate_multi_point_walk(cities_num, seq_length):
    seq = [random.randint(0, cities_num - 1) for j in xrange(seq_length)]
    ret = 0
    cur = 0
    for j in xrange(len(seq)):
        if seq[j] == cur:
            ret += 1
        else:
            try:
                if seq.index(seq[j], j+1) < seq.index(cur, j+1):
                    cur = seq[j]
            except:
                pass
    return ret

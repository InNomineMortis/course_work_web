from math import log2

# service function
def isint(n):
    return int(n) == float(n)


def encode(vector):
    code_Hamming = []
    len_vec = len(vector) - 1
    for i in range(7):
        if not isint(log2(i + 1)):
            code_Hamming.append(vector[len_vec])
            len_vec -= 1
        elif log2(i + 1) == 0:
            code_Hamming.append(str((int(vector[0]) + int(vector[2]) + int(vector[3])) % 2))
        elif log2(i + 1) == 1:
            code_Hamming.append(str((int(vector[0]) + int(vector[1]) + int(vector[3])) % 2))
        elif log2(i + 1) == 2:
            code_Hamming.append(str((int(vector[0]) + int(vector[1]) + int(vector[2])) % 2))

    code_Hamming.reverse()
    return code_Hamming


def decode(vector):
    syn_errors = []
    decode = []
    correct = True

    syn_errors.append((int(vector[0]) + int(vector[2]) + int(vector[4]) + int(vector[6])) % 2)
    syn_errors.append((int(vector[0]) + int(vector[1]) + int(vector[4]) + int(vector[5])) % 2)
    syn_errors.append((int(vector[0]) + int(vector[1]) + int(vector[2]) + int(vector[3])) % 2)

    decode.extend([int(vector[0]), int(vector[1]), int(vector[2]), int(vector[4])])

    if sum(syn_errors) != 0:
        correct = False

    return decode, correct

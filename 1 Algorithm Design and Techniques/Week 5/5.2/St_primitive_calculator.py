# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n //= 3
        elif n % 2 == 0:
            n //= 2
        else:
            n = n - 1
    return reversed(sequence)


def Dyn_Seq(n):
    OP_Cnt = [0] * (n + 1)

    OP_Cnt[1] = 1
    for i in range(2, n + 1):
        IND_cnt = [i - 1]
        if i % 2 == 0:
            IND_cnt.append(i // 2)
        if i % 3 == 0:
            IND_cnt.append(i // 3)

        Min_cnt = min([OP_Cnt[x] for x in IND_cnt])
        OP_Cnt[i] = Min_cnt + 1

    Val_r_nw = n
    Rem_val = [Val_r_nw]
    while Val_r_nw != 1:
        Choices_ = [Val_r_nw - 1]
        if Val_r_nw % 2 == 0:
            Choices_.append(Val_r_nw // 2)
        if Val_r_nw % 3 == 0:
            Choices_.append(Val_r_nw // 3)

        Val_r_nw = min(
            [(c, OP_Cnt[c]) for c in Choices_],
            key=lambda x: x[1]
        )[0]
        Rem_val.append(Val_r_nw)
    return reversed(Rem_val)


input = sys.stdin.read()
n = int(input)
sequence = list(Dyn_Seq(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

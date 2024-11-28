import math

def main():
    initial = '11000111101101101100101001011111001000001011111011101001010011010101000011111100010101101011101000'

    parity_indexes = [0] * math.floor(math.log(len(initial), 2) + 1)

    for i in range(0, len(parity_indexes)):
        parity_indexes[i] = 2**i - 1

    seq = [0] * (len(initial) + math.floor(math.log(len(initial), 2)) + 1)

    for i in range(0, len(seq)):
        seq[i] = -999

    initial_idx = 0

    for i in range(0, len(seq)):
        if i not in parity_indexes:
            seq[i] = initial[initial_idx]
            initial_idx += 1

    values = [0] * len(parity_indexes)

    for i in range(0,len(parity_indexes)):
        diff = parity_indexes[i] + 1
        
        passed = 0

        for j in range(parity_indexes[i], len(seq)):
            if (passed < diff):
                if (int(seq[j]) != -999):
                    values[i] += int(seq[j])

                passed += 1

            else:
                passed = 0
                j += diff

    for i in range(0, len(values)):
        values[i] %= 2
        seq[parity_indexes[i]] = values[i]

    result = ""
    t = 0

    for i in range(0, len(seq)):
        t += 1

        if (t == 4):
            t = 0
            result += str(seq[i]) + " "
            continue

        result += str(seq[i])

    print(result)

if __name__ == "__main__":
    main()

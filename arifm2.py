def main():
    word = "жидковалександрвладимирович"
    cd = len(word)
    denom = cd

    letters = {
    "и": [0, 4],
    "а": [4,7],
    "в": [7,10],
    "д": [10,13],
    "к": [13,15],
    "л": [15,17],
    "о": [17,19],
    "р": [19,21],
    "ж": [21,22],
    "е": [22,23],
    "с": [23,24],
    "н": [24,25],
    "м": [25,26],
    "ч": [26,27],
    }

    numer_left = 0
    numer_right = len(word)

    for i in range(0, len(word)):
        print("Буква: ", word[i])
        number_numer_left = letters[word[i]][0]
        number_numer_right = letters[word[i]][1]

        step = int(abs(numer_right-numer_left) / cd)

        print()

        print("Шаг: ", step)

        print()

        print("Левая грань", numer_left, " / ", denom);
        print("Правая грань", numer_right, " / ", denom);

        print()

        new_numer_left = numer_left + number_numer_left * step;
        new_numer_right = new_numer_left + abs(number_numer_left-number_numer_right) * step;

        print("Левое число", new_numer_left, " / ", denom);
        print("Правое число", new_numer_right, " / ", denom);

        denom *= cd

        numer_left = new_numer_left * 27
        numer_right = new_numer_right * 27
        print("----")


if __name__ == "__main__":
    main()

# CodeWars : https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111


def resolve_pair(col1, col2):
    if col1 == col2:
        return col2
    return "RGB".replace(col1, "").replace(col2, "")


def triangle(row):
    if len(row) == 1:
        return row
    if len(row) == 2:
        return resolve_pair(row[0], row[1])

    next = ""
    for i in range(1, len(row)):
        next += resolve_pair(row[i], row[i - 1])
    print(next)
    return triangle(next)


def main():
    str = "RGBRGBRGBRGB"

    print(str)
    print(triangle(str))


if __name__ == "__main__":
    main()

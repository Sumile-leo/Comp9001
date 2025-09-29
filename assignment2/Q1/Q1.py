import os
import sys
"""
japan.py

A program that allows a user to reforge an imperfect katana blueprint
to match a master blacksmith's perfect design. The katana is represented
using '#' for the blade, and '=' and '|' for the handle.

The program compares similarity scores, accepts or rejects katanas,
and repeatedly prompts the user to reforge the blade until it meets
the required similarity threshold.

Usage:
    python3 japan.py <imperfect_blueprint.bp> <min_similarity>
"""


def get_katana(katana: str):
    with open(katana, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines

def print_katana(bp: str):
    with open(bp, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end='')
    """
    Prints the contents of a katana blueprint file upside down.

    Parameters:
        bp (str): The filename of the katana blueprint (.bp file).
    """
    pass


def get_similarity_score(imperfect_bp: str) -> float:
    """
    Compares the blade of an imperfect katana against the perfect katana
    in perfect_katana.bp.

    Calculates and returns a similarity score between 0 and 1, where 1 means
    a perfect match. The similarity is based on the number of '#' symbols
    per line in the blade section only.

    Parameters:
        imperfect_bp (str): The filename of the imperfect katana blueprint.

    Returns:
        float: The average line similarity between the two blueprints.
    """

    lines = get_katana(imperfect_bp)

    lines_perfect = get_katana("perfect_katana.bp")

    temp = []

    for i in range(4, min(len(lines), len(lines_perfect))):
        big = max(len(lines[i]), len(lines_perfect[i]))
        small = min(len(lines[i]), len(lines_perfect[i]))
        t = small / big
        temp.append(t)

    total = sum(temp)

    return total / len(temp)

    pass


def reforge_imperfect_katana(imperfect_bp: str):
    """
    Prompts the user to reshape the blade of the imperfect katana by entering
    the number of '#' symbols for each line.

    Updates the imperfect blueprint with the new blade while keeping the handle
    intact, getting it as close as the perfect katana in perfect_katana.bp.

    Parameters:
        imperfect_bp (str): The filename of the imperfect katana blueprint.
    """

    lines = get_katana(imperfect_bp)

    temp = lines.copy()

    lines_perfect = get_katana("perfect_katana.bp")

    blade = len(lines_perfect) - 4
    max_width = len(lines_perfect[3]) - 2
    now_blade = 1

    print_bol = False

    print(">> REFORGING KATANA.")
    print()
    print(f"Katana Details:\n- Blade (lines): {blade}\n- Maximum width: {max_width}\n")
    while True:
        if now_blade == blade + 1:
            temp = [" " + item if i != 3 else item for i, item in enumerate(temp)]
            print()
            print(">> FORGING COMPLETE.")
            if input("Would you like to print the katana [yes/no]? ") == "yes":
                print()
                print_bol = True
            if print_bol:
                with open(imperfect_bp, "w", encoding="utf-8") as f:
                    f.writelines(line + "\n" for line in temp)
                print_katana(imperfect_bp)
            break
        inp_blade = input(f"Line ({now_blade}/{blade}) [{lines_perfect[now_blade + 3]}]: ")
        try:
            inp_blade = int(inp_blade)
        except ValueError:
            print("Error: Input must be an integer.")
            continue
        if not 0 < inp_blade <= max_width:
            print(f"Error: Input must be between 1 to {max_width} (inclusive).")
            continue

        temp[now_blade + 3] = "#"*inp_blade
        now_blade += 1

    pass


def main():
    """
    Runs the full katana forging simulation from start to finish.

    Handles command line arguments, loads the blueprints, checks the
    similarity score, and repeatedly prompts the user to reforge the katana
    until it meets the required threshold.
    """
    if len(sys.argv) < 3:
        print("Error: Missing arguments.")
        print(
            "Usage: python3 japan.py <imperfect_blueprint.bp> <min_similarity>")
        sys.exit(1)

    filename = sys.argv[1]
    similarity_str = sys.argv[2]

    if not filename.endswith(".bp"):
        print(
            "Error: Invalid file extension. Expected a filename ending in .bp")
        sys.exit(1)

    try:
        similarity = float(similarity_str)
    except ValueError:
        print("Error: Invalid similarity score. Expected a float value.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print(f"Error: File not found. Please check that {filename} exists.")
        sys.exit(1)

    if not (0 <= similarity <= 1):
        print("Error: Similarity score must be between 0 and 1 (inclusive).")
        sys.exit(1)

    print(">> READING IN BLUEPRINTS.")
    print()
    while True:
        print(">> ANALYSING THEIR SIMILARITY.")
        score = get_similarity_score(filename)
        print(f"Similarity score: {score:.2f}")
        if float(similarity) > score:
            print("Denied: You must reforge it.")
        else:
            print("Accepted: The blacksmith is satisfied.")
            break
        print()
        reforge_imperfect_katana(filename)
        print()



    pass


# Do not modify this!
if __name__ == '__main__':
    main()
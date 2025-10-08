import re


def license_key_formatter(license, k):
    # COMPLETE THIS FUNCTION
    clean = license.replace("-", "").upper()

    groups = []
    while clean:
        groups.insert(0, clean[-k:])
        clean = clean[:-k]

    return "-".join(groups)

def license_key_formatter2(license, k):
    s = re.sub(r'[^A-Za-z0-9]', '', license).upper()
    pattern = f"(?=(?:.{{{k}}})+$)"
    groups = re.split(pattern, s)

    return "-".join(groups)
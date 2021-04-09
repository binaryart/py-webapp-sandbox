from shortuuid import ShortUUID
from string import ascii_letters, digits


def generate_guid():
    return _su.uuid()


def _su_alphabet():
    candidates = ascii_letters + digits
    exclude_chars = [
        # removing similar-looking characters
        'l', '1', 'I', 'O', '0',
        # common English curse words
        'c', 'f', 'h', 'i', 's', 't', 'u',
    ]

    for char in exclude_chars:
        candidates = candidates.replace(char, "")

    return candidates


_su = ShortUUID(alphabet=_su_alphabet())

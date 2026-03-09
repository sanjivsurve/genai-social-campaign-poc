TRANSLATIONS = {
    "USA": "Own the court with unstoppable style",
    "Argentina": "Juega con estilo"
}


def translate(message, region):

    region = region.strip()

    if region in TRANSLATIONS:
        return TRANSLATIONS[region]

    return message
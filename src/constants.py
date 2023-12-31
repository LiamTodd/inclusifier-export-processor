import os

SINGLE_TYPE = "single"
ALL_TYPE = "all"
EXPORTS_DIR = "exports"

OUTPUT_PATH = f"{os.getcwd()}/processed_exports/processed-"
CSV_HEADERS = ["Term", "Occurrences", "Files", "Category"]


NON_INCLUSIVE_LANGUAGE_TERMS = {
    "ABLEIST LANGUAGE": [
        "crazy",
        "sane",
        "insane",
        "blind",
        "cripple",
        "dumb",
        "sanity-check",
        "sanity check",
        "dummy",
        "bonkers",
        "mad",
        "lunatic",
        "loony",
        "deficient",
        "deformed",
        "dumb",
        "gimp",
        "retarded",
        "unsighted",
        "visually challenged",
    ],
    "GENDERED LANGUAGE": [
        "man-hours",
        "man hours",
        "manhours",
        "manking",
        "male adapter",
        "female adapter",
        "guys",
        "manned",
        "man made",
        "manmade",
        "manpower",
        "man power",
        "man-power",
        "mom test",
        "grandmother test",
        "girlfriend test",
        "chairman",
        "mans",
        "salesman",
        "daughter board",
        "female connector",
        "male connector",
        "gender bender",
    ],
    "VIOLENT LANGUAGE": [
        "stonith",
        "hang",
        "hung",
        "hit",
        "abort",
        "blast radius",
        "kill",
        "nuke",
        "terminate",
    ],
    "AGEIST LANGUAGE": ["the elderly", "the aged", "seniors", "senior citizen"],
    "RACIALLY CHARGED LANGUAGE": [
        "whitelist",
        "white list",
        "white-list",
        "blacklist",
        "black list",
        "black-list",
        "native",
        "first-class citizen",
        "first class citizen",
        "master",
        "slave",
        "blackbox",
        "black box",
        "black-box",
        "whitebox",
        "white box",
        "white-box",
        "blackhole",
        "blackhat",
        "black hat",
        "black-hat",
        "whitehat",
        "white hat",
        "white-hat",
        "first-class",
        "first class",
        "ghetto",
        "gypsy",
        "primitive",
        "tribal knowledge",
        "tribal wisdom",
        "webmaster",
        "web master",
        "web-master",
        "whiteglove",
        "white glove",
        "white-glove",
        "whitelabel",
        "white label",
        "white-label",
        "quantum supremacy",
    ],
    "BIASED LANGUAGE": [
        "normal",
        "healthy",
        "health check",
        "abnormal",
        "sick",
        "disabled",
        "quadriplegic",
        "victim of",
        "suffering from",
        "wheelchair-bound",
        "physically challenged",
        "special",
        "differently abled",
        "handi-capable",
        "handicapped",
        "average user",
    ],
    "MILITARY LANGUAGE": [
        "demilitarized zone",
        "outpost",
        "war room",
        "warroom",
        "war-room",
    ],
    "OTHER": [
        "chubby",
        "denigrate",
        "fat",
        "hands on",
        "hands-on",
        "hands off",
        "hands-off",
        "jank",
        "lame",
        "monkey test",
        "ninja",
        "sexy",
        "orphaned object",
    ],
}

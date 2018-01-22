import re

MACROS = {
    "hex": '0x([0-9A-F])',
    "1-bit-num": '(0x[0-1]{{1}})',
    "3-bit-num": r'(0x[0-8]{{1}})',
    "4-bit-num": r'({hex}{{1}})',
    "9-bit-num": r'({hex}{{3}})',
    "8-bit-num": r'({hex}{{2}})',
    "16-bit-num": r"({hex}{{4}})",
    "32-bit-num": r'({hex}{{8}})',
    "320-bit-num": r'({hex}{{0,80}})'
}

COMPILED_MACROS = {}

for key, value in MACROS.items():
    val = value.format(**COMPILED_MACROS)
    COMPILED_MACROS[key] = val

FIELDS = {
    "SOURCE_PORT sourcePort": '{16-bit-num}',
    "DEST_PORT dest(tination)?Port": '{16-bit-num}',
    "PORTS ports": '{32-bit-num}',
    "SEQ_NUM seq(uence)?Number": '{32-bit-num}',
    "ACK ack(knowledgement)?Number": '{32-bit-num}',
    "OFFSET dataOffset": '{4-bit-num}',
    "RSEERVED reserved": '{3-bit-num}',
    "FLAGS flags": '{9-bit-num}',
    "WINDOW win(dow)?Size": '{16-bit-num}',
    "CHECKSUM checksum": '{16-bit-num}',
    "URGEN urgent(Pointer)?": '{16-bit-num}',
    "OPTIONS options": '{320-bit-num}',
    "DATA data": r'({hex}{{2}})+'
}

COMPILED_FIELDS = []

for key, value in FIELDS.items():
    token_type, name = key.split(' ')
    val = value.format(**COMPILED_MACROS)
    name_regex = re.compile(name)
    val_regex = re.compile(val)
    COMPILED_FIELDS.append(
      (token_type, name_regex.match, val_regex.match)
    )

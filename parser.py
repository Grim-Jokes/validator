import tcp_tokens

SAMPLE = """
{
  sourcePort: 0xFFFF;
  sourcePort: 0xFFFF;
  destinationPort: 0xFFFF;
  sequenceNumber: 0xFFFFFFFF;
  ackNumber: 0xFFFFFFFF;
  dataOffset: 0xFF;
  reserved: 0xFF;
  flags: 0x000;
  window: 0xFFFF;
  checkSum: 0xFFFFFFFF;
  urgent: 0xFFFFFFFF;
  options: 0x00;
  padding: 0xFFFFFF;
  data:0xFF0xFF0xDD
}
"""

DELIM = ':{}; ';


def validate(token_type, name, value):
    if name == 'OPTIONS':
        int(value, 16)
    pass


def show_error(tokun_type):
    if token_type == "SOURCE_PORT":
        return (
            f"{name} must be a hex value."
            "The hex value must start with 0x and be 4 digits long"
        )


parsed = {}


def parse(content=SAMPLE):
    content = content.strip()
    length = len(content)
    pos = 0
    line = 0
    column = 0

    while pos < length:
        character = content[pos]

        if character in DELIM:
            char_type = character
        elif character == '\n':
            line += 1
        else:
            for token_type, name_regex, value_regex in tcp_tokens.COMPILED_FIELDS:

                name_match = name_regex(content, pos)
                name = ''
                value = ''

                if name_match:
                    name = name_match.group()
                    pos = pos + len(name)

                    while content[pos] in DELIM:
                        pos += 1

                    match = value_regex(content, pos)

                    if match:
                        value = match.group()
                        validate(token_type, name, value)
                        pos = pos + len(name)

                        if token_type not in parsed:
                            parsed[token_type] = 'name'
                        else:
                            print(f"{name} Already defined as {parsed[token_type]}")

                    else:
                        print(
                            f"`{name}` was found on {line} but the value cannot be parsed!")

            if name and value:
                # Create tokens
                pass

        pos += 1


parse()

def convert(s):
    if not isinstance(s, list):
        raise TypeError("Argument must be a list")
# for git example
    try:
        number =''
        DIGIT_MAP =str
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversation error: {e!r}", file= sys.stderr)
        raise
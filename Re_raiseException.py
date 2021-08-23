 def convert(s):

    try:
        DIGIT_MAP=str
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
        
    except (KeyError, TypeError) as e:
        print (f"conversation error: {e!r}", file=sys.stderr)
        raise

         
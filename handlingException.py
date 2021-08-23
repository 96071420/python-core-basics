def convert(s):
  
    try:
        number =''
        DIGIT_MAP = str 
        for token in s:
            number += DIGIT_MAP[token]
            x = int(number)
            print(f"conversion failed x = {x}")
            x = -1

    except KeyError:
     print("conversaion failed")
    x = -1
    return x

  



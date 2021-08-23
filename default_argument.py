def banner(message, boader='-'):
    line = boader * len(message)
    print(line)
    print(message)
    print(line)

banner("Norwegian Blue")
banner("sun, moon and stars", "*")
banner("sun,moon and stars", boader="*")
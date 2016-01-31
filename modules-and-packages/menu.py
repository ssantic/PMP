def menu(**options):
    while True:
        choice = raw_input("Enter an option ({}) or q: ".format('/'.join(options.keys())))
        if choice == 'q':
            return None
        elif choice in option:
            return options[choice]()
        else print "Not a valid option."

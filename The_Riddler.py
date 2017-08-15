import random

day_counter = 0
alan_tickets = 0
betty_tickets = 0
charles_tickets = 0
diana_tickets = 0

drivers = ["Alan", "Betty", "Charles", "Diana"]


def head_to_work():
    if random.choice(drivers) == "Alan":
        print "Alan it's your turn."
        global alan_tickets
        if alan_tickets == 3:
            print "i cant"
            head_to_work()
        else:
            return alan_drives_tw()
    elif random.choice(drivers) == "Betty":
        print "Betty it's your turn."
        global betty_tickets
        if betty_tickets == 3:
            print "nope"
            head_to_work()
        else:
            return betty_drives_tw()
    elif random.choice(drivers) == "Charles":
        print "Charles it's your turn."
        global charles_tickets
        if charles_tickets == 3:
            print "no way"
            head_to_work()
        else:
            return charles_drives_tw()
    elif random.choice(drivers) == "Diana":
        print "Diana it's your turn."
        global diana_tickets
        if diana_tickets == 3:
            print "sorry guys"
            head_to_work()
        else:
            return diana_drives_tw()
    else:
        print "All drivers have their Licenses suspended."
        print "Take the Bus."


def alan_drives_tw():
    global alan_tickets
    print "Yo i'm driving"
    print "..."
    print "Now driving"
    if random.random() <= 0.50:
        print "your getting pulled over"
        if random.random <= 0.10:
            print "your getting a ticket"
            alan_tickets += 1
            print "i got a ticket, but we have arrived at work"
            head_home()
        else:
            print "just a warning today"
            print "we have arrived at work"
            head_home()
    else:
        print "we have arrived at work"
        head_home()


def betty_drives_tw():
    global betty_tickets
    print "Hi i'll drive"
    print "..."
    print "we outta here"
    if random.random() <= 0.50:
        print "your getting pulled over"
        if random.random() <= 0.15:
            print "your getting a ticket"
            betty_tickets += 1
            print "i got a ticket but, made it to work"
            head_home()
        else:
            print "just a warning today"
            print "made it to work"
            head_home()
    else:
        print "made it to work"
        return head_home()


def charles_drives_tw():
    global charles_tickets
    print "I'll take the wheel"
    print "..."
    print "lets roll out"
    if random.random() <= 0.50:
        print "your getting pulled over"
        if random.random() <= 0.20:
            print "your getting a ticket"
            charles_tickets += 1
            print "i got a ticket but, made it to work"
            head_home()
        else:
            print "just a warning today"
            print "made it to work"
            head_home()
    else:
        print "made it to work"
        head_home()


def diana_drives_tw():
    global diana_tickets
    print "I got it today"
    print "..."
    print "whippin it"
    if random.random() <= 0.50:
        print "your getting pulled over"
        if random.random() <= 0.25:
            print "its ticket time"
            diana_tickets += 1
            print "i got a ticket but, were here at work"
        else:
            print "just a warning today"
            print "were here at work"
            return head_home()
    else:
        print "were here at work"
        head_home()


def head_home():
    if random.choice(drivers) == "Alan":
        print "Alan it's your turn"
        global alan_tickets
        if alan_tickets == 3:
            print "i cant"
            return head_home()
        else:
            return alan_drives_h()
    elif random.choice(drivers) == "Betty":
        print "Betty it's your turn"
        global betty_tickets
        if betty_tickets == 3:
            print "nope"
            return head_home()
        else:
            return betty_drives_h()
    elif random.choice(drivers) == "Charles":
        print "Charles it's your turn"
        global charles_tickets
        if charles_tickets == 3:
            print "no way"
            return head_home()
        else:
            return charles_drives_h()
    elif random.choice(drivers) == "Diana":
        print "Diana it's your turn"
        global diana_tickets
        if diana_tickets == 3:
            print "sorry guys"
            return head_home()
        else:
            return diana_drives_h()
    else:
        print "Drivers are not eligible to drive"


def alan_drives_h():
    global alan_tickets
    global day_counter
    print "Yo i'm driving"
    print "..."
    print "Now driving"
    if random.random() <= 0.50:
        print "your getting pulled over"
        if random.random <= 0.10:
            print "your getting a ticket"
            alan_tickets += 1
        else:
            print "just a warning today"
            print "were home"
            day_counter += 1
            return head_to_work()
    else:
        print "were home"
        day_counter += 1
        head_to_work()


def betty_drives_h():
    global betty_tickets
    global day_counter
    print "Hi i'll drive"
    print "..."
    print "we outta here"
    if random.random() <= 0.50:
        print "your getting pulled over"
        if random.random() <= 0.15:
            print "your getting a ticket"
            betty_tickets += 1
        else:
            print "just a warning today"
            print "made it home"
            day_counter += 1
            return head_to_work()
    else:
        print "made it home"
        day_counter += 1
        head_to_work()


def charles_drives_h():
    global charles_tickets
    global day_counter
    print "I'll take the wheel"
    print "..."
    print "lets roll out"
    if random.random() <= 0.50:
        print "your getting pulled over"
        if random.random() <= 0.20:
            print "your getting a ticket"
            charles_tickets += 1
        else:
            print "just a warning today"
            print "made it home guys"
            day_counter += 1
            return head_to_work()
    else:
        print "made it home guys"
        day_counter += 1
        head_to_work()


def diana_drives_h():
    global diana_tickets
    global day_counter
    print "I got it today"
    print "..."
    print "whippin it"
    if random.random() <= 0.50:
        print "your getting pulled over"
        if random.random() <= 0.25:
            print "its ticket time"
        else:
            print "just a warning today"
            print "were home everyone"
            day_counter += 1
            return head_to_work()
    else:
        print "were here at home"
        day_counter += 1
        head_to_work()

print head_to_work()
print "Alan %d tikets." % (alan_tickets)
print "Betty %d tickets." % (betty_tickets)
print "Charles %d tickets." % (charles_tickets)
print "Diana %d tickets." % (diana_tickets)
print "%d days has passed." % (day_counter)

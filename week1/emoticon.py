emoticon ="v.v"



def main():
    global emoticon
    say("is anyone there i am afraid?")
    # now i want to change the emoticon to happy 
    #since it is a global variable we an modify it by stating global  emoticon
    emoticon=":D"
    say("Oh, hi?")


def say(phrase):
    print(phrase+" "+emoticon)

main()

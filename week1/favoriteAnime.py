def anime():
    show= ["naruto"," one piece",
           "    Dragon balls"," Bleach",
           "pokemon","enezuma eleven",
           " ben 10","attack on titan"]
    return show
    
def main():
    listAnime= anime()
    for items in listAnime:
        print(items.strip().title())

main()
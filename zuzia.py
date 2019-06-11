picture_konrad = 2
picture_zuzia = 1
zadowolenie = "Konradowi się bardzo podoba!"
brak_zadowolenia = "skoro nie ma, to szkoda :("

while picture_zuzia != 2:
    picture_zuzia += 1

if picture_zuzia == picture_konrad:
    print("Zuzia dodała zdjecie.")
else:
    print("Zuzia nie dodała zdjecia.")

if picture_konrad == picture_zuzia:
    print(zadowolenie)
else:
    print(brak_zadowolenia)
import re
text = open("output.html")

city_flag = False
chip_flag = False
room_flag = False
rank_flag = False
player_flag = False
end_flag = False
#flag = False
city = []
chip = []
room = []
rank = []
player = []
for line in text:
    line = text.readline()
    i = line.rfind(">") + 1
    rez = line[i:]

    if "CITY / STATE / COUNTRY" in line:
        flag = True
    if flag:
        if "CITY / STATE / COUNTRY" in line or "CHIP COUNT" in line or "ROOM / TABLE / SEAT" in line or "RANK" in line or "PLAYER" in line:
            x = 1
        else:
            if "/" in rez:
                room.append(rez)
            elif rez[0].isalpha():
                if "," in rez:
                    city.append(rez)
                else:
                    player.append(rez)
            elif rez[0].isdigit():
                if "," in rez:
                    chip.append(rez)
                else:
                    rank.append(rez)
print(x)


    if "CITY / STATE / COUNTRY" in line:
        city_flag = True
        chip_flag, room_flag, rank_flag, player_flag = False, False, False, False
    elif "CHIP COUNT" in line:
        chip_flag = True
        city_flag, room_flag, rank_flag, player_flag = False, False, False, False
    elif "ROOM / TABLE / SEAT" in line:
        room_flag = True
        city_flag, chip_flag, rank_flag, player_flag = False, False, False, False
    elif "RANK" in line:
        rank_flag = True
        city_flag, chip_flag, room_flag, player_flag = False, False, False, False
    elif "PLAYER" in line:
        player_flag = True
        city_flag, chip_flag, room_flag, rank_flag = False, False, False, False
    elif "<br></span></div><span" in line:
        end_flag = True
        city_flag, chip_flag, room_flag, rank_flag, player_flag = False, False, False, False, False

    i = line.rfind(">")

    if city_flag:
        city.append("\"" + line[i+1:] + "\"")
    elif chip_flag:
        chip.append("\"" + line[i+1:] + "\"")
    elif room_flag:
        room.append(line[i+1:])
    elif rank_flag:
        rank.append(line[i+1:])
    elif player_flag:
        player.append(line[i+1:])
    elif end_flag:
        if "Page" in line:
            print(line[i+1:], end="")
            text.readline()
        else:
            print(line[i+1:], end="")

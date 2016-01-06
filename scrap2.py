#doesnt work for the very last value
import re
text = open("output.html")

city_flag = False
chip_flag = False
room_flag = False
rank_flag = False
player_flag = False
end_flag = False
begin = False
flag_arr = [False, False, False, False, False]
current = 0
city = []
chip = []
room = []
rank = []
player = []
left = 0
badboys = []
for line in text:
    i = line.rfind(">") + 1
    rez = line[i:]

    if not begin:
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

        if city_flag:
            city.append(rez)#"\"" + rez + "\"")
        elif chip_flag:
            chip.append(rez)#"\"" + rez + "\"")
        elif room_flag:
            room.append(rez)
        elif rank_flag:
            rank.append(rez)
        elif player_flag:
            player.append(rez)
        elif end_flag:
            if "Page" in line:
                flag_arr[current] = True
                begin = True
    else:
        if "ST. LOUIS PARK, MN, US" in line:
            print("tt")
        if "<br></span></div>" in line and line[line.rfind("left")+5:100+line[100:].find("px")] != left:
            left = line[line.rfind("left")+5:100+line[100:].find("px")]
            flag_arr[current] = False
            if current == 4:
                current = -1
            current += 1
            flag_arr[current] = True

        if rez == '\n':
            x = 1
        elif flag_arr[0]:
            rank.append(rez)
        elif flag_arr[1]:
            player.append(rez)
            if "DID NOT REPORT" in line:
                badboys.append(len(player)-1)
        elif flag_arr[2]:
            if len(city) in badboys:
                city.append("")
            city.append(rez)
        elif flag_arr[3]:
            chip.append(rez)
        elif flag_arr[4]:
            room.append(rez)

for r in range(654):
    print(rank[r].strip()+"\t\t"+ player[r].strip() +"\t\t"+ city[r].strip() +"\t\t"+ chip[r].strip() +"\t\t\t"+ room[r].strip())
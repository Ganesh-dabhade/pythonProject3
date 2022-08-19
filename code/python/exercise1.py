# list sorted by team players.

famous_player=["pate,tennis",
              "sachin,cricket",
              "p.v sindhu, badminton",
              "chhatri, football"]

print(famous_player)
print(sorted(famous_player,key= lambda player:player.split(",")[0]))

# sorted by sports.

print(sorted(famous_player,key= lambda player:player.split(",")[1]))

# get top salary.
# fuction

def top_n_salaries(salaries, top_n):
    salaries_top_n1=set(salaries)
    salaries_top_n=sorted(list(salaries_top_n1), reverse=True)[0:3]
    return salaries_top_n

salaries = [
    18732.8, 12842.28, 13391.69, 14061.23,
    25509.77, 13636.95, 11841.63, 11519.12,
    16719.45, 25066.37, 12842.28, 25066.37
]

#using set
salaries_top_n=set(salaries)
print("top 3 salary")
print(sorted(list(salaries_top_n), reverse=True)[0:3])

print("using function")
print(top_n_salaries(salaries, 3))
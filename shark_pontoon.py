# https://www.codewars.com/kata/57e921d8b36340f1fd000059/python


def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    if pontoon_distance / you_speed < shark_distance / shark_speed:
        return "Alive!"
    else:
        return "Shark Bait!"

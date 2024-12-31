# 제목 : 택배 배달과 수거하기

def solution(cap, n, deliveries, pickups):
    deliveries_index = pickups_index = n - 1
    answer = 0

    while deliveries_index >= 0 or pickups_index >= 0:
        while deliveries_index >= 0 and deliveries[deliveries_index] == 0:
            deliveries_index -= 1

        while pickups_index >= 0 and pickups[pickups_index] == 0:
            pickups_index -= 1

        answer += (max(deliveries_index, pickups_index) + 1) * 2
        box = cap

        while box > 0 and deliveries_index >= 0:
            count = min(deliveries[deliveries_index], box)
            deliveries[deliveries_index] -= count
            box -= count

            if deliveries[deliveries_index] > 0:
                break

            deliveries_index -= 1

        box = 0

        while box < cap and pickups_index >= 0:
            count = min(pickups[pickups_index], cap - box)
            pickups[pickups_index] -= count
            box += count

            if pickups[pickups_index] > 0:
                break

            pickups_index -= 1

    return answer

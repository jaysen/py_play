def climbing_leaderboard(ranked, player):
    ranks = []

    for score in player:
        ranked_dict = {x: 0 for x in ranked}
        ranked_dict[score] = 0
        sorted_dict = sorted(ranked_dict, reverse=True)
        print(sorted_dict) #debug

        ranks.append(sorted_dict.index(score) + 1)
    return ranks



if __name__ == '__main__':
    ranked = [100,90,90,80]
    player = [70,80,105]

    rankings = climbing_leaderboard(ranked, player)
    print(rankings)

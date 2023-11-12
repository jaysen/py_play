# works but not all tests work in time given
def climbing_leaderboard_v1(ranked, player):
    ranks = []

    for score in player:
        ranked_dict = {x: 0 for x in ranked}
        ranked_dict[score] = 0
        sorted_dict = sorted(ranked_dict, reverse=True)
        print(sorted_dict) #debug

        ranks.append(sorted_dict.index(score) + 1)
    return ranks

# works but not all tests work in time given
def climbing_leaderboard_v2(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    rankings = []
    for score in player:
        found = False
        if score in ranked:
            rankings.append(ranked.index(score) + 1)
            continue
        for i in range(len(ranked)):
            if score > ranked[i]:
                rankings.append(i + 1)
                found = True
                break
        if not found:
            rankings.append(len(ranked) + 1)
    return rankings

def climbing_leaderboard(ranked, player):
    # Remove duplicates and sort the leaderboard in descending order
    unique_ranked = sorted(list(set(ranked)), reverse=True)
    player_ranks = []

    # The index of the last ranked player's score
    l = len(unique_ranked) - 1

    for score in player:
        # Check from the last index of unique_ranked where the player's score fits
        while (l >= 0) and (score >= unique_ranked[l]):
            l -= 1
        # Player's rank is the index + 2 (since the index is 0-based and we need to account for the next rank)
        player_ranks.append(l + 2)

    return player_ranks


if __name__ == '__main__':
    ranked = [100,90,90,80]
    player = [70,80,105]

    rankings = climbing_leaderboard(ranked, player)
    print(rankings)

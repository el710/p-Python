from os import system


if __name__ == '__main__':
    system('cls')

    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    task_total = 82
    time_avg = 45.2

    print("Using '%' string...")
    print("Members in team 'Code Masters': %s !" % team1_num)
    print("Full number of members in both team: %s and %d !" % (team1_num, team2_num))

    print("\nUsing 'format' string...")
    print("'Data Wizards' team has solved: {} tasks !".format(score_2))
    print("'Data Wizards' team has done tasks in: {0} sec !".format(team2_time))

    print("\nUsing 'f' string...")
    print(f"Both teams have solved {score_1} and {score_2} tasks.")
    print(f"Today was solved {score_1 + score_2} tasks, in average {((team1_time + team2_time) / task_total):.1f} sec per task!")

    def result():
        if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
            return '"Code Masters" team is winner'
        elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
            return '"Data Wizards" team is winner'
        else:
            return 'Draw'
    print(f"Challenge result = {result()}")



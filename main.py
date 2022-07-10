import game_data
import art
import random
#1 Generate a random pair (A and B)
#2 Compare which has higher pts (A vs B)
#3 Let user guess
#4 If user guesses correctly, 
    #4a Let B be the new A
    #4b Repeat frop line 2
#If user incorrect
    #4a Show points, end

def print_info(data: dict, intro: str=""):
    '''
    Prints information about the data.
    '''
    print(f"{intro}{data['name']}, {data['description']}, from {data['country']}.")

def print_vs(a, b, vs_logo):
    '''
    Prints versus screen with stylised "versus" using vs_logo.
    '''
    print_info(a, "A: ")
    print(vs_logo)
    print_info(b, "B: ")

def compare_followers(a: dict, b: dict):
    '''
    Returns dict whose follower_count value is higher.
    '''
    higher = 0
    if a["follower_count"] > b["follower_count"]:
        higher = a
    elif b["follower_count"] > a["follower_count"]:
        higher = b
    else:
        higher = 0 #Tie (edge-case)

    return higher

def get_random_players(n: int, l: list):
    '''
    Return a list of n random players and updated l with selected players removed.
    '''
    if n > len(l):
        return []
    
    random_players = random.sample(l, k=2)

    for player in random_players:
        l.remove(player)

    return random_players, l
        
def game(data: list):
    insta_data = data
    pair = get_random_players(2, insta_data)[0][:]
    player_a = pair[0]
    player_b = pair[1]

    user_guess = None
    user_player = None
    is_correct = True
    score = 0

    #Game loop
    while is_correct:
        print_vs(player_a, player_b, art.vs)
        winner = compare_followers(player_a, player_b)
        winner_name = winner["name"]
        winner_followers = winner["follower_count"]

        print(f"Score: {score}")
        user_guess = input(f"Who has more followers, A or B? ").lower()
        print("")
        
        if user_guess == "a":
            user_player = player_a
        elif user_guess == "b":
            user_player = player_b

        if user_player != winner:
            is_correct = False
            continue
        
        score += 1

        player_a = player_b
        #Generate new data list if user has gone through all the players.
        if not insta_data:
            insta_data = data

        player_b = get_random_players(1, insta_data)[0][0]
        
    #Lose screen
    else:
        if player_a == winner:
            loser_name = player_b["name"]
            loser_followers = player_b["follower_count"]
        else:
            loser_name = player_a["name"]
            loser_followers = player_a["follower_count"]

        print(f"You lose! {winner_name} has {winner_followers}M followers. {loser_name} only has {loser_followers}M followers!")
        
        lose_message = ""
        if score == 0:
            lose_message = f"Oh wow, {score}. You're bad."
        elif score > 10:
            lose_message = f"{score} huh. You need to go out and touch grass"
        elif score > 5:
            lose_message = f"{score} is higher than 50% of our players (trust me the stats is real)"
        elif score > 2:
            lose_message = f"You scored {score}. Meh"
        
        print(lose_message)

    # print(f"Winner is {winner_name}, with {winner_followers}M followers.")
game(game_data.data)
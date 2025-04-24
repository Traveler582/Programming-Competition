# Authors: Logan Kiernan, with assistance from: James Fox, Bernard Scott III
#
# The purpose of this program is to act as the "GameMaster" of the first ACM programming competition.
# It dynamically loads all of the Player files in the directory and runs the game, receiving whether
# each player Cooperated or Defected. It then sends the relavent data to each player, so their decisions can be
# better informed for future plays. After all of the matches are run, it prints a leaderboard along with Defection and
# Cooperation percentages
#
# To everyone participating in this competion: Congrats on making history by participating in the 
# first University of Scranton ACM Student Chapter Programming Competion! (The officers are still working on a cooler name for it)
# We wish you the best of luck, may the odds be ever in your favor, and
# may the best programmer win! :)

# These are declared as constants to simplify the data being sent to each player. noOp is really only used for the first game
# as no player has made any decisions, and thus is unable to use previous rounds to extrapolate data
import importlib.util
import os
import random
from itertools import combinations

#These constants are defined to simplify the data sent to each player
defect = False
cooperate = True

#rounds = 100 + random.randint(100, 400)
rounds = 10


def load_submissions(file_path):
    spec = importlib.util.spec_from_file_location("submission", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "player"):
        raise AttributeError(f"{file_path} missing required class 'player'")

    return module

class SubmissionManager:
    def __init__(self, submission_dir, batch_size=3):
        self.submission_dir = submission_dir
        self.batch_size = batch_size
        self.files = [os.path.join(submission_dir, f) for f in os.listdir(submission_dir)
                      if f.endswith(".py")]

    def load(self, file_path):
        module = load_submissions(file_path)
        return module.player  # Return the class (not an instance)

    def run_batches(self):
        for i in range(0, len(self.files), self.batch_size):
            group = self.files[i:i + self.batch_size]
            file_paths = group
            player_classes = [self.load(p) for p in group]
            yield list(zip(file_paths, player_classes))  # Zip file_paths and player_classes together




def run_game(player_instances, file_paths):
    last_moves = [None] * len(player_instances)
    

    points = [0] * len(player_instances)  # Initialize points list dynamically based on player count

    for _ in range(rounds):
        current_moves = []
        for index, player in enumerate(player_instances):
            try:
                decision = player.play(list(last_moves))
            except Exception as e:
                print(f"Player {index} errored: {e}")
                decision = False  # If the player has an error, assume defection
            current_moves.append(decision)

        cooperations = current_moves.count(True)

        if cooperations == len(player_instances):  # All Cooperate
            currentPoints = [4] * len(player_instances)
        elif cooperations == len(player_instances) - 1:  # 2 Cooperate, 1 Defects
            currentPoints = [0 if m else 10 for m in current_moves]
        elif cooperations == 1:  # One cooperates, two defect
            currentPoints = [0 if m else 2 for m in current_moves]
        else:  # No cooperation
            currentPoints = [1] * len(player_instances)

        for i in range(len(player_instances)):
            points[i] += currentPoints[i]

        last_moves = current_moves

    max_score = max(points)
    winners = [i for i, s in enumerate(points) if s == max_score]

    # Use the correct number of file paths
    for i in winners:
        print(f"{file_paths[i]} wins!")

    return points, winners

def print_leaderboard(stats):
    print("\n===  Final Leaderboard  ===")
    sorted_leaderboard = sorted(stats.items(), key=lambda x: x[1]['wins'], reverse=True)

    print(f"{'Player':<30} {'Wins':<5} {'Ties':<5} {'Cooperate %':<12} {'Defect %':<10}")
    print("-" * 70)
    for file_name, data in sorted_leaderboard:
        total_moves = data['cooperates'] + data['defects']
        coop_pct = (data['cooperates'] / total_moves * 100) if total_moves else 0
        defect_pct = (data['defects'] / total_moves * 100) if total_moves else 0
        print(f"{os.path.basename(file_name):<30} {data['wins']:<5} {data['ties']:<5} {coop_pct:>10.2f}%   {defect_pct:>7.2f}%")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    submission_dir = './FilePath' #<LK>: Change this with the File Path for the folder where the solution(s) is
    manager = SubmissionManager(submission_dir)

    all_files_and_classes = [(file_path, cls) for batch in manager.run_batches() for file_path, cls in batch]

    # Initialize stats tracking
    stats = {
        file_path: {
            'wins': 0,
            'cooperates': 0,
            'defects': 0,
            'ties': 0,
        } for file_path, _ in all_files_and_classes
    }

    
    for trio in combinations(all_files_and_classes, 3):
        file_paths, player_classes = zip(*trio)
        players = [cls(index) for index, cls in enumerate(player_classes)]

        print(f"\n=== Running Game: {file_paths[0]}, {file_paths[1]}, {file_paths[2]} ===")

        # Track individual moves for leaderboard
        move_history = {fp: [] for fp in file_paths}

        def tracking_run_game(player_instances, file_paths):
            last_moves = [None] * len(player_instances)
            
            points = [0] * len(player_instances)

            for _ in range(rounds):
                current_moves = []
                for index, player in enumerate(player_instances):
                    try:
                        move = player.play(list(last_moves))
                    except Exception as e:
                        print(f"Player {index} errored: {e}")
                        move = False
                    current_moves.append(move)

                for i, move in enumerate(current_moves):
                    if move is True:
                        stats[file_paths[i]]['cooperates'] += 1
                    elif move is False:
                        stats[file_paths[i]]['defects'] += 1

                cooperations = current_moves.count(True)

                if cooperations == len(player_instances):
                    currentPoints = [4] * len(player_instances)
                elif cooperations == len(player_instances) - 1:
                    currentPoints = [0 if m else 10 for m in current_moves]
                elif cooperations == 1:
                    currentPoints = [0 if m else 5 for m in current_moves]
                else:
                    currentPoints = [1] * len(player_instances)

                for i in range(len(player_instances)):
                    points[i] += currentPoints[i]

                last_moves = current_moves

            max_score = max(points)
            winners = [i for i, s in enumerate(points) if s == max_score]

            if len(winners) > 1:
                for i in winners:
                    stats[file_paths[i]]['ties'] += 1

            for i in winners:
                stats[file_paths[i]]['wins'] += 1

            return points, winners

        points, winners = tracking_run_game(players, file_paths)

    # Print stats at the end
    print_leaderboard(stats)
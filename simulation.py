import random

# ── Settings based on REAL dataset analysis ────────────
# Dataset: Online Gaming Behaviour (40,034 players)
# Average sessions per week: 9.5
# Average play time: 12 hours
# Most popular genre: Sports

SERVER_CAPACITY = 10      # server handles 10 players at once
TOTAL_PLAYERS   = 50      # simulate 50 players
MIN_WAIT        = 1       # min wait time in minutes
MAX_WAIT        = 15      # max wait time in minutes
AVG_SESSION     = 12      # average session = 12 hours (from dataset)
PEAK_ARRIVAL    = 15      # peak hour: 15 players arrive per minute

# ── Simulation ─────────────────────────────────────────
print("=" * 50)
print("     GAME SERVER QUEUE SIMULATION")
print("     Based on Real Gaming Dataset")
print("     Total Dataset Players: 40,034")
print("=" * 50)

queue        = []
in_match     = []
wait_times   = []
joined_count = 0

for player_id in range(1, TOTAL_PLAYERS + 1):
    wait = 0

    if len(in_match) >= SERVER_CAPACITY:
        wait = random.randint(MIN_WAIT, MAX_WAIT)
        queue.append(player_id)
        print(f"Player {player_id:>3} | WAITING | Wait: {wait} min")
    else:
        in_match.append(player_id)
        joined_count += 1
        print(f"Player {player_id:>3} | JOINED  | Wait: 0 min")

    wait_times.append(wait)

    if player_id % (SERVER_CAPACITY * 3) == 0:
        in_match.clear()

# ── Results ────────────────────────────────────────────
print("=" * 50)
print("            SIMULATION RESULTS")
print("=" * 50)
print(f"Total Players Simulated : {TOTAL_PLAYERS}")
print(f"Server Capacity         : {SERVER_CAPACITY}")
print(f"Players Joined Directly : {joined_count}")
print(f"Players Who Waited      : {sum(1 for w in wait_times if w > 0)}")
print(f"Average Wait Time       : {sum(wait_times)/len(wait_times):.2f} min")
print(f"Max Wait Time           : {max(wait_times)} min")
print(f"Min Wait Time           : {min(wait_times)} min")
print(f"Avg Session Duration    : {AVG_SESSION} hours (from dataset)")
print("=" * 50)
print("Simulation Complete!")
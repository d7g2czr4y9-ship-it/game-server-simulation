import random

# ── Settings based on REAL dataset ─────────────────
SERVER_CAPACITY  = 10    # max players per match
TOTAL_PLAYERS    = 50    # players to simulate
MIN_MATCH_TIME   = 5     # min match duration (minutes)
MAX_MATCH_TIME   = 30    # max match duration (minutes)
MIN_WAIT         = 1     # min queue wait (minutes)
MAX_WAIT         = 15    # max queue wait (minutes)

print("=" * 55)
print("      GAME SERVER QUEUE SIMULATION")
print("      Based on Real Dataset: 40,034 players")
print("=" * 55)

server_slots  = []   # list of (player_id, match_end_time)
wait_times    = []
joined_count  = 0
waited_count  = 0
current_time  = 0    # simulation clock in minutes

for player_id in range(1, TOTAL_PLAYERS + 1):
    current_time += random.randint(1, 3)  # player arrives every 1-3 mins

    # Remove players whose match has ended
    server_slots = [(p, t) for p, t in server_slots if t > current_time]

    if len(server_slots) >= SERVER_CAPACITY:
        # Server full — player waits
        wait = random.randint(MIN_WAIT, MAX_WAIT)
        wait_times.append(wait)
        waited_count += 1
        print(f"Player {player_id:>3} | ⏳ WAITING | Wait: {wait} min | Server: {len(server_slots)}/{SERVER_CAPACITY} full")
    else:
        # Server has space — player joins immediately
        match_duration = random.randint(MIN_MATCH_TIME, MAX_MATCH_TIME)
        match_end = current_time + match_duration
        server_slots.append((player_id, match_end))
        wait_times.append(0)
        joined_count += 1
        print(f"Player {player_id:>3} | ✅ JOINED  | Wait: 0 min | Match ends at: {match_end} min")

# ── Results ─────────────────────────────────────────
print("=" * 55)
print("              SIMULATION RESULTS")
print("=" * 55)
print(f"Total Players Simulated : {TOTAL_PLAYERS}")
print(f"Server Capacity         : {SERVER_CAPACITY}")
print(f"Players Joined Directly : {joined_count}")
print(f"Players Who Waited      : {waited_count}")
print(f"Average Wait Time       : {sum(wait_times)/len(wait_times):.2f} min")
print(f"Max Wait Time           : {max(wait_times)} min")
print(f"Total Simulation Time   : {current_time} minutes")
print("=" * 55)
print("Simulation Complete!")
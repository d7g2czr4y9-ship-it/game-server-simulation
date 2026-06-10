import random
# Peak hours simulation - models real game server behaviour
# Similar to bank queue taught in Simulation & Modelling class
# ── Settings ──────────────────────────────
SERVER_CAPACITY = 8      # max players in a match
TOTAL_PLAYERS   = 50      # players we will simulate
MIN_WAIT        = 1       # min seconds to wait
MAX_WAIT        = 10      # max seconds to wait
#scenario label
SCENARIO = "peak hours - high player load"
# ── Simulation ────────────────────────────
print("=" * 40)
print("  GAME SERVER QUEUE SIMULATION")
print(f"scenario : {SCENARIO}")
print("=" * 40)

queue        = []
in_match     = []
wait_times   = []
joined_count = 0

for player_id in range(1, TOTAL_PLAYERS + 1):
    wait = 0

    # If server is full, player waits
    if len(in_match) >= SERVER_CAPACITY:
        wait = random.randint(MIN_WAIT, MAX_WAIT)
        queue.append(player_id)
        print(f"Player {player_id} | Status: WAITING | Wait Time: {wait}s")
    else:
        in_match.append(player_id)
        joined_count += 1
        print(f"Player {player_id} | Status: JOINED  | Wait Time: 0s")

    wait_times.append(wait)

    # After every 5 players, free up the server
    if player_id % (SERVER_CAPACITY * 3) == 0:
        in_match.clear()

# ── Results ───────────────────────────────
print("=" * 40)
print(f"Total Players    : {TOTAL_PLAYERS}")
print(f"Server Capacity  : {SERVER_CAPACITY}")
print(f"Players Waited   : {sum(1 for w in wait_times if w > 0)}")
print(f"players joined : {joined_count}")
print(f"Average Wait Time: {sum(wait_times) / len(wait_times):.2f}s")
print(f"Min Wait Time    : {min(wait_times)}s")
print("=" * 40)
print("simulation complete!")
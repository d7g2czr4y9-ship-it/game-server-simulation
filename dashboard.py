import streamlit as st
import time
import random

st.set_page_config(page_title="Game Server Simulation", layout="wide")
st.title("🎮 Game Server Queue Simulation")
st.caption("Based on real data from 40,034 players | UMT Lahore 2026")

SERVER_CAPACITY = 5   # reduced so queue forms faster
TOTAL_PLAYERS = 30

if st.button("▶ Start Live Simulation", type="primary"):

    server = {}    # player_id -> seconds remaining
    queue = []     # (player_id, wait_seconds)
    log = []
    second = 0

    # Players arrive every 2 seconds — faster than matches end
    arrival_schedule = {i * 2: i + 1 for i in range(TOTAL_PLAYERS)}

    col1, col2, col3 = st.columns(3)
    server_box = col1.empty()
    queue_box = col2.empty()
    log_box = col3.empty()
    timer_box = st.empty()

    arrived_count = 0

    while arrived_count < TOTAL_PLAYERS or queue or server:
        second += 1

        # New player arrives?
        if second in arrival_schedule:
            pid = arrival_schedule[second]
            arrived_count += 1

            if len(server) < SERVER_CAPACITY:
                match_time = random.randint(15, 40)  # longer matches = more waiting
                server[pid] = match_time
                log.append(f"✅ P{pid} JOINED match ({match_time}s)")
            else:
                wait_time = random.randint(10, 25)
                queue.append([pid, wait_time])
                log.append(f"⏳ P{pid} added to QUEUE (wait: {wait_time}s)")

        # Finish matches
        finished = [p for p, t in server.items() if t <= 0]
        for p in finished:
            del server[p]
            log.append(f"🏁 P{p} match ENDED — slot freed!")

            if queue:
                next_pid, _ = queue.pop(0)
                match_time = random.randint(15, 40)
                server[next_pid] = match_time
                log.append(f"🚀 P{next_pid} moved queue → SERVER (match: {match_time}s)")

        # Count down timers
        server = {p: t - 1 for p, t in server.items()}
        queue = [[p, max(0, t - 1)] for p, t in queue]

        # Server display
        s_text = "### 🖥️ Server (In Match)\n"
        if server:
            for p, t in server.items():
                mins = t // 60
                secs = t % 60
                bar = "🟢" * min(t // 5, 8)
                s_text += f"**Player {p}** {bar}\n`{mins:02d}:{secs:02d}` left\n\n"
        else:
            s_text += "*No active matches*"
        server_box.markdown(s_text)

        # Queue display
        q_text = "### ⏳ Waiting Queue\n"
        if queue:
            for i, (p, t) in enumerate(queue):
                mins = t // 60
                secs = t % 60
                q_text += f"**#{i+1} Player {p}** — `{mins:02d}:{secs:02d}` wait\n\n"
        else:
            q_text += "*Queue is empty ✅*"
        queue_box.markdown(q_text)

        # Log display
        l_text = "### 📋 Live Events\n"
        for entry in log[-12:]:
            l_text += f"{entry}\n\n"
        log_box.markdown(l_text)

        # Timer
        timer_box.markdown(f"⏱️ **Time: {second}s** | 🖥️ In Match: {len(server)}/{SERVER_CAPACITY} | ⏳ Queue: {len(queue)}")

        time.sleep(1)

        if arrived_count >= TOTAL_PLAYERS and not queue and not server:
            break

    st.success("🎉 Simulation Complete!")
    st.balloons()
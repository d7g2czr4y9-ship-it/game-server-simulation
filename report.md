# Game Server Queue Simulation - Project Report
## Student: Khadija Ghaffar | UMT Lahore | 2026

## 1. Introduction
This project simulates a game server matchmaking queue
using Discrete Event Simulation (DES). The simulation
is based on real data from 40,034 players.

## 2. Dataset Analysis
- Source: Kaggle - Online Gaming Behaviour Dataset
- Total Records: 40,034 players
- Average Age: 32 years
- Average Play Time: 12 hours
- Average Sessions Per Week: 9.5
- Most Popular Genre: Sports
- Most Common Location: USA
- High Engagement Players: 25.8%

## 3. Simulation Design
- Entity: Player
- Resource: Game Server (capacity: 10)
- Events: Arrive, Wait, Join, Match End
- State Variables: Queue length, Server status

## 4. Results
- 50 players simulated
- Players who joined directly: varies
- Players who waited: varies
- Average wait time: 3-5 minutes
- Peak hours cause longer queues

## 5. Conclusion
The simulation shows that when player arrival rate
exceeds server capacity, queues form and wait times
increase — exactly like real game servers such as
PUBG, Valorant and Free Fire.
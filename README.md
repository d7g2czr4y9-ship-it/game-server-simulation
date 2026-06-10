# Game Server Queue Simulation

A Discrete Event Simulation of a game server matchmaking queue.
Based on real data analysis of 40,034 players.

## Dataset Analysis (Kaggle Notebook)
https://www.kaggle.com/code/khadijaghaffar/notebooka233fafc08

Graphs included:
- Most Popular Game Genres
- Age Distribution of Players
- Player Engagement Levels
- Play Time Hours Distribution
- Sessions Per Week Analysis

## What the Simulation Does
- Simulates players arriving at a game server
- Models queue formation when server is full
- Tracks wait times for each player
- Based on real dataset values (avg 12hr session, 9.5 sessions/week)

## How to Run
python3 simulation.py

## Key Results from Dataset
- Total Players Analyzed: 40,034
- Average Age: 32 years
- Average Play Time: 12 hours
- Average Sessions Per Week: 9.5
- Most Popular Genre: Sports
- High Engagement Players: 25.8%

## Simulation Results
- Server Capacity: 10 players
- When arrival rate exceeds capacity, queue forms
- Peak hours cause average wait of 3-5 minutes
- Matches real world behaviour of PUBG, Valorant, Free Fire

## Course
Simulation and Modelling — UMT Lahore 2026
Student: Khadija Ghaffar
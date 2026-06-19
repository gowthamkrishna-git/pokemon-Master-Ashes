# ⚡ Pokémon Master Ashes

## Become the Pokémon Master

A text-based Pokémon adventure built using **Python conditional statements, loops, functions, dictionaries, lists, randomization, and battle mechanics**.

Travel across the Johto region, earn gym badges, build your team, defeat your rival **Garry**, and claim the legendary title:

# 🏆 POKÉMON MASTER

---

# 📖 Story

In the peaceful region of **Johto**, a young trainer named **Gowtham** dreams of becoming the greatest Pokémon trainer ever.

Unlike most trainers, Gowtham does not begin his journey alone.

His first and closest companion is **Pikachu** — a loyal partner who stands beside him through every victory and defeat.

From childhood, Gowtham dreamed of:

* Exploring unknown regions
* Capturing powerful Pokémon
* Building an unstoppable team
* Becoming Johto Champion

But there is one obstacle.

His lifelong rival…

## ⚔️ Garry

Garry is talented, strategic, and determined.

Every battle between Gowtham and Garry pushes both trainers closer to their limits.

To prove himself worthy of the title, Gowtham must:

✔ Defeat every gym
✔ Earn every badge
✔ Build a powerful team
✔ Face Garry in the Johto League

Only one trainer can become champion.

Will Gowtham achieve his dream?

---

# 🎮 Game Features

## Core Gameplay

* Text-based Pokémon simulator
* Decision-based navigation
* Turn-based battle system
* Move cooldown mechanics
* Persistent HP system
* Random enemy move selection
* Badge progression
* Final championship battle

---

# 🗺 World Map

```
            NORTH
         Water Gym
              ↑

WEST ← Johto City → EAST
Grass Gym      Stone Gym

              ↓
         Fire Gym
            SOUTH
```

Spawn Point:

```
Johto City
```

---

# 🏅 Gym System

Each gym contains:

* 3 Enemy Pokémon
* 3 vs 3 Battle
* Unique attacks
* Random attack choices
* Move cooldown system

Badges earned:

1. Rock Badge
2. Grass Badge
3. Water Badge
4. Fire Badge

Collect all badges to unlock:

🏆 JOHTO LEAGUE

---

# ⚔ Battle Rules

## Team Rules

Gym Battle:

```
Player → 3 Pokémon
Gym → 3 Pokémon
```

League Battle:

```
Player → 3 Pokémon
Garry → Random 3 Pokémon
```

---

## Pokémon Selection Rules

✅ No duplicate Pokémon allowed

Example:

Correct:

```
Pikachu
Charizard
Tyranitar
```

Wrong:

```
Pikachu
Pikachu
Pikachu
```

---

## HP Rules

If your Pokémon wins:

✔ Remaining HP carries into next battle

Example:

```
Pikachu:
100 HP

Wins with:
38 HP

Starts next fight:
38 HP
```

---

## Faint Rules

If Pokémon HP reaches:

```
0
```

It faints.

You must choose another available Pokémon.

Fainted Pokémon cannot return.

---

## Move Cooldown Rules

After using a move:

You must use:

```
2 different moves
```

before using that move again.

Example:

Valid:

```
Thunderbolt
Quick Attack
Iron Tail
Thunderbolt
```

Invalid:

```
Thunderbolt
Quick Attack
Thunderbolt
```

Enemy Pokémon follow the same cooldown rules.

---

# 👑 Final Boss — Garry

After collecting all badges:

Enter:

```
league
```

Garry randomly selects:

* 3 Pokémon
* Different moves
* Different damage
* Cooldown system enabled

Each League run is unique.

---

# 💀 Failure Conditions

If Garry defeats you:

❌ All badges are removed

You must restart from:

```
Stone Gym
```

and collect badges again.

---

# 🏆 Victory Conditions

Defeat Garry and:

```
YOU DEFEATED GARRY

YOU ARE THE JOHTO LEAGUE CHAMPION

POKÉMON MASTER TITLE ACHIEVED

GAME OVER
```

The adventure ends.

---

# ▶ Commands

Move Commands:

```
east
west
north
south
league
exit
```

---

# 🛠 Technologies Used

* Python
* Conditional Statements
* Loops
* Functions
* Lists
* Dictionaries
* Random Module
* Terminal Interface

---

# 🚀 Run The Game

Install Python:

```bash
python3 --version
```

Run:

```bash
python3 main.py
```

---

# ⭐ Developer

Created by:

**Gowtham**

Trainer • Explorer • Future Pokémon Master

With his trusted companion:

⚡ Pikachu

"Every champion starts with a single battle."

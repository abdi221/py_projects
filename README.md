# 🐍 Python Project Roadmap — 2-Month Guide
**4–5 hours/day · 1 hour reserved for documentation · 23 projects**

---

## How to Use This Guide
Each project entry has:
- **🎯 Objective** — what you're building and why
- **🚫 Anti-goals** — what to consciously avoid (keeps scope tight)
- **📚 Warm-up tasks** — smaller practice exercises to do *before* the project
- **🔧 Core concepts to master** — the Python tools/modules you'll need
- **🔍 Deepen your understanding** — what to look up after the project works
- **🧪 Experiments** — things to try once the basic version is done

---

## 📅 Weekly Structure (Repeat Every Week)

| Day | Focus |
|-----|-------|
| Mon–Fri | Build, experiment, document |
| Saturday | Review the week. Refactor one old project. Fix bad habits. |
| Sunday | Explore one concept deeper (a YouTube video, a docs page, a chapter) |

Your 1-hour documentation block should be a `notes.md` file per project. Write: what you built, what confused you, what you'd do differently.

---

## WEEK 1 — Python Foundations via Games

**Core Skills This Week:** variables, input/output, conditionals, loops, random module, functions

---

### Project 1 — Number Guessing Game

**🎯 Objective:** The computer picks a random number (e.g. 1–100). The user guesses until they get it right. Each wrong guess gets a "too high" or "too low" hint. Track how many attempts it took.

**🚫 Anti-goals:**
- Don't add a GUI yet
- Don't crash if the user types a word instead of a number (handle this gracefully)
- Don't hardcode the secret number

**📚 Warm-up tasks (do these first, 30–60 min):**
1. Write a program that prints "Hello, [name]!" using `input()`
2. Write a program that generates 5 random numbers between 1 and 50 and prints them
3. Write a `while` loop that counts from 1 to 10, then from 10 to 1

**🔧 Core concepts:**
- `import random` → `random.randint(a, b)`
- `int(input(...))` — converting strings to integers
- `while` loops with a `break` condition
- `if / elif / else` chains
- A counter variable for attempts

**🔍 Deepen your understanding:**
- What is the difference between `break` and `continue` in a loop?
- Look up `try / except` — how would you use it to handle bad input (like someone typing "abc")?
- What is `random.choice()` vs `random.randint()`?

**🧪 Experiments:**
- Add a difficulty setting (easy = 1–50, hard = 1–500)
- Add a maximum number of guesses. If exceeded, the player loses
- Print the percentage accuracy at the end (correct guess / total guesses)

---

### Project 2 — Word Guessing Game

**🎯 Objective:** Pick a random word from a list. The user guesses the word one letter at a time. Show how many letters match. The player has limited attempts.

**🚫 Anti-goals:**
- Don't worry about reading words from a file yet — a hardcoded list is fine
- Don't build a full Hangman yet (that's next)

**📚 Warm-up tasks:**
1. Create a list of 10 animals. Print a random one.
2. Loop through a string letter by letter and print each one
3. Check if a letter exists in a word using the `in` keyword

**🔧 Core concepts:**
- `list`, indexing, `random.choice()`
- String iteration: `for char in word`
- `str.lower()` — make comparison case-insensitive
- Tracking correct guesses with a list or set

**🔍 Deepen your understanding:**
- What is a Python `set`? How does it differ from a `list`?
- What does `'_'.join(...)` do? (useful for displaying progress)
- Look up list comprehensions — they'll simplify some of your code here

**🧪 Experiments:**
- Show a running display like `_ p p _ e` as guesses come in
- Penalise duplicate guesses (same letter twice)
- Load words from a `.txt` file instead of a hardcoded list

---

### Project 3 — Hangman Game

**🎯 Objective:** Classic Hangman. Random word from a list. Show underscores for unguessed letters. Each wrong guess adds a body part to the "hanged man" (printed as ASCII art). Win by guessing all letters, lose after 6 wrong guesses.

**🚫 Anti-goals:**
- The ASCII art doesn't have to be beautiful — simple is fine
- Don't accept multi-letter inputs as valid guesses

**📚 Warm-up tasks:**
1. Make a dictionary `{ 0: "head", 1: "body", 2: "left arm" ... }` and print each stage
2. Write a function that takes a word and a list of guessed letters and returns the masked string (e.g. `"h_ng__n"`)

**🔧 Core concepts:**
- Functions (define them with `def`, pass arguments, return values)
- Dictionaries for storing hangman stages
- Separating logic into functions: `display_board()`, `check_win()`, `get_guess()`
- Using `set` for guessed letters to avoid duplicates

**🔍 Deepen your understanding:**
- What is *scope* in Python? Why can't a variable inside a function be seen outside?
- What is a *pure function* vs a function with side effects?
- Look up `string.ascii_lowercase` — useful for validating single-letter input

**🧪 Experiments:**
- Add a category hint (animal, food, country)
- Add a high score tracker (fewest wrong guesses wins)
- Accept `?` as input to reveal a random letter (one-time hint)

---

### Project 4 — 21 Number Game (Blackjack-lite)

**🎯 Objective:** Players take turns drawing a random number (1–11). The goal is to get as close to 21 as possible without going over. You vs the computer. Computer draws until it hits 17+. Closest to 21 without busting wins.

**🚫 Anti-goals:**
- No suits or a real card deck needed — just random numbers
- No real money simulation
- Don't make it multiplayer network-based

**📚 Warm-up tasks:**
1. Simulate a coin flip 1000 times and count heads vs tails
2. Write a function that adds a random number to a total and checks if it exceeds 21

**🔧 Core concepts:**
- Game loop structure (`while playing`)
- Simulating simple AI: the computer follows a rule ("draw if total < 17")
- Functions for each player's turn
- Boolean flags (`player_bust = True`)

**🔍 Deepen your understanding:**
- What is a *game loop*? Search for "game loop pattern Python"
- What is the difference between `and`, `or`, and `not`? Write truth tables for all three

**🧪 Experiments:**
- Let the user bet a virtual currency amount each round
- Track wins/losses across multiple rounds
- Add a double-down option (one more card, bet doubles)

---

### Project 5 — Rock Paper Scissors

**🎯 Objective:** User types rock, paper, or scissors. Computer picks randomly. Apply the rules. Display the result. Track score across multiple rounds.

**🚫 Anti-goals:**
- Don't accept invalid inputs silently — prompt again
- Don't write a long chain of `if/elif/elif/elif` when a dictionary can do it cleaner

**📚 Warm-up tasks:**
1. Create a dictionary `wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}` and print what each beats
2. Write a function that takes two choices and returns `"win"`, `"lose"`, or `"tie"`

**🔧 Core concepts:**
- Dictionary-based logic (cleaner than long if-chains)
- Input validation with a `while True` loop
- Separating game logic from display logic

**🔍 Deepen your understanding:**
- What is the *Single Responsibility Principle*? Why should `check_winner()` not also print the result?
- Look up Python f-strings — practise them here

**🧪 Experiments:**
- Add Rock Paper Scissors Lizard Spock
- Play best-of-5 and declare an overall winner
- Save the score to a text file and load it next time

---
## 📅 Weekly Structure (Repeat Every Week)

| Day | Focus |
|-----|-------|
| Mon–Fri | Build, experiment, document |
| Saturday | Review the week. Refactor one old project. Fix bad habits. |
| Sunday | Explore one concept deeper (a YouTube video, a docs page, a chapter) |
---

## WEEK 2 — Logic-Heavy Games + OOP Foundations

**Core Skills This Week:** lists/2D lists, dictionaries, basic OOP (`class`, `__init__`, methods), file basics

---

### Project 10 — Mastermind Game

> *Doing this before projects 6–9 because it uses only logic, no libraries.*

**🎯 Objective:** The computer picks a secret 4-digit code (digits 1–6, no repeats). The player guesses. After each guess, tell them how many digits are: correct value AND position ("black peg"), correct value but wrong position ("white peg"). Player has 10 tries.

**🚫 Anti-goals:**
- Don't show the secret code during the game
- Don't accept codes with invalid digits silently

**📚 Warm-up tasks:**
1. Write a function that counts how many elements two lists have in common (regardless of position)
2. Write a function that compares two lists element-by-element and counts exact matches

**🔧 Core concepts:**
- List comparison logic
- Generating a random code with `random.sample()` (no repeats!)
- Breaking the checking logic into its own function

**🔍 Deepen your understanding:**
- What is `random.sample()` and how is it different from `random.choices()`?
- Search "Mastermind algorithm" — how would a computer *solve* this game optimally?

**🧪 Experiments:**
- Allow repeats as a harder mode
- Add a hint system that reveals one correct position
- Track average guesses over 10 games and display stats

---

### Project 12 — Flames Game

**🎯 Objective:** Classic teen game. Take two names, remove common letters, count remaining letters. Use that count to cycle through F-L-A-M-E-S, eliminating one letter each round. The last letter standing is the "relationship" result.

**🚫 Anti-goals:**
- Case sensitivity shouldn't matter (`"Alice"` == `"alice"` for this)
- Don't overthink it — this is a string manipulation exercise, not a real predictor

**📚 Warm-up tasks:**
1. Write a function that takes two strings and removes all characters they share (considering count)
2. Write a list cycling/elimination algorithm — given `["F","L","A","M","E","S"]` and a count N, find which one gets eliminated

**🔧 Core concepts:**
- String → list conversion: `list("hello")`
- Removing elements from a list carefully (`list.remove()` vs index-based deletion)
- Modulo arithmetic for cycling: `count % len(remaining)`

**🔍 Deepen your understanding:**
- What is modulo (`%`) and what makes it useful for circular/wrapping logic?
- Look up Python's `collections.Counter` — how would it help with letter counting?

**🧪 Experiments:**
- Process multiple name pairs in a loop from a file
- Add a "compatibility score" as a percentage based on common letters
- Make it case-insensitive and strip spaces automatically

---

### Project 18 — Cows and Bulls Game

**🎯 Objective:** Computer picks a 4-digit number (no repeating digits). Player guesses. Count *bulls* (right digit, right position) and *cows* (right digit, wrong position). Player wins when they get 4 bulls.

**🚫 Anti-goals:**
- This is essentially Mastermind with digits — don't copy-paste, rewrite the logic fresh and notice the differences

**📚 Warm-up tasks:** Same as Mastermind warm-ups — revisit and refine your comparison functions.

**🔧 Core concepts:**
- Generating a 4-digit number with unique digits: `random.sample(range(10), 4)`, watch out for leading zero
- Comparing string digits vs integer digits
- Reusing/refactoring your logic from Mastermind (practice DRY — Don't Repeat Yourself)

**🔍 Deepen your understanding:**
- What is refactoring? How could you extract a general `count_bulls_cows(secret, guess)` function that works for both Mastermind and this?

**🧪 Experiments:**
- Let the player pick the code length (3, 4, or 5 digits)
- Track and display the player's guess history neatly
- Build a brute-force computer solver as a separate script

---

### Project 20 — Higher-Lower Game

**🎯 Objective:** Show two things (celebrities, countries by population, etc.) with a number associated. Player picks which is higher. Track their streak. Game ends on first wrong answer.

**🚫 Anti-goals:**
- Don't use an online API yet — hardcode 20–30 items in a list of dicts
- Don't repeat the same comparison twice in one session

**📚 Warm-up tasks:**
1. Create a list of 5 dictionaries: `[{"name": "Sweden", "population": 10_400_000}, ...]`
2. Write a function that picks two different random items from a list (no repeats)

**🔧 Core concepts:**
- List of dictionaries (this is your first mini-database)
- Tracking state across rounds (streak, seen items)
- Formatting numbers nicely with f-strings: `f"{pop:,}"` adds commas

**🔍 Deepen your understanding:**
- What is a dictionary? Why is `item["population"]` better than `item[1]` for readability?
- Search "Python list of dicts sort" — how do you sort your items by value?

**🧪 Experiments:**
- Replace the hardcoded list with an API call (search "restcountries API")
- Show a leaderboard of best streaks saved to a file
- Add a timer — player has 5 seconds per guess

---

### Project 23 — How To Create a Countdown Timer

**🎯 Objective:** User enters hours, minutes, seconds. Timer counts down in the terminal, updating every second. When it hits zero, alert the user.

**🚫 Anti-goals:**
- Don't build a clock/stopwatch (different)
- The terminal display should overwrite itself each second, not print 1000 new lines

**📚 Warm-up tasks:**
1. Use `import time` and `time.sleep(1)` to print "tick" every second for 10 seconds
2. Write a function that converts total seconds to `HH:MM:SS` format

**🔧 Core concepts:**
- `import time` → `time.sleep(1)`
- `print(f"\r{display}", end="", flush=True)` — the `\r` trick to overwrite the same line
- Converting and validating time input

**🔍 Deepen your understanding:**
- What does `flush=True` do? Why is it needed here?
- Search "Python ANSI escape codes terminal" — how can you add colour to terminal output?
- What is a Unix timestamp? (`time.time()`)

**🧪 Experiments:**
- Play a sound when the timer ends (use `winsound` on Windows or `os.system("afplay bell.wav")` on Mac)
- Let the user name the timer ("Pasta Timer") and show the label
- Build a Pomodoro timer (25 min work, 5 min break, repeat)

---
## 📅 Weekly Structure (Repeat Every Week)

| Day | Focus |
|-----|-------|
| Mon–Fri | Build, experiment, document |
| Saturday | Review the week. Refactor one old project. Fix bad habits. |
| Sunday | Explore one concept deeper (a YouTube video, a docs page, a chapter) |
---

## WEEK 3 — File I/O, External Libraries, String Manipulation

**Core Skills This Week:** reading/writing files, `pip install`, working with external libraries, basic string processing

> Before this week: practice `pip install requests`, understand what a virtual environment is (`python -m venv env`). Always work inside a venv from now on.

---

### Project 6 — Check if Two PDF Documents Are Identical

**🎯 Objective:** User provides two PDF file paths. Your script extracts the text from each and compares them. Report: identical, mostly similar (show diff), or completely different.

**🚫 Anti-goals:**
- Don't compare the raw bytes of the files (that only works if they're pixel-identical, not content-identical)
- Don't try to compare images inside PDFs — text only is fine

**📚 Warm-up tasks:**
1. `pip install PyPDF2` (or `pypdf`). Write a script that opens a PDF and prints all its text
2. Write a function that takes two strings and returns `True` if they're identical
3. Look at Python's `difflib` module — print the difference between two strings

**🔧 Core concepts:**
- `pypdf` (modern replacement for PyPDF2): `PdfReader`, `page.extract_text()`
- Python's built-in `difflib.SequenceMatcher` for similarity ratio
- File path handling with `pathlib.Path`

**🔍 Deepen your understanding:**
- What is `pathlib`? Why is it better than string-based paths like `"C:\\Users\\..."`?
- What does `difflib.unified_diff()` return? (It's how git shows diffs!)
- Search "PDF text extraction limitations" — why does this sometimes fail?

**🧪 Experiments:**
- Compare PDFs page-by-page and report which pages differ
- Output a similarity percentage
- Write the diff report to a `.txt` file

---

### Project 7 — Convert Emoji into Text

**🎯 Objective:** User types or pastes a string containing emojis. Your script converts each emoji to its text description (e.g., `😊` → `"smiling face with smiling eyes"`). Also do the reverse: text description → emoji.

**🚫 Anti-goals:**
- Don't build a translator — only emoji ↔ description
- Don't try to handle every Unicode edge case

**📚 Warm-up tasks:**
1. `pip install emoji`. Print `emoji.emojize(":smile:")` and `emoji.demojize("😊")`
2. Write a function that takes a sentence and replaces all emojis with their names in square brackets

**🔧 Core concepts:**
- `emoji` library: `demojize()`, `emojize()`, `emoji_list()`
- String `.replace()` and regex basics (`import re`)
- Dictionary lookup patterns

**🔍 Deepen your understanding:**
- What is Unicode? What is UTF-8? Why do emojis sometimes break in older programs?
- Look up `re.sub()` — how do you replace patterns in strings using regular expressions?
- What is the emoji standard? (search "Unicode emoji list")

**🧪 Experiments:**
- Count how many emojis are in a block of text
- Translate emoji sequences into a "story" (😀🌧️ → "happy despite rain")
- Build a simple emoji-to-emoji translator dictionary

---

### Project 19 — Simple Attendance Tracker

**🎯 Objective:** Track attendance for a class or group. Add students, mark them present/absent for a given date, view attendance reports. Data persists between runs (saved to file).

**🚫 Anti-goals:**
- No GUI needed — terminal menu is fine
- Don't use a database (SQL) yet — CSV or JSON is the right tool here

**📚 Warm-up tasks:**
1. Write a script that writes a list of names to a `.txt` file, then reads it back
2. Write a script that appends a new line to a CSV file using `csv.writer`
3. Write a script that reads a JSON file and prints its contents (`import json`)

**🔧 Core concepts:**
- `import csv` — `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter`
- `import json` — `json.dump()`, `json.load()`
- `pathlib.Path.exists()` — check if a file already exists before creating it
- A simple menu loop: `print("1. Add student\n2. Mark attendance\n3. View report")`

**🔍 Deepen your understanding:**
- What is CSV? What are its limitations (e.g. what happens if a name contains a comma)?
- What is JSON? When would you choose JSON over CSV?
- Search "Python context manager `with open`" — why is `with open(...) as f:` safer than just `f = open(...)`?

**🧪 Experiments:**
- Calculate and display attendance percentage per student
- Filter by date range
- Export an attendance summary as a formatted `.txt` report

---

## WEEK 4 — APIs, Web Requests, Real-World Data

**Core Skills This Week:** HTTP requests, JSON APIs, error handling, environment variables for secrets

> Before this week: understand what an API is. Watch a 10-minute video: "What is a REST API explained for beginners." Know what HTTP status codes are (200 = OK, 404 = not found, 401 = unauthorised).

---
## 📅 Weekly Structure (Repeat Every Week)

| Day | Focus |
|-----|-------|
| Mon–Fri | Build, experiment, document |
| Saturday | Review the week. Refactor one old project. Fix bad habits. |
| Sunday | Explore one concept deeper (a YouTube video, a docs page, a chapter) |
---

### Project 13 — Pokémon Training Game

**🎯 Objective:** Use the free PokéAPI (no key needed). Fetch real Pokémon data (name, HP, attack, type). Build a simple battle simulator: your Pokémon vs a random one. Simulate turns based on stats.

**🚫 Anti-goals:**
- Don't implement the full Pokémon damage formula — simplify it
- Don't cache every Pokémon — just fetch on demand

**📚 Warm-up tasks:**
1. `pip install requests`. Make a GET request to `https://pokeapi.co/api/v2/pokemon/pikachu` and print the JSON
2. Extract just the name, HP, and attack stat from the response
3. Write a simple combat round: attacker's attack vs defender's defence, reduce HP

**🔧 Core concepts:**
- `requests.get(url)` → `.json()` to parse response
- Navigating nested JSON: `data["stats"][0]["base_stat"]`
- Error handling: `response.raise_for_status()`
- `class Pokemon` with attributes: name, hp, attack, defense — your first real class!

**🔍 Deepen your understanding:**
- What is OOP (Object-Oriented Programming)? What is `self`?
- What is `__repr__` or `__str__` on a class?
- Search "Python dataclasses" — they're a cleaner way to define data-holding classes

**🧪 Experiments:**
- Add type advantages (water beats fire → 1.5x damage)
- Allow the player to choose their starter Pokémon by name
- Add experience points and a level-up system between battles

---

### Project 16 — Get Live Weather Desktop Notifications

**🎯 Objective:** Fetch live weather for the user's city using a free weather API (OpenWeatherMap). Display current temperature, conditions, and an optional notification if it's about to rain.

**🚫 Anti-goals:**
- Store your API key in a `.env` file, never hardcode it
- Don't display a full forecast app — just current conditions + one notification

**📚 Warm-up tasks:**
1. Sign up for a free OpenWeatherMap API key (free tier is enough)
2. Make a request to their `/weather` endpoint for your city and print the raw JSON
3. `pip install python-dotenv`. Load an API key from a `.env` file

**🔧 Core concepts:**
- `python-dotenv`: `load_dotenv()`, `os.getenv("API_KEY")`
- Parsing weather JSON: temperature (convert Kelvin → Celsius: subtract 273.15), description, humidity
- `plyer` library for desktop notifications: `notification.notify()`

**🔍 Deepen your understanding:**
- What is an API key and why should you never commit it to GitHub?
- Search "HTTP query parameters" — how does `?q=Stockholm&appid=...` work in a URL?
- What is `.env` and `.gitignore`? These are standard practice in all real projects.

**🧪 Experiments:**
- Run the script automatically every morning (search "schedule library Python" or "cron job")
- Add a 5-day forecast summary
- Change the notification message based on conditions (umbrella emoji for rain, sun for clear)

---

### Project 21 — Fun Fact Generator Web App

**🎯 Objective:** A minimal web app (using Flask) with one button: "Give me a fact." It fetches a random fact from a public API (e.g. `https://uselessfacts.jsph.pl/random.json`) and displays it on the page.

**🚫 Anti-goals:**
- Don't build a full multi-page site
- Don't store facts in a database
- This is your *hello world* for Flask — keep it tiny

**📚 Warm-up tasks:**
1. `pip install flask`. Copy the Flask hello world example from the docs and run it
2. Create an HTML template with a button and a `<p>` tag
3. Make a Python function that fetches a random fact from the API and returns the text

**🔧 Core concepts:**
- Flask basics: `@app.route()`, `render_template()`, `request`, `jsonify`
- Jinja2 templates: `{{ variable }}`, `{% if %}`, `{% for %}`
- Serving a simple HTML page with a fetch from JavaScript (or a form POST)
- Flask's `debug=True` mode during development

**🔍 Deepen your understanding:**
- What is the difference between a GET and a POST request?
- What is Jinja2? How does it work with Flask?
- Search "Flask vs FastAPI vs Django" — know your options (don't switch yet, just understand the landscape)

**🧪 Experiments:**
- Add a "category" dropdown (animals, history, science)
- Let users submit their own facts (save to a text file)
- Add a "fact of the day" that doesn't change until midnight

---

## WEEK 5 — System Tools & Desktop Automation

**Core Skills This Week:** OS interaction, working with audio, screenshots, system notifications

> This week touches system-level tools. Things *will* break depending on OS (Windows vs Mac vs Linux). Don't panic — read the error, search it with your OS name included.

---

### Project 15 — Desktop Notifier

**🎯 Objective:** A script that sends a desktop notification with a custom title, message, and optional icon. Build a few useful triggers: motivational quote every hour, reminder after a set time, etc.

**🚫 Anti-goals:**
- This is simpler than it sounds — don't over-engineer it
- Don't build a full notification center

**📚 Warm-up tasks:**
1. `pip install plyer`. Run the basic `notification.notify()` example
2. Combine with Project 23's countdown timer: notify when the timer ends

**🔧 Core concepts:**
- `plyer.notification.notify(title, message, timeout)`
- `import schedule` — scheduling recurring tasks
- `time.sleep()` inside a scheduler loop

**🔍 Deepen your understanding:**
- How does `schedule` differ from `threading.Timer`?
- Search "Python background process" — how would you run this without a terminal window?

**🧪 Experiments:**
- Build a "study session" tool: notify every 25 minutes (Pomodoro)
- Randomly pick a quote from a list file for each notification
- Send the live weather (from Project 16) as a morning notification

---

### Project 8 — Create a Voice Recorder

**🎯 Objective:** Record audio from the microphone when the user presses Enter, stop recording when they press Enter again. Save the recording as a `.wav` file with a timestamped filename.

**🚫 Anti-goals:**
- Don't edit or playback audio programmatically yet
- Don't build a music app — just clean recording and saving

**📚 Warm-up tasks:**
1. `pip install sounddevice soundfile`. Run a test that records 3 seconds and saves it
2. Understand `numpy` arrays briefly — audio data is stored as an array of numbers

**🔧 Core concepts:**
- `sounddevice.rec()`, `sounddevice.wait()`
- `soundfile.write()` to save `.wav`
- `datetime.now().strftime("%Y%m%d_%H%M%S")` for timestamped filenames
- Threading basics: record in background while waiting for keyboard input (optional but useful)

**🔍 Deepen your understanding:**
- What is a sample rate? (44100 Hz is CD quality) What does it mean?
- What is the difference between `.wav` and `.mp3`?
- Search "Python threading basic example"

**🧪 Experiments:**
- Automatically name recordings by transcribing the first 5 seconds (search "SpeechRecognition Python")
- Save recordings in a dated folder structure (`recordings/2024-11/`)
- Display recording duration after saving

---

### Project 14 — Taking Screenshots Using pyscreenshot

**🎯 Objective:** Take a full screenshot, a region screenshot (user-defined coordinates), and optionally auto-screenshot every N seconds. Save with timestamps.

**🚫 Anti-goals:**
- Don't build a screen recorder yet (that's Project 9)
- Don't process or edit images in this one

**📚 Warm-up tasks:**
1. `pip install Pillow pyscreenshot`. Take a full screenshot and open it
2. Look up PIL Image: `Image.open()`, `image.show()`, `image.save()`

**🔧 Core concepts:**
- `pyscreenshot.grab()` (or `PIL.ImageGrab.grab()` on Windows/Mac)
- Bounding box: `grab(bbox=(x1, y1, x2, y2))`
- File naming with timestamps
- Optional: `time.sleep()` loop for interval screenshots

**🔍 Deepen your understanding:**
- What is PIL/Pillow? What can it do beyond screenshots? (resize, crop, filter, draw text on images)
- What are screen coordinates? How do you find the resolution of your screen programmatically?

**🧪 Experiments:**
- Build a "screen diff" tool: take two screenshots 10 seconds apart and highlight pixels that changed (using Pillow's `ImageChops.difference()`)
- Add a hotkey trigger using `keyboard` library
- Automatically upload screenshots to a folder

---

## WEEK 6 — 2D Logic, Grid Games, Advanced OOP

**Core Skills This Week:** 2D lists, matrix operations, more advanced class design

---

### Project 11 — 2048 Game

**🎯 Objective:** The classic 2048 game in the terminal. A 4×4 grid of numbers. Player moves (up/down/left/right) slide all tiles in that direction. Matching tiles merge (2+2=4). A new tile (2 or 4) spawns after each move. Goal: reach the 2048 tile.

**🚫 Anti-goals:**
- Terminal version only — no graphics needed
- Don't make the board print a new grid every turn if you can overwrite it (optional polish)
- Don't implement undo/redo yet

**📚 Warm-up tasks:**
1. Create a 4×4 2D list filled with zeros: `[[0]*4 for _ in range(4)]`
2. Write a function that "slides" a single row left: `[2, 0, 2, 4]` → `[4, 4, 0, 0]`
3. Write a function that adds a random 2 or 4 to an empty cell

**🔧 Core concepts:**
- 2D list manipulation (this is the hardest part of the project)
- Slide logic: compress zeros, merge equal neighbours, compress again
- Rotate the grid to reuse the "slide left" function for all 4 directions
- `os.system("cls" or "clear")` to refresh the terminal display

**🔍 Deepen your understanding:**
- How do you transpose (rotate) a 2D list in Python? `list(zip(*grid))`
- What is immutability? Why should your slide function return a *new* list rather than modifying the old one?
- Search "2048 algorithm explained" to understand the canonical approach

**🧪 Experiments:**
- Track and display the current score (sum of all merged tiles)
- Detect "game over" (no valid moves left)
- Add an AI solver (search "2048 expectimax algorithm")

---

## WEEK 7 — Documents, Receipts, Reports

**Core Skills This Week:** generating PDFs, working with report libraries, formatting output documents

---

### Project 22 — Creating Payment Receipts

**🎯 Objective:** User enters customer name, list of items with prices, and payment method. Your script generates a professionally formatted PDF receipt with itemised list, subtotal, tax, and total.

**🚫 Anti-goals:**
- Don't build a real payment system
- Don't use Word — PDF is the standard for receipts

**📚 Warm-up tasks:**
1. `pip install fpdf2`. Run the hello world example — generate a PDF with your name on it
2. Write a function that calculates subtotal, tax (e.g. 25% Swedish VAT), and total given a list of prices
3. Draw a simple table manually using `fpdf`: columns for Item, Qty, Price

**🔧 Core concepts:**
- `fpdf2`: `FPDF()`, `add_page()`, `set_font()`, `cell()`, `ln()`, `multi_cell()`
- Table layout using cells with borders
- Generating a receipt number (random or sequential)
- `datetime.now()` for receipt date

**🔍 Deepen your understanding:**
- What is the difference between `fpdf2` and `reportlab`? When would you use each?
- What is a PDF unit (pt vs mm vs cm)? `fpdf2` uses mm by default.
- Search "fpdf2 table example" — tables are the hardest part to get right

**🧪 Experiments:**
- Add a company logo image at the top
- Add a barcode or QR code (search `qrcode` Python library)
- Read item list from a CSV file instead of manual input

---

## WEEK 8 — Screen Recording, Advanced System Tools

**Core Skills This Week:** OpenCV, system-level access, threading for concurrent tasks

---

### Project 9 — Create a Screen Recorder

**🎯 Objective:** Capture the screen at a set frame rate, encode it as a video file. Record until the user stops it. Save as `.mp4` or `.avi`.

**🚫 Anti-goals:**
- Don't add audio in the first version — video only
- Don't expect 60fps from a Python script — 10–15fps is realistic

**📚 Warm-up tasks:**
1. `pip install opencv-python pyautogui numpy`. Take a screenshot with pyautogui and convert it to an OpenCV image
2. Write a `VideoWriter` that takes a list of frames and saves them as a video
3. Understand `cv2.VideoWriter_fourcc(*"XVID")` — what is a codec?

**🔧 Core concepts:**
- `pyautogui.screenshot()` → `numpy` array → OpenCV frame
- `cv2.VideoWriter` for encoding video
- Threading: capture frames in one thread, monitor keyboard in another
- `keyboard` library for stop hotkey

**🔍 Deepen your understanding:**
- What is a video codec? (H.264, XVID, MP4V) Why does it matter for file size and compatibility?
- What is frame rate? What determines max achievable FPS in this approach?
- Search "ffmpeg Python" — the professional-grade alternative

**🧪 Experiments:**
- Add a countdown before recording starts ("Recording in 3... 2... 1...")
- Highlight the mouse cursor in the recording
- Auto-open the saved file after recording ends

---

### Project 17 — How to Use pynput to Make a Keylogger

**🎯 Objective:** ⚠️ **Ethical note:** Keyloggers are serious tools. Build this ONLY on your own machine, never deploy it on others' computers. The purpose here is to understand how keyboard events work and how security tools are built — not for surveillance.

Build a script that logs all keypresses (including special keys) to a file, with timestamps. Add an auto-stop after N minutes.

**🚫 Anti-goals:**
- Do NOT run this on any machine you don't own
- Do NOT send logs to a server
- This is for local learning only

**📚 Warm-up tasks:**
1. `pip install pynput`. Run the listener example from the docs and print each key pressed
2. Write a function that formats a keypress nicely: `Key.space` → `" "`, `Key.enter` → `"\n"`, regular keys → their character

**🔧 Core concepts:**
- `pynput.keyboard.Listener` — event-driven programming (callbacks)
- `on_press` and `on_release` callbacks
- Writing to a log file in real time (`file.write()` + `file.flush()`)
- Running the listener in a non-blocking way

**🔍 Deepen your understanding:**
- What is event-driven programming? How does it differ from sequential code?
- What is a callback function?
- Search "how antivirus detects keyloggers" — understand the defensive side too

**🧪 Experiments:**
- Log only keypresses during a specific application (filter by window title)
- Auto-encrypt the log file using `cryptography` library
- Build the opposite: a "replay" script that types back what was logged

---

## 🧠 When You're Stuck — A Framework

**Before googling, try this for 15 minutes:**
1. Read the error message top to bottom. The last line is usually the most useful
2. Add `print()` statements before the broken line to see what your variables actually contain
3. Isolate the problem — comment out everything except the broken part

**Searching effectively:**
- Always include the error text AND the library name: `"pynput AttributeError on_press"`
- Search Stack Overflow with `python [library] [what you're trying to do]`
- For library questions, the official docs are almost always better than random tutorials

**When a library isn't working:**
- Check you're in the right virtual environment: `pip list` shows what's installed
- Check you're using the right Python version: `python --version`
- Search "[library name] not working [your OS]"

**When your logic is wrong but there's no error:**
- Use `print()` to trace values step by step — this is debugging
- Write the smallest possible test of your logic in a new file
- Explain your code out loud (rubber duck debugging — it works)

**When you want to give up:**
- That feeling usually means you're 20 minutes away from the breakthrough
- Take a walk. Seriously. Your brain solves problems in the background.
- Post in r/learnpython — the community is genuinely helpful

---

## 📖 Documentation Hour — What to Write Each Day

Your `notes.md` for each project should answer:
- What did I build today?
- What was the hardest part and how did I solve it?
- What does `[specific function/method]` do? (Explain it in your own words)
- What would I add if I had more time?
- One thing I want to look up more tomorrow

This becomes your personal Python reference. After 2 months, you'll have 23 entries of real experience — more valuable than any tutorial.

---

## 🔥 Consistency Tips

**The most important thing:** Show up even when you don't feel like it. A bad 1-hour session is worth more than a perfect session you didn't have.

**Make it hard to skip:**
- Set a specific time (e.g. 9AM daily) — don't decide *when* each morning
- Keep your editor open with yesterday's code visible — starting is the hardest part
- Tell someone you're doing this (accountability partner, Discord server, Reddit post)

**Make it easy to continue:**
- Always end a session by writing one comment: `# TODO tomorrow: fix the input validation here`
- Never finish a session at a clean stopping point — stop mid-thought so starting tomorrow feels like continuing, not starting over
- Keep a "wins" list — one bullet per day noting something that worked

**When motivation dips (it will, around week 3–4):**
- Switch the order — if you're bored, jump ahead to a project that excites you
- Build something personal — modify a project to solve *your* actual problem
- Time-box frustration: if stuck for >45 min, move on and come back

**Track your streak but don't worship it:**
- A GitHub contribution graph or a paper calendar with X marks works great
- Breaking a streak once doesn't erase your progress. Get back the next day.

**The bigger picture:** After these 8 weeks, you won't be an expert — you'll be someone who has *shipped 23 things*, debugged real errors, read real documentation, and built real intuitions. That's worth far more than finishing a course.

---

## 📌 Quick Reference — Libraries Used in This Guide

| Library | Install | Projects |
|---------|---------|----------|
| `requests` | `pip install requests` | 13, 16, 21 |
| `pypdf` | `pip install pypdf` | 6 |
| `emoji` | `pip install emoji` | 7 |
| `sounddevice` + `soundfile` | `pip install sounddevice soundfile` | 8 |
| `opencv-python` | `pip install opencv-python` | 9 |
| `fpdf2` | `pip install fpdf2` | 22 |
| `flask` | `pip install flask` | 21 |
| `plyer` | `pip install plyer` | 15, 16 |
| `pyscreenshot` | `pip install pyscreenshot Pillow` | 14 |
| `pynput` | `pip install pynput` | 17 |
| `python-dotenv` | `pip install python-dotenv` | 16 |
| `schedule` | `pip install schedule` | 15 |
| `pyautogui` | `pip install pyautogui` | 9 |
| `numpy` | `pip install numpy` | 8, 9 |

> Always use a virtual environment: `python -m venv env` → activate it → install inside it.

---

*Good luck. The fact that you're planning this carefully already puts you ahead of most beginners.*

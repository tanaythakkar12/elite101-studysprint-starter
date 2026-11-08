# StudySprint

StudySprint is a Python flashcard and quiz app that runs in the terminal.
It helps students study, practice questions, and track their quiz scores.

## Features

- Take a flashcard quiz and see your score and percentage.
- View all flashcards in your deck.
- Add new flashcards with questions and answers.
- Study flashcards by category.
- View the last flashcard in the deck.
- See how many flashcards are in each category.
- View a summary of your flashcard deck.

## How to Run

Open the project in VS Code or GitHub Codespaces.

Run:

```bash
python main.py
```

Choose an option from the menu to start studying.

## How to Run Tests

Run:

```bash
python -m unittest
```

## Project Files

| File | Purpose |
|---|---|
| `main.py` | Runs the main menu |
| `storage.py` | Loads and saves flashcard data |
| `features/core.py` | Handles flashcards and quizzes |
| `features/reports.py` | Creates deck summaries |
| `data/studysprint.json` | Stores flashcard data |
| `tests/` | Contains automated tests |

## Team

- Tanay Thakkar - Solo Developer

## Future Improvements

- Add a Review Missed Cards feature to practice incorrectly answered questions.
- Improve quiz progress tracking.
- Add more options for organizing flashcards.

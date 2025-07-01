
# Quiz Application

A fully functional GUI-based quiz platform built with Python and Tkinter, featuring user login, category-based question selection, answer persistence, scoring, and time tracking. The app supports user management and category/question storage via pickle serialization. Designed to be extensible, secure, and user-friendly.

---

## Features

✅ User login and guest access
✅ Dynamic category selection with a list-based interface
✅ Question and answer loading from serialized pickle data
✅ Save/clear answers with live feedback
✅ Countdown timer with per-session scoring
✅ Modular design with separate classes for login, category, and quiz handling
✅ Easy to extend with new questions, categories, or user types

---

## System Design

* Frontend: Tkinter-based GUI for cross-platform compatibility
* Backend: Pickle-based local data store for rapid prototyping
* Architecture: MVC-inspired separation with classes for login, categories, and quiz flows
* Data Flow:

  1. Load users/categories from pickle
  2. Authenticate user or allow guest login
  3. Display category list
  4. Serve quiz questions with answer persistence
  5. Show scoring at the end

---

## Technologies Used

* Language: Python 3
* GUI Framework: Tkinter
* Data Storage: Pickle serialization
* Libraries: `tkinter`, `pickle`, `time`, `messagebox`

---

## Setup Instructions

1. Clone the repo

   ```bash
   git clone https://github.com/yourusername/quiz-application.git
   cd quiz-application
   ```
2. Install Python 3 if not already available
3. Make sure your `users.pickle` and `categories.pickle` are in the project directory
4. Run the app

   ```bash
   python quiz.py
   ```

---

## Data File Structure

* `users.pickle`: stores username + regno
* `categories.pickle`: stores available quiz categories
* `category_name.pickle`: question bank for each category with question text, options, and answers

---

## Extending the Application

✅ To add new categories, create new pickle files and register their names in `categories.pickle`
✅ To add new users, update `users.pickle` with their names and regno
✅ To add questions, update the corresponding category pickle with question dicts

---

## Future Enhancements

* Migrate from pickle to SQLite or JSON for improved maintainability
* Add user registration in-app
* Provide question randomization and difficulty levels
* Export results to a leaderboard file or server
* Include analytics for user scoring patterns

---

## License

This project is open-source and available under the MIT License.

---

If you want, I can help you generate badges, contribution guidelines, or even a detailed changelog section — just say the word.

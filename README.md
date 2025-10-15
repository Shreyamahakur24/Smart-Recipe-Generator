# Smart-Recipe-Generator
The Smart Recipe Generator uses Python/Flask &amp; JS/HTML/CSS for partial ingredient matching, diet filtering, and responsive design.

## Project Overview
The **Smart Recipe Generator** is a technical assessment project developed to demonstrate core software engineering principles, including robust backend logic (Python/Flask) and a clean, responsive frontend (HTML/CSS/JS). The application suggests recipes based on ingredients provided by the user, incorporating filtering and intelligent partial matching to enhance usability.

---

## 🚀 Required Features Implemented

The application successfully implements the following core features from the project brief:

### 1. Recipe Generation & Matching
* **Partial Match Algorithm (Recipe Matching Logic):** The backend uses a scoring system to suggest recipes even if the user is missing a few required items. Recipes are ranked by the percentage of required ingredients the user possesses.
* **Detailed Recipe Output:** Each result provides detailed instructions, required ingredients, nutritional information, and cooking metadata (time, difficulty).
* **Substitution Suggestions:** Missing ingredients are explicitly listed to guide the user on what they need to complete the recipe, serving as a simplified substitution suggestion.

### 2. User Input and Filters
* **Ingredient Input:** Users input available ingredients via a simple comma-separated text field.
* **Dietary Preferences Handling:** Recipes can be filtered by selection (e.g., **Vegetarian**, **Non-Vegetarian**, **Gluten-Free**), fulfilling the dietary restriction requirement.

### 3. Recipe Database
* **Minimum Data Set:** The backend includes a simple, in-memory JSON database containing **21 recipes** across various cuisines, exceeding the minimum requirement.

### 4. UI/UX & Technical Requirements
* [cite_start]**Clean, Intuitive Interface:** The application provides a clear, single-page interface for input and results[cite: 26].
* [cite_start]**Mobile Responsive Design:** The CSS uses media queries to ensure the layout is optimized for all screen sizes (a required feature)[cite: 27, 38].
* [cite_start]**Loading States:** A visible loading indicator is displayed during the API call for a better user experience (UX)[cite: 47].
* [cite_start]**Dark/Light Mode:** A theme toggle allows users to switch between a **Soothing Light Mode** and a **Dark Mode**, demonstrating attention to UX considerations[cite: 43].
* [cite_start]**Clean Code:** The code is structured and commented for clarity and maintainability[cite: 45].
* [cite_start]**Basic Error Handling:** Frontend and backend include checks for missing input and server connection failures.

---

## 🛠️ Technology Stack

| Component | Technology Used | Notes |
| :--- | :--- | :--- |
| **Backend** | Python 3, Flask | Lightweight web framework for API routing and business logic. |
| **API/Data** | Flask-CORS, JSON (in-memory DB) | Handles cross-origin requests; Recipe database stored as Python dictionaries. |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla JS) | [cite_start]Focus on clean, production-quality code [cite: 45] without reliance on heavy frameworks. |

---

## 🚀 Setup and Installation

### 1. Clone the Repository

```bash
git clone [YOUR-GITHUB-REPO-URL]
cd smart-recipe-generator

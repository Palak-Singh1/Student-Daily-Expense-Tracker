
# Spendly — Student Daily Expense Tracker

Spendly is a modern, student-focused daily expense and budget management web application built with Python and Streamlit.

It helps students record their everyday expenses, organize transactions by category, monitor their monthly budget, understand spending patterns, and make better financial decisions.

---

## ✨ Features

### 💳 Expense Management
- Record daily expenses with:
  - Expense title
  - Amount
  - Category
  - Transaction date
  - Optional notes
- Automatic transaction ID generation
- Input validation for expense title and amount
- Instant dashboard updates after adding an expense

### 📅 Date-Based Expense Tracking
- Add a specific date while recording an expense
- Display transaction dates in the expense history
- Keep expenses organized according to when they were recorded
- Current date is displayed on the dashboard

### 📋 Transaction Management
- View all recorded transactions
- Search expenses by title
- Filter expenses by category
- Delete individual transactions
- View transaction count
- Review expense details and amounts

### 📊 Spending Insights
Spendly automatically analyzes recorded expenses and provides:

- Total amount spent
- Total number of transactions
- Average expense
- Highest spending category
- Category-wise spending breakdown
- Percentage of total spending by category
- Visual spending progress indicators

### 💰 Budget Planner
- Set a custom monthly spending budget
- Update the budget whenever required
- View:
  - Monthly budget
  - Total amount spent
  - Remaining budget
  - Percentage of budget used
- Visual budget progress bar
- Automatic warning when spending approaches or exceeds the budget
- Reset budget option

### 🔔 Budget Alerts
- Enable or disable budget warnings
- Receive spending guidance based on budget usage
- Different alerts are displayed depending on spending level:
  - Comfortable spending
  - Moderate usage
  - Nearing budget limit
  - Budget exceeded

### 👤 Profile & Preferences
- Set and update display name
- Personalized dashboard greeting
- Dynamic greeting based on the current time:
  - Good morning
  - Good afternoon
  - Good evening
- Current date displayed on the dashboard

### 🗂️ Data Management
- Clear all recorded transactions
- Reset the monthly budget
- Manage tracker settings from a centralized Preferences section

---

## 🎨 User Interface

Spendly was designed with a clean and modern student-oriented interface.

### UI Highlights

- Purple, blue and cyan gradient-based visual theme
- Modern dashboard cards
- Custom sidebar navigation
- Spendly branded logo
- Clean typography and spacing
- Visual budget indicators
- Personalized dashboard
- Minimal and distraction-free layout

The interface focuses on making financial tracking simple without making the application feel like a traditional finance-management tool.

---

## 🛠️ Tech Stack

### Frontend / UI
- Streamlit
- HTML
- CSS

### Backend / Logic
- Python

### Concepts Used
- Python functions
- Lists and dictionaries
- Conditional statements
- Loops
- Session state
- Data filtering and searching
- Basic financial calculations
- Category-wise aggregation

---

## 📂 Project Structure

```text
Spendly/
│
├── app.py              # Main Streamlit application
├── main.py             # Expense data and application logic
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
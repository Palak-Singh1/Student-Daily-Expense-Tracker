

## Spendly — Student Daily Expense Tracker

Spendly is a modern, student-focused daily expense and budget management web application built with Python and Streamlit.

It helps students record their everyday expenses, organize transactions by category, monitor their monthly budget, understand spending patterns, and make better financial decisions.

---
##Live Demo Link :
https://spendly-tracker.streamlit.app/

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

## Supabase database setup (persistent cloud storage)

This version adds Supabase Auth and a PostgreSQL database. Each signed-in user can access only their own expenses and preferences.

### 1. Create a Supabase project
1. Create a project at https://supabase.com/.
2. Open **SQL Editor → New query**.
3. Paste the contents of `supabase_schema.sql` and run it.
4. In **Project Settings → API** (or **Connect**), copy the Project URL and the **anon/public** key. Never use the `service_role` key in this app.

### 2. Add Streamlit secrets
In your Streamlit Community Cloud app, open **Settings → Secrets** and add:

```toml
[supabase]
url = "https://YOUR-PROJECT-REF.supabase.co"
anon_key = "YOUR_SUPABASE_ANON_PUBLIC_KEY"
```

Replace both placeholders with your actual project values. Do not commit secrets to GitHub.

### 3. Deploy this version
1. Commit/push `app.py`, `app1.py`, `database.py`, `requirements.txt`, and `supabase_schema.sql` to the GitHub repository connected to Streamlit.
2. In Streamlit Community Cloud, set **Main file path** to `app.py` (or `app1.py`).
3. Reboot the app after adding secrets.
4. Create an account in Spendly, then log in. New expenses and preferences will be stored in Supabase.

### Important notes
- This does not automatically migrate expenses that existed only in an old Streamlit session; that data was not persistent.
- Each user must sign in. Row Level Security restricts records to their owner.
- Supabase email confirmation may be enabled by default. If signup does not log you in immediately, confirm your email, then use the Log in tab.
- Never expose a service-role key.

import streamlit as st
import main
import textwrap
from datetime import date, datetime

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Spendly",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

    /* Main application */
    .stApp {
        background:
            radial-gradient(circle at 85% 8%, rgba(124,58,237,0.10), transparent 24%),
            radial-gradient(circle at 18% 92%, rgba(6,182,212,0.08), transparent 22%),
            #f7f8fc;
    }

    /* Remove default top padding */
    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1400px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #ffffff 0%, #fbf9ff 55%, #f6fbff 100%);
        border-right: 1px solid #e7e5f4;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    /* Brand */
    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 35px;
    }

    .brand-icon {
        width: 58px;
        height: 58px;
        border-radius: 18px;
        background: linear-gradient(145deg, #7c3aed 0%, #5b21b6 55%, #0891b2 140%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 18px;
        font-weight: 800;
        letter-spacing: -1px;
        box-shadow: 0 10px 24px rgba(109, 40, 217, 0.24);
        border: 1px solid rgba(255,255,255,0.25);
        position: relative;
    }

    .brand-icon::after {
        content: "";
        position: absolute;
        width: 22px;
        height: 8px;
        border: 2px solid rgba(255,255,255,0.75);
        border-top: none;
        border-radius: 0 0 8px 8px;
        bottom: 9px;
        left: 50%;
        transform: translateX(-50%);
    }

    .brand-name {
        font-size: 26px;
        font-weight: 850;
        color: #32136f;
        letter-spacing: -0.5px;
    }

    .brand-subtitle {
        font-size: 13px;
        color: #8b95aa;
        margin-top: -4px;
    }


    /* Streamlit form labels */
    div[data-testid="stTextInput"] label,
    div[data-testid="stTextInput"] label p,
    div[data-testid="stNumberInput"] label,
    div[data-testid="stNumberInput"] label p,
    div[data-testid="stSelectbox"] label,
    div[data-testid="stSelectbox"] label p,
    div[data-testid="stTextArea"] label,
    div[data-testid="stTextArea"] label p {
        color: #202b40 !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }

    /* Streamlit form input text */
    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stDateInput"] input,
    div[data-testid="stSelectbox"] input {
        color: #202b40 !important;
        -webkit-text-fill-color: #202b40 !important;
        background-color: #ffffff !important;
    }

    /* Input placeholders */
    div[data-testid="stTextInput"] input::placeholder,
    div[data-testid="stNumberInput"] input::placeholder,
    div[data-testid="stTextArea"] textarea::placeholder {
        color: #8b95aa !important;
        -webkit-text-fill-color: #8b95aa !important;
        opacity: 1 !important;
    }

    /* Navigation */
    .nav-title {
        color: #64748b;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Header */
    .welcome {
        font-size: 42px;
        font-weight: 850;
        color: #17213a;
        letter-spacing: -1.2px;
        margin-bottom: 4px;
        background: linear-gradient(90deg, #17213a 0%, #4c1d95 55%, #087f8c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        font-size: 17px;
        color: #71809a;
        margin-bottom: 25px;
    }

    .today-label {
        display: inline-block;
        padding: 8px 13px;
        margin: 3px 0 22px 0;
        border-radius: 999px;
        background: linear-gradient(90deg, #ede9fe, #ecfeff);
        color: #4c1d95;
        font-size: 13px;
        font-weight: 750;
        border: 1px solid #ddd6fe;
    }

    /* Cards */
    .metric-card {
        padding: 25px;
        border-radius: 20px;
        min-height: 145px;
        color: white;
        box-shadow: 0 10px 25px rgba(60, 40, 100, 0.12);
    }

    .purple-card {
        background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%);
    }

    .blue-card {
        background: linear-gradient(135deg, #06b6d4 0%, #2563eb 100%);
    }

    .green-card {
        background: linear-gradient(135deg, #14b8a6 0%, #0f766e 100%);
    }

    .red-card {
        background: linear-gradient(135deg, #f97316 0%, #e11d48 100%);
    }

    .card-title {
        font-size: 16px;
        font-weight: 600;
        opacity: 0.9;
    }

    .card-value {
        font-size: 31px;
        font-weight: 800;
        margin-top: 12px;
    }

    .card-description {
        font-size: 14px;
        margin-top: 5px;
        opacity: 0.85;
    }

    /* White content cards */
    .content-card {
        background: rgba(255,255,255,0.94);
        border: 1px solid #e8e7f2;
        border-radius: 22px;
        padding: 25px;
        box-shadow: 0 14px 35px rgba(31, 41, 55, 0.07);
        margin-top: 25px;
        backdrop-filter: blur(8px);
    }

    .section-title {
        font-size: 23px;
        font-weight: 750;
        color: #202b40;
        margin-bottom: 18px;
    }

    /* Expense item */
    .expense-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 15px 5px;
        border-bottom: 1px solid #f0f1f5;
    }

    .expense-left {
        display: flex;
        align-items: center;
        gap: 13px;
    }

    .expense-icon {
        width: 46px;
        height: 46px;
        border-radius: 14px;
        background: #f1eaff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
    }

    .expense-name {
        font-size: 16px;
        font-weight: 650;
        color: #253047;
    }

    .expense-category {
        font-size: 13px;
        color: #71809a;
        margin-top: 3px;
    }

    .expense-date {
        font-size: 12px;
        color: #8b95aa;
        margin-top: 2px;
    }

    .expense-amount {
        color: #6d28d9;
        font-size: 17px;
        font-weight: 750;
    }

    /* Budget */
    .budget-number {
        font-size: 32px;
        font-weight: 800;
        color: #202b40;
    }

    .budget-text {
        color: #8b95aa;
        font-size: 15px;
    }

    /* Sidebar profile */
    .profile {
        border-top: 1px solid #eeeef5;
        padding-top: 20px;
        margin-top: 30px;
    }

    .profile-name {
        font-weight: 700;
        color: #202b40;
        font-size: 15px;
    }

    .profile-info {
        color: #94a3b8;
        font-size: 13px;
        margin-top: 3px;
    }
    /* -------------------------------------------------
       STREAMLIT TEXT COLOR FIX
    ------------------------------------------------- */

    [data-testid="stAppViewContainer"] h1,
    [data-testid="stAppViewContainer"] h2,
    [data-testid="stAppViewContainer"] h3 {
        color: #202b40 !important;
    }

    [data-testid="stAppViewContainer"] p {
        color: #64748b !important;
    }

    /* Metric labels */
    [data-testid="stMetricLabel"] {
        color: #64748b !important;
    }

    /* Metric values */
    [data-testid="stMetricValue"] {
        color: #202b40 !important;
    }

    /* Markdown text */
    [data-testid="stAppViewContainer"] [data-testid="stMarkdownContainer"] p {
        color: #202b40 !important;
    }

    /* Success / info messages */
    [data-testid="stAlert"] p {
        color: inherit !important;
    }   
    /* Sidebar navigation buttons — match the date badge */
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button {
        background: linear-gradient(90deg, #ede9fe 0%, #ecfeff 100%) !important;
        color: #4c1d95 !important;
        border: 1px solid #ddd6fe !important;
        border-radius: 16px !important;
        box-shadow: 0 6px 16px rgba(76, 29, 149, 0.06) !important;
        transition: all 0.2s ease !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
        background: linear-gradient(90deg, #e5ddff 0%, #ddfbff 100%) !important;
        border-color: #c4b5fd !important;
        color: #3b176f !important;
        transform: translateY(-1px);
        box-shadow: 0 9px 20px rgba(76, 29, 149, 0.10) !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stButton"] > button * {
        color: #4c1d95 !important;
        fill: #4c1d95 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stButton"] > button p,
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button div,
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button span {
        color: #4c1d95 !important;
    }

    /* -------------------------------------------------
       BUTTON VISIBILITY + PROFESSIONAL UI FIX
       ------------------------------------------------- */

    /* Main-page buttons */
    [data-testid="stAppViewContainer"] div[data-testid="stButton"] > button {
        background-color: #111827 !important;
        color: #ffffff !important;
        border: 1px solid #111827 !important;
        border-radius: 12px !important;
        min-height: 48px !important;
    }

    [data-testid="stAppViewContainer"] div[data-testid="stButton"] > button:hover {
        background-color: #1f2937 !important;
        border-color: #1f2937 !important;
        color: #ffffff !important;
    }

    /* Form submit buttons such as Save Profile / Save Budget */
    [data-testid="stFormSubmitButton"] button,
    [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #6d28d9, #7c3aed) !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 48px !important;
        font-weight: 700 !important;
        box-shadow: 0 6px 16px rgba(109, 40, 217, 0.18) !important;
    }

    [data-testid="stFormSubmitButton"] button:hover,
    [data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #5b21b6, #6d28d9) !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    [data-testid="stFormSubmitButton"] button *,
    [data-testid="stFormSubmitButton"] > button * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        fill: #ffffff !important;
    }

    /* Regular action buttons */
    [data-testid="stAppViewContainer"] div[data-testid="stButton"] > button {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    [data-testid="stAppViewContainer"] div[data-testid="stButton"] > button * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    [data-testid="stAppViewContainer"] div[data-testid="stButton"] > button p,
    [data-testid="stAppViewContainer"] div[data-testid="stButton"] > button span,
    [data-testid="stAppViewContainer"] div[data-testid="stButton"] > button div {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        fill: #ffffff !important;
    }

    /* Make markdown lists/text visible.
       The old global paragraph rule was making some
       Settings/About content too faint on the page. */
    [data-testid="stAppViewContainer"] [data-testid="stMarkdownContainer"] li,
    [data-testid="stAppViewContainer"] [data-testid="stMarkdownContainer"] ul,
    [data-testid="stAppViewContainer"] [data-testid="stMarkdownContainer"] ol {
        color: #202b40 !important;
    }

    [data-testid="stAppViewContainer"] [data-testid="stMarkdownContainer"] li::marker {
        color: #6d28d9 !important;
    }

    [data-testid="stAppViewContainer"] [data-testid="stMarkdownContainer"] strong {
        color: #202b40 !important;
    }

    /* Streamlit toggle label */
    [data-testid="stAppViewContainer"] [data-testid="stToggle"] label,
    [data-testid="stAppViewContainer"] [data-testid="stToggle"] label p {
        color: #202b40 !important;
    }

    /* Give Settings sections a little breathing room. */
    [data-testid="stAppViewContainer"] hr {
        border-color: #e5e7eb !important;
    }

    /* Final sidebar navigation visibility override.
       Streamlit's later global button rules were turning the sidebar
       labels white on the light gradient background. */
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button,
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button p,
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button span,
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button div {
        color: #4c1d95 !important;
        -webkit-text-fill-color: #4c1d95 !important;
        fill: #4c1d95 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover,
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover p,
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover span,
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover div {
        color: #3b176f !important;
        -webkit-text-fill-color: #3b176f !important;
    }

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# DATA FROM EXISTING PYTHON LOGIC
# -------------------------------------------------

expenses = main.expenses

total_spent = sum(
    expense["amount"]
    for expense in expenses
)

number_of_expenses = len(expenses)

# Persistent monthly budget for the current Streamlit session.
# It starts at ₹8,000 and is updated from the Budget page.
if "monthly_budget" not in st.session_state:
    st.session_state.monthly_budget = 8000.0

# Settings state
if "user_name" not in st.session_state:
    st.session_state.user_name = "Palak"

if "budget_alerts" not in st.session_state:
    st.session_state.budget_alerts = True

if "budget_reset_notice" not in st.session_state:
    st.session_state.budget_reset_notice = False

monthly_budget = st.session_state.monthly_budget

remaining = monthly_budget - total_spent

# Prevent negative "remaining" display
remaining_display = max(remaining, 0)

# Calculate budget percentage
budget_percentage = (
    (total_spent / monthly_budget) * 100
    if monthly_budget > 0
    else 0
)

# -------------------------------------------------
# DATE / TIME HELPERS
# -------------------------------------------------

today = date.today()
current_hour = datetime.now().hour

if current_hour < 12:
    greeting = "Good morning"
elif current_hour < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

def format_expense_date(expense):
    value = expense.get("date")
    if not value:
        return "Date not recorded"
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").strftime("%d %b %Y")
    except (ValueError, TypeError):
        return str(value)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.markdown("""
    <div class="brand">
        <div class="brand-icon">SP</div>
        <div>
            <div class="brand-name">Spendly</div>
            <div class="brand-subtitle">Student Daily Expense Tracker</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="nav-title">MENU</div>',
        unsafe_allow_html=True
    )

    if st.button("Overview", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

    if st.button("Record Expense", use_container_width=True):
        st.session_state.page = "Add Expense"
        st.rerun()

    if st.button("Transactions", use_container_width=True):
        st.session_state.page = "History"
        st.rerun()

    if st.button("Insights", use_container_width=True):
        st.session_state.page = "Analytics"
        st.rerun()

    if st.button("Budget Planner", use_container_width=True):
        st.session_state.page = "Budget"
        st.rerun()

    if st.button("Preferences", use_container_width=True):
        st.session_state.page = "Settings"
        st.rerun()

    st.markdown(f"""
    <div class="profile">
        <div class="profile-name">{st.session_state.user_name}</div>
        <div class="profile-info">B.Tech CSE • Student</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# DASHBOARD PAGE
# -------------------------------------------------

if st.session_state.page == "Dashboard":

    # -------------------------------------------------
    # HEADER
    # -------------------------------------------------

    st.markdown(
        f'<div class="welcome">{greeting}, {st.session_state.user_name}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Track your spending and stay within your budget.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="today-label">{today.strftime("%A, %d %B %Y")}</div>',
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # QUICK ADD BUTTON
    # -------------------------------------------------

    add_col1, add_col2 = st.columns([6, 1])

    with add_col2:
        if st.button("Record Expense", use_container_width=True):
            st.session_state.page = "Add Expense"
            st.rerun()

    # -------------------------------------------------
    # SUMMARY CARDS
    # -------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card purple-card">
            <div class="card-title">Total Spent</div>
            <div class="card-value">₹{total_spent:,.0f}</div>
            <div class="card-description">
                Across {number_of_expenses} transaction(s)
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card green-card">
            <div class="card-title">Transactions</div>
            <div class="card-value">{number_of_expenses}</div>
            <div class="card-description">
                Recorded transactions
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card blue-card">
            <div class="card-title">Monthly Budget</div>
            <div class="card-value">₹{monthly_budget:,.0f}</div>
            <div class="card-description">
                Monthly spending limit
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        if remaining >= 0:
            st.markdown(f"""
            <div class="metric-card green-card">
                <div class="card-title">Remaining</div>
                <div class="card-value">₹{remaining_display:,.0f}</div>
                <div class="card-description">
                    Budget available
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            over_budget = abs(remaining)

            st.markdown(f"""
            <div class="metric-card red-card">
                <div class="card-title">Over Budget</div>
                <div class="card-value">₹{over_budget:,.0f}</div>
                <div class="card-description">
                    Limit exceeded
                </div>
            </div>
            """, unsafe_allow_html=True)

    # -------------------------------------------------
    # BUDGET PROGRESS
    # -------------------------------------------------

    st.markdown("""
    <div class="content-card">
        <div class="section-title">Budget Progress</div>
    """, unsafe_allow_html=True)

    budget_col1, budget_col2 = st.columns([4, 1])

    with budget_col1:

        st.markdown(
            f'<div class="budget-text">₹{total_spent:,.0f} spent of ₹{monthly_budget:,.0f}</div>',
            unsafe_allow_html=True
        )

        # Streamlit progress accepts values between 0 and 1
        progress_value = min(budget_percentage / 100, 1)

        st.progress(progress_value)

    with budget_col2:

        if budget_percentage <= 100:
            budget_display = f"{budget_percentage:.0f}%"
        else:
            budget_display = f"Over {budget_percentage:.0f}%"

        st.markdown(
            f'<div class="budget-number">{budget_display}</div>',
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------
    # BUDGET ALERT
    # -------------------------------------------------

    if st.session_state.budget_alerts and monthly_budget > 0:

        if budget_percentage > 100:
            st.error(
                f"Limit exceeded by ₹{abs(remaining):,.0f}. "
                "Consider reducing non-essential spending."
            )

        elif budget_percentage >= 80:
            st.warning(
                f"You have used {budget_percentage:.1f}% of your monthly budget. "
                f"₹{max(remaining, 0):,.0f} remaining."
            )

        elif budget_percentage >= 50:
            st.info(
                f"You have used {budget_percentage:.1f}% of your monthly budget. "
                f"₹{max(remaining, 0):,.0f} remaining."
            )

    # -------------------------------------------------
    # SPENDING BY CATEGORY
    # -------------------------------------------------

    category_totals = {}

    for expense in expenses:

        category = expense["category"]

        category_totals[category] = (
            category_totals.get(category, 0)
            + expense["amount"]
        )

    st.markdown("""
    <div class="content-card">
        <div class="section-title">Category Breakdown</div>
    """, unsafe_allow_html=True)

    if category_totals:

        sorted_categories = sorted(
            category_totals.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for category, amount in sorted_categories:

            percentage = (
                (amount / total_spent) * 100
                if total_spent > 0
                else 0
            )

            st.markdown(
                f'<div style="color:#202b40; font-size:16px; font-weight:700; margin:12px 0 6px 0;">{category} — ₹{amount:,.0f}</div>',
                unsafe_allow_html=True
            )

            st.progress(min(percentage / 100, 1))

    else:
        st.info("Add expenses to see category-wise spending.")

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------
    # RECENT EXPENSES
    # -------------------------------------------------

    st.markdown("""
    <div class="content-card">
        <div class="section-title">Recent Transactions</div>
    """, unsafe_allow_html=True)

    if expenses:

        recent_expenses = list(reversed(expenses[-5:]))

        category_icons = {
            "Food": "FD",
            "Transport": "TR",
            "Books": "BK",
            "Entertainment": "EN",
            "Health": "HL",
            "Shopping": "SH",
            "Others": "OT"
        }

        for expense in recent_expenses:

            icon = category_icons.get(
                expense["category"],
                "OT"
            )

            expense_html = f"""
                <div class="expense-item">
                    <div class="expense-left">
                        <div class="expense-icon">{icon}</div>
                        <div>
                            <div class="expense-name">{expense["description"]}</div>
                            <div class="expense-category">{expense["category"]}</div>
                            <div class="expense-date">{format_expense_date(expense)}</div>
                        </div>
                    </div>
                    <div class="expense-amount">₹{expense["amount"]:,.0f}</div>
                </div>
            """

            st.markdown(textwrap.dedent(expense_html), unsafe_allow_html=True)

    else:
        st.info("No expenses added yet. Add your first expense!")

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# ADD EXPENSE PAGE
# -------------------------------------------------

elif st.session_state.page == "Add Expense":

    st.title("Record Expense")
    st.caption("Record your daily spending in a few simple steps.")

    with st.form("add_expense_form"):

        expense_title = st.text_input(
            "Transaction Title",
            placeholder="e.g. College lunch, Metro card..."
        )

        amount = st.number_input(
            "Amount (₹)",
            min_value=0.0,
            step=10.0,
            format="%.2f"
        )

        expense_date = st.date_input(
            "Transaction Date",
            value=date.today(),
            max_value=date.today()
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Transport",
                "Books",
                "Entertainment",
                "Health",
                "Shopping",
                "Others"
            ]
        )

        note = st.text_area(
            "Notes",
            placeholder="Add an optional note..."
        )

        submitted = st.form_submit_button(
            "Save Transaction",
            use_container_width=True
        )

        if submitted:

            if not expense_title.strip():
                st.error("Please enter an Expense Title.")

            elif amount <= 0:
                st.error("Please enter an amount greater than ₹0.")

            else:

                expense = {
                    "id": main.next_id,
                    "amount": amount,
                    "category": category,
                    "description": expense_title.strip(),
                    "date": expense_date.isoformat()
                }

                if note.strip():
                    expense["note"] = note.strip()

                main.expenses.append(expense)
                main.next_id += 1

                st.success("Expense added successfully!")

                st.session_state.page = "Dashboard"
                st.rerun()


# -------------------------------------------------
# HISTORY PAGE - TEMPORARY
# -------------------------------------------------

# -------------------------------------------------
# HISTORY PAGE
# -------------------------------------------------

elif st.session_state.page == "History":

    st.title("Transaction History")
    st.caption("Review, search, and manage your recorded transactions.")

    if not expenses:
        st.info("No expenses recorded yet.")
    else:

        # Search box
        search = st.text_input(
            "🔍 Search Expense",
            placeholder="Search by transaction title..."
        )

        # Category filter
        categories = ["All"] + sorted(
            set(expense["category"] for expense in expenses)
        )

        selected_category = st.selectbox(
            "Filter by Category",
            categories
        )

        date_filter = st.date_input(
            "Filter by Date",
            value=None,
            max_value=date.today()
        )

        # Filter expenses
        filtered_expenses = []

        for expense in reversed(expenses):

            title_match = (
                search.lower() in expense["description"].lower()
            )

            category_match = (
                selected_category == "All"
                or expense["category"] == selected_category
            )

            expense_date_value = expense.get("date")
            if date_filter and expense_date_value:
                date_match = expense_date_value == date_filter.isoformat()
            elif date_filter and not expense_date_value:
                date_match = False
            else:
                date_match = True

            if title_match and category_match and date_match:
                filtered_expenses.append(expense)

        st.markdown(
            f"### {len(filtered_expenses)} Expense(s)"
        )

                             # Display expenses
        filtered_expenses.sort(
            key=lambda item: item.get("date", ""),
            reverse=True
        )

        for index, expense in enumerate(filtered_expenses):

            col1, col2, col3 = st.columns([5, 2, 1])

            with col1:
                st.markdown(
                    f'''
                    <div class="expense-item">
                        <div class="expense-left">
                            <div class="expense-icon">TX</div>
                            <div>
                                <div class="expense-name">
                                    {expense["description"]}
                                </div>
                                <div class="expense-category">
                                    {expense["category"]}
                                </div>
                                <div class="expense-date">
                                    {format_expense_date(expense)}
                                </div>
                            </div>
                        </div>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f'''
                    <div style="
                        font-size:18px;
                        font-weight:700;
                        color:#6d28d9;
                        padding-top:15px;
                    ">
                        ₹{expense["amount"]:,.0f}
                    </div>
                    ''',
                    unsafe_allow_html=True
                )

            with col3:
                if st.button(
                    "Delete",
                    key=f"history_delete_{index}_{expense['id']}"
                ):
                    main.expenses.remove(expense)
                    st.success("Expense deleted successfully!")
                    st.rerun()



# -------------------------------------------------
# ANALYTICS PAGE
# -------------------------------------------------

elif st.session_state.page == "Analytics":

    st.title("Spending Insights")
    st.caption("Understand your spending patterns and category-wise distribution.")

    # ---------------------------------------------
    # BASIC CALCULATIONS
    # ---------------------------------------------

    total_spent = sum(
        expense["amount"]
        for expense in expenses
    )

    total_transactions = len(expenses)

    average_expense = (
        total_spent / total_transactions
        if total_transactions > 0
        else 0
    )

    # ---------------------------------------------
    # CATEGORY TOTALS
    # ---------------------------------------------

    category_totals = {}

    for expense in expenses:

        category = expense["category"]

        category_totals[category] = (
            category_totals.get(category, 0)
            + expense["amount"]
        )

    # ---------------------------------------------
    # TOP CATEGORY
    # ---------------------------------------------

    if category_totals:

        top_category = max(
            category_totals,
            key=category_totals.get
        )

        top_category_amount = category_totals[
            top_category
        ]

    else:

        top_category = "N/A"
        top_category_amount = 0

    # ---------------------------------------------
    # SUMMARY CARDS
    # ---------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Spent",
            f"₹{total_spent:,.0f}"
        )

    with col2:
        st.metric(
            "Transactions",
            total_transactions
        )

    with col3:
        st.metric(
            "Average Expense",
            f"₹{average_expense:,.0f}"
        )

    with col4:
        st.metric(
            "Top Category",
            top_category
        )

    st.divider()

    # ---------------------------------------------
    # CATEGORY-WISE SPENDING
    # ---------------------------------------------

    st.subheader("Category Breakdown")

    if category_totals:

        sorted_categories = sorted(
            category_totals.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for category, amount in sorted_categories:

            percentage = (
                (amount / total_spent) * 100
                if total_spent > 0
                else 0
            )

            st.write(
                f"**{category}** — "
                f"₹{amount:,.0f} "
                f"({percentage:.1f}%)"
            )

            st.progress(
                min(percentage / 100, 1.0)
            )

    else:

        st.info(
            "No expenses available. "
            "Add an expense to see analytics."
        )

    st.divider()

    # ---------------------------------------------
    # TOP SPENDING CATEGORY
    # ---------------------------------------------

    if category_totals:

        st.subheader("Highest Spending Category")

        st.success(
            f"{top_category} — "
            f"₹{top_category_amount:,.0f}"
        )


# -------------------------------------------------
# BUDGET PAGE
# -------------------------------------------------

elif st.session_state.page == "Budget":

    st.title("Budget Planner")
    st.caption("Set a monthly spending limit and monitor your progress.")

    # Current budget summary
    budget_col1, budget_col2, budget_col3 = st.columns(3)

    with budget_col1:
        st.markdown("**Monthly Budget**")
        st.markdown(f"### ₹{monthly_budget:,.0f}")

    with budget_col2:
        st.markdown("**Total Spent**")
        st.markdown(f"### ₹{total_spent:,.0f}")

    with budget_col3:
        st.markdown("**Remaining**")
        if remaining >= 0:
            st.markdown(f"### ₹{remaining:,.0f}")
        else:
            st.markdown(f"### -₹{abs(remaining):,.0f}")

    st.divider()

    # Set / update budget
    st.subheader("Set Monthly Budget")

    with st.form("budget_form"):
        new_budget = st.number_input(
            "Monthly Budget (₹)",
            min_value=0.0,
            value=float(monthly_budget),
            step=100.0,
            format="%.0f"
        )

        save_budget = st.form_submit_button(
            "Save Budget",
            use_container_width=True
        )

    if save_budget:
        if new_budget <= 0:
            st.error("Please enter a budget greater than ₹0.")
        else:
            st.session_state.monthly_budget = float(new_budget)
            st.success(f"Monthly budget updated to ₹{new_budget:,.0f}.")
            st.rerun()

    # Recalculate using the current saved budget
    current_budget = st.session_state.monthly_budget
    current_remaining = current_budget - total_spent
    current_percentage = (
        (total_spent / current_budget) * 100
        if current_budget > 0
        else 0
    )

    st.subheader("Budget Progress")
    st.progress(min(current_percentage / 100, 1.0))

    if current_remaining >= 0:
        st.success(
            f"✅ You have ₹{current_remaining:,.0f} remaining from your monthly budget."
        )
    else:
        st.error(
            f"⚠️ You are ₹{abs(current_remaining):,.0f} over your monthly budget."
        )

    st.markdown(
        f"**₹{total_spent:,.0f} spent of ₹{current_budget:,.0f}** — "
        f"{current_percentage:.1f}% used"
    )

    # Simple budget guidance
    if current_percentage < 50:
        st.info("You are comfortably within your budget. Keep it up!")
    elif current_percentage < 80:
        st.warning("You have used more than half of your budget. Keep an eye on spending.")
    elif current_percentage <= 100:
        st.warning("Your budget is getting close to the limit.")
    else:
        st.error("You have exceeded your monthly budget.")


# -------------------------------------------------
# SETTINGS PAGE
# -------------------------------------------------

elif st.session_state.page == "Settings":

    st.title("Preferences")
    st.caption("Personalize your experience and manage your tracker settings.")

    if st.session_state.budget_reset_notice:
        st.success("Budget has been reset to ₹8,000.")
        st.session_state.budget_reset_notice = False

    # -------------------------------------------------
    # PROFILE SETTINGS
    # -------------------------------------------------

    st.subheader("Profile")

    with st.form("profile_settings_form"):

        new_name = st.text_input(
            "Display Name",
            value=st.session_state.user_name,
            placeholder="Enter your name"
        )

        save_profile = st.form_submit_button(
            "Save Profile",
            use_container_width=True
        )

    if save_profile:

        if not new_name.strip():
            st.error("Please enter your name.")

        else:
            st.session_state.user_name = new_name.strip()
            st.success("Profile updated successfully!")
            st.rerun()

    st.divider()

    # -------------------------------------------------
    # BUDGET ALERT SETTINGS
    # -------------------------------------------------

    st.subheader("Budget Alerts")

    budget_alerts = st.toggle(
        "Enable budget warnings",
        value=st.session_state.budget_alerts,
        key="budget_alert_toggle"
    )

    if budget_alerts != st.session_state.budget_alerts:
        st.session_state.budget_alerts = budget_alerts

    if st.session_state.budget_alerts:
        st.success(
            "Budget warnings are enabled. "
            "Spendly will show alerts on the Dashboard when spending gets high."
        )
    else:
        st.info(
            "Budget warnings are disabled. "
            "You can still see your budget progress normally."
        )

    st.divider()

    # -------------------------------------------------
    # DATA MANAGEMENT
    # -------------------------------------------------

    st.subheader("Data Management")

    st.warning(
        "These actions affect your current Spendly session. "
        "Deleted expenses cannot be recovered."
    )

    data_col1, data_col2 = st.columns(2)

    with data_col1:

        if st.button(
            "Clear All Transactions",
            use_container_width=True
        ):

            if expenses:

                main.expenses.clear()

                st.success("All transactions have been cleared.")
                st.rerun()

            else:

                st.info("There are no expenses to clear.")

    with data_col2:

        if st.button(
            "Reset Budget",
            use_container_width=True
        ):

            st.session_state.monthly_budget = 8000.0
            st.session_state.budget_reset_notice = True
            st.rerun()

    st.divider()

    # -------------------------------------------------
    # ABOUT
    # -------------------------------------------------

    st.subheader("About Spendly")

    # Use native Streamlit components here instead of raw HTML.
    # This prevents the About content from being rendered as a code block.
    with st.container(border=True):

        st.markdown("### Spendly — Student Daily Expense Tracker")

        st.write(
            "A simple expense and budget management application "
            "designed to help students track daily spending."
        )

        st.markdown("#### Features")

        st.markdown(
            """
            - ✓ Expense tracking
            - ✓ Expense history and search
            - ✓ Date-wise transaction records
            - ✓ Category-wise analytics
            - ✓ Monthly budget management
            - ✓ Budget progress tracking
            - ✓ Personal settings
            """
        )

        st.divider()
        st.caption("Version 1.0")
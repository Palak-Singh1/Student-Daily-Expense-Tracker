import streamlit as st
from supabase import create_client


def get_client():
    """Create a Supabase client from Streamlit secrets."""
    try:
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["anon_key"]
    except Exception as exc:
        raise RuntimeError(
            "Missing [supabase].url or [supabase].anon_key in Streamlit secrets."
        ) from exc
    if not url or not key or "YOUR_" in url or "YOUR_" in key:
        raise RuntimeError("Supabase URL/key are not configured.")
    return create_client(url, key)


def get_profile(client, user_id):
    response = (
        client.table("profiles")
        .select("user_id, display_name, monthly_budget, budget_alerts")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )
    return response.data[0] if response.data else None


def save_profile(client, user_id, display_name, monthly_budget, budget_alerts):
    payload = {
        "user_id": user_id,
        "display_name": display_name,
        "monthly_budget": float(monthly_budget),
        "budget_alerts": bool(budget_alerts),
    }
    response = client.table("profiles").upsert(payload, on_conflict="user_id").execute()
    return response.data[0] if response.data else payload


def get_expenses(client, user_id):
    response = (
        client.table("expenses")
        .select("id, amount, category, description, expense_date, note")
        .eq("user_id", user_id)
        .order("expense_date", desc=False)
        .order("id", desc=False)
        .execute()
    )
    result = []
    for row in response.data or []:
        item = {
            "id": int(row["id"]),
            "amount": float(row["amount"]),
            "category": row["category"],
            "description": row["description"],
            "date": row["expense_date"],
        }
        if row.get("note"):
            item["note"] = row["note"]
        result.append(item)
    return result


def add_expense(client, user_id, expense):
    payload = {
        "user_id": user_id,
        "amount": float(expense["amount"]),
        "category": expense["category"],
        "description": expense["description"],
        "expense_date": expense.get("date"),
        "note": expense.get("note", ""),
    }
    return client.table("expenses").insert(payload).execute().data[0]


def delete_expense(client, user_id, expense_id):
    return (
        client.table("expenses")
        .delete()
        .eq("user_id", user_id)
        .eq("id", int(expense_id))
        .execute()
    )


def clear_expenses(client, user_id):
    return client.table("expenses").delete().eq("user_id", user_id).execute()

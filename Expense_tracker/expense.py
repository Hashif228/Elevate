import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

conn = sqlite3.connect('expense.db')
c = conn.cursor()
j=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                date TEXT,
                category TEXT,
                amount REAL)''')
conn.commit()
def add_expense(date, category, amount):
    c.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)",
              (date, category, amount))
    conn.commit()

def update_expense(expense_id, date, category, amount):
    c.execute("UPDATE expenses SET date=?, category=?, amount=? WHERE id=?",
              (date, category, amount, expense_id))
    conn.commit()

def delete_expense(expense_id):
    c.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()

def view_expenses():
    c.execute("SELECT * FROM expenses")
    return c.fetchall()

def plot_monthly_expenses():
    c.execute("SELECT date, category, amount FROM expenses order by date")
    rows = c.fetchall()
    monthly_totals = {}
    for date, category, amount in rows:
        month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
        if month not in monthly_totals:
            monthly_totals[month] = 0
        monthly_totals[month] += amount

    months = list(monthly_totals.keys())
    totals = list(monthly_totals.values())

    plt.figure(figsize=(10, 5))
    plt.plot(months, totals, marker='o')
    plt.title("Monthly Spending Over Time")
    plt.xlabel("Month")
    plt.ylabel("Total Spending")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_category_pie():
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = c.fetchall()
    categories = [row[0] for row in rows]
    totals = [row[1] for row in rows]

    plt.figure(figsize=(8, 6))
    plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Spending by Category")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def plot_graphs():
    c.execute("SELECT date, category, amount FROM expenses order by date")
    rows = c.fetchall()
    monthly_totals = {}
    for date, category, amount in rows:
        month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
        if month not in monthly_totals:
            monthly_totals[month] = 0
        monthly_totals[month] += amount

    months = list(monthly_totals.keys())
    totalsl = list(monthly_totals.values())


    j.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rowsj = j.fetchall()
    categories = [row[0] for row in rowsj]
    totalsp = [row[1] for row in rowsj]



    plt.figure(figsize=(4, 6))
    plt.subplot(2,1,1)
    plt.pie(totalsp, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Spending by Category")
    plt.axis('equal')
    plt.subplot(2,1,2)
    plt.plot(months, totalsl, marker='o')
    plt.title("Monthly Spending Over Time")
    plt.xlabel("Month")
    plt.ylabel("Total Spending")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()





def export_pdf_report(filename="Report.pdf"):
    conn = sqlite3.connect("expense.db")
    c = conn.cursor()
    c.execute("SELECT date, category, amount FROM expenses")
    t = conn.cursor()
    t.execute("SELECT SUM(amount) FROM expenses")
    total=t.fetchone()[0]
    rows = c.fetchall()
    conn.close()

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 40, "Expense Report")

    c.setFont("Helvetica", 12)
    y = height - 80
    c.drawString(50, y, "Date")
    c.drawString(200, y, "Category")
    c.drawString(400, y, "Amount")

    y -= 20
    for row in rows:
        date, category, amount = row
        c.drawString(50, y, str(date))
        c.drawString(200, y, category)
        c.drawString(400, y, str(amount))
        y -= 20
        if y < 40:
            c.showPage()
            y = height - 40
    c.drawString(400, y, f"Total={total}")
    c.save()
    print(f"PDF report saved as {filename}")





def menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Plot Monthly Expenses")
        print("6. Plot Category Pie")
        print("7. Plot both graphs")
        print("8. Export details as a pdf")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            amount = float(input("Amount: "))
            add_expense(date, category, amount)
        elif choice == '2':
            expenses = view_expenses()
            for exp in expenses:
                print(exp)
        elif choice == '3':
            expense_id = int(input("Expense ID to update: "))
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            update_expense(expense_id, date, category, amount)
        elif choice == '4':
            expense_id = int(input("Expense ID to delete: "))
            delete_expense(expense_id)
        elif choice == '5':
            plot_monthly_expenses()
        elif choice == '6':
            plot_category_pie()
        elif choice == '7':
            plot_graphs()
        elif choice=='8':
            export_pdf_report()
        elif choice == '0':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
    conn.close()

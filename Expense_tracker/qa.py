import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

conn = sqlite3.connect('expense.db')
c = conn.cursor()
data = [
    ('2025-02-01', 'Shopping', 1785.50),
    ('2025-02-02', 'Cinema', 800),
    ('2025-01-03', 'Shopping', 545.00),
]
c.executemany("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)", data)

conn.commit()

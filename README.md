# 💸 FINLA: Financial Life Assistant

> A personalized financial tracker and advisor built entirely in Python.  
> Track. Plan. Grow. — all from a minimalist, Dockerized app that just works.

---

## 🌟 Features

- 🔐 **Secure Login/Signup System**
- 📊 **Dashboard with Visualized Insights**
- 💰 **Add & Manage Transactions (Recurring + One-time)**
- 🔔 **Low Balance & Savings Alerts**
- 🧮 **Export Monthly/Yearly Reports**
- 📝 **Quote of the Day** – curated from Warren Buffet & other financial giants
- 🛠️ **Settings Page** to update thresholds, user data, and preferences
- ☁️ **Data Stored in CSVs** (hostel-friendly, no DB needed)
- 🐳 **Dockerized for Simple Deployment**

---

## 📸 Screenshots  
*(Coming soon: UI previews of dashboard, transaction manager, and alerts)*

---

## 🚀 Quickstart (Docker Method)

Make sure you have Docker installed.

```bash
# Clone this repo
git clone https://github.com/lathigamohan/finla.git
cd finla

# Build Docker image
docker build -t finla .

# Run the app
docker run -p 5000:5000 finla

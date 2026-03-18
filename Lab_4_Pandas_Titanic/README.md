# Lab 4: Data Analysis with Pandas (Titanic Dataset)

## Overview (Roman Urdu Mein)
Is lab mein humne **Pandas** library ke zariye real-world data handling seekhi hai. Titanic dataset use karne ka maqsad ye tha ke hum samajh sakein ke kasy gande (messy) data ko AI model ke liye tayaar kiya jata hai.

### Tasks Performed (Step-by-Step):
1. **Task 18 (Data Loading)**: Seaborn library ke zariye Titanic ka industrial dataset load kiya (`sns.load_dataset`).
2. **Task 19 (Exploration)**: `head()` aur `shape` use kar ke data ka overview liya.
3. **Task 20 (Filtering)**: Boolean Indexing use kar ke specific passengers (e.g., Female Survivors) ka data nikaala.
4. **Task 21 (Sorting)**: Data ko Ticket Price (Fare) aur Class ke hisaab se arrange kiya.
5. **Task 22 (Handling Missing Data)**: `fillna()` use kar ke khali Age ko average se bhara aur `dropna()` se invalid records nikaal diye.
6. **Task 23 (Manipulation)**: Naye features (Family Size) add kiye aur columns ko professional names (Ticket_Price) diye.

---

## 🤖 Industry Discussion: How ML Engineers Work
Humne is lab ke doran ye bhi seekha ke industry mein ML Engineer kasy kaam karte hain:

### 1. Agentic AI vs Manual Coding
*   **Agentic Approach**: Aaj kal ke engineers (jaise hum ne Churn AI banaya) Gemini/Grok APIs use karte hain jo khud hi detect karti hain ke data kaisa hai aur code likh deti hain.
*   **Importance of Manual Skills**: Manual Pandas seekhna zaroori hai taake jab AI ghalat logic lagaye (jaise Age mein ghalat value bhar dena), toh aap usey **Debug** kar sakein.

### 2. SQL integration
*   Data asals mein SQL databases se aata hai. `pd.read_sql` command use kar ke hum SQL data ko Pandas mein laate hain.

### 3. AI Orchestrator Role
*   Aik modern ML Engineer asals mein aik "Architect" hota hai jo different AI models aur data libraries ko jorr kar aik **"Automated Agent"** banata hai.

---

### Live Lab on Google Colab:
[View Lab 4 Notebook on Colab](https://colab.research.google.com/drive/1KBhZIJoDtIp5F-5zNpE-NFqz9s0MDs-a#scrollTo=hZASneOdjoOq)

---

Developed with ⚡ by Muhammad Usman Ray

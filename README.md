# **AGENTIC REVIEW TREND ANALYSIS**
### **Swiggy – Google Play Store Reviews**

---

## **📌 PROBLEM STATEMENT**

Product teams need a reliable way to track **evolving user issues, feature requests, and feedback** from app store reviews.

Traditional topic modeling techniques such as **LDA** and **BERTopic** often **fragment semantically similar topics**, resulting in inaccurate and unstable trends.

This project implements an **Agentic AI system** that consumes **daily batches of Google Play Store reviews** and generates a **trend analysis report from T-30 to T**.

---

## **🤖 WHY AGENTIC AI?**

This solution uses **multiple AI agents**, each with a clearly defined responsibility:

- **High recall topic extraction**
- **Semantic topic consolidation**
- **Dynamic topic discovery**
- **Daily trend aggregation**

This approach avoids topic fragmentation and ensures **accurate, product-ready trend signals**.

---

video:https://drive.google.com/file/d/14FqMillx9Xvz4wJ-pawJTMBqPEunJpbN/view?usp=sharing
## **🧠 SYSTEM ARCHITECTURE**

---

## **🧩 AGENT RESPONSIBILITIES**

### **1️⃣ INGESTION AGENT**
- Fetches Google Play Store reviews
- Groups reviews by **date**
- Treats each date as a **daily batch**

---

### **2️⃣ TOPIC EXTRACTION AGENT**
- Extracts:
  - **Issues**
  - **Complaints**
  - **Feature requests**
  - **General feedback**
- Optimized for **high recall**
- Uses **LLM-based semantic understanding**

---

### **3️⃣ TOPIC DEDUPLICATION AGENT**
- Prevents topic fragmentation
- Consolidates semantically similar topics

**Example:**
- “Delivery guy was rude”
- “Delivery partner behaved badly”
- “Delivery person was impolite”

➡ **Canonical Topic:** **Delivery partner rude**

---

### **4️⃣ CANONICAL TOPIC TAXONOMY**
- Maintains a **living topic store**
- Stores normalized topic names
- Enables consistent long-term trend tracking

---

### **5️⃣ TREND AGGREGATION AGENT**
- Counts topic occurrences per day
- Generates trend table from **T-30 to T**
- Output is **directly consumable by product teams**

---

## **📊 OUTPUT REPORT FORMAT**

| **Topic** | **Jun 1** | **Jun 2** | **…** | **Jun 30** |
|----------|----------|----------|------|----------|
| **Delivery issue** | 12 | 8 | … | 23 |
| **Food stale** | 5 | 7 | … | 11 |
| **Delivery partner rude** | 8 | 12 | … | 9 |
| **Maps not working** | 2 | 4 | … | 5 |
| **Instamart open all night** | 1 | 0 | … | 4 |

---

## **⚙️ TECHNOLOGY STACK**
- **Python**
- **OpenAI API**
- **google-play-scraper**
- **Pandas**
- **Agentic AI design**

---

## **🚀 HOW TO RUN**

```bash
pip install -r requirements.txt
python main.py





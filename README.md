Agentic Review Trend Analysis

Swiggy – Google Play Store Reviews

🔍 Problem Statement

Product teams need a reliable way to track evolving user issues, feature requests, and feedback from app store reviews.
Traditional topic modeling techniques (LDA, BERTopic) often fragment similar topics, leading to inaccurate trends.

This project builds an Agentic AI system that consumes daily batches of Google Play Store reviews and generates a trend analysis report showing topic frequency from T-30 to T.

🤖 Why Agentic AI?

This solution uses multiple AI agents, each with a clearly defined responsibility:

High recall topic extraction

Semantic topic consolidation

Dynamic topic discovery

Daily trend aggregation

This avoids topic fragmentation and ensures accurate trend signals for product decision-making.

🧠 Agent Architecture
Daily Google Play Reviews
        ↓
Ingestion Agent
        ↓
Topic Extraction Agent (LLM-based)
        ↓
Topic Deduplication Agent (Semantic Matching)
        ↓
Canonical Topic Taxonomy
        ↓
Trend Aggregation Agent
        ↓
T-30 → T Trend Report

🧩 Agents Overview
1️⃣ Ingestion Agent

Fetches Google Play Store reviews

Groups reviews by date

Treats each date as a daily batch

2️⃣ Topic Extraction Agent

Uses LLMs to extract:

Issues

Complaints

Feature requests

General feedback

Designed for high recall

3️⃣ Topic Deduplication Agent

Prevents creation of duplicate or overlapping topics

Uses semantic equivalence checks to merge similar topics
Example:

“delivery guy was rude”

“delivery partner behaved badly”
→ delivery partner rude

4️⃣ Trend Aggregation Agent

Counts topic occurrences per day

Produces a trend table from T-30 to T

📊 Output Format

The final output is a CSV table consumable by product teams:

Topic	Jun 1	Jun 2	...	Jun 30
Delivery issue	12	8	...	23
Food stale	5	7	...	11
Delivery partner rude	8	12	...	9
Maps not working	2	4	...	5
Instamart open all night	1	0	...	4
⚙️ Tech Stack

Python

OpenAI API (LLM-based agents)

google-play-scraper

Pandas

Agentic AI design patterns

🚀 How to Run
pip install -r requirements.txt
export OPENAI_API_KEY=your_api_key
python main.py


Output will be generated at:

/output/trend_report.csv

🎯 Key Highlights

Daily batch processing

High recall topic extraction

Semantic topic consolidation

Dynamic discovery of new topics

Designed for real-world product analytics

📌 Use Case

This system enables product, operations, and CX teams to:

Identify trending issues

Detect emerging user requests

Track feedback changes over time

Prioritize fixes and feature improvements


# Agentic Review Trend Analysis (Swiggy)

This project implements an agentic AI system to analyze Google Play Store reviews
and generate daily topic trend reports from June 2024 onward.

## Features
- Daily batch review ingestion
- LLM-based topic extraction
- Semantic topic deduplication
- Trend analysis (T-30 to T)

## Run
```bash
export OPENAI_API_KEY=your_key
pip install -r requirements.txt
python main.py
```

Output is generated in /output/trend_report.csv

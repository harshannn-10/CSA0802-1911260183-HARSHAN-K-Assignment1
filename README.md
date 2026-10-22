# CSA08 Python Programming — Assignment 1

**Student name:** Harshan K  
**Register number:** 1911260183  
**Course:** Python Programming  
**Python version:** Python 3.10+ recommended  
**External libraries:** None; standard library only (`decimal`, `time`, `unittest`).

## Project contents
- `Task01` … `Task12`: task notes and example programs.
- `milkrate.py`: shared rate-card, validation, payment and ten-day bonus functions.
- `main.py`: interactive calculator (single entry, or ten-day total with bonus).
- `test_milkrate.py`: automated regression tests.
- `assignment_report.docx`: report template with explanations, design decisions and evidence checklist.
- `fill_report.py`: fills the report tables with real results (needs `pip install python-docx`).

## Run instructions
Open a terminal in this folder:
```bash
python milkrate.py
python main.py
python -m unittest -v
python Task10/task10.py
python fill_report.py
```
If `python` is not recognized on Windows, try `py` instead.

## Rate calculation
Standard rate: ₹30.00 per litre at 3.5% fat and 8.5% SNF. Each 0.1 percentage-point fat step changes the rate by ₹0.40; each SNF step changes it by ₹0.30. April–June uses ₹32.00 base and ₹0.45 per fat step. A ₹0.50/litre bonus applies to entries when the farmer's ten-day total exceeds 500 L.

## Assumptions that should be confirmed
- Fat range: 2.0% to 7.0%, inclusive (given in assignment).
- SNF range: assumed 0.0% to 20.0% because no SNF limits were supplied in the visible brief.
- Step counts: nearest whole 0.1 percentage-point step using Decimal `ROUND_HALF_UP`.
- Each payment and rate is rounded to two decimal places; the ten-day total sums rounded payments.
- Seasonal changes apply April through June; SNF rate remains unchanged.
- Bonus threshold is strictly greater than 500 L, not greater than or equal to 500 L.

## GitHub setup
Create a repository named `CSA08-1911260183-Assignment1`. Commit each task as it is completed. Before submission, add your own run screenshots and replace the student placeholders in the report and README.

## Important
This is a complete starter submission with code, test cases, task notes, and a report template. Run the programs on your own computer, inspect the results, capture genuine screenshots, and ensure you can explain the code for the viva. Do not claim that screenshots or timings were collected unless you actually collected them.

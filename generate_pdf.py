from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, """
Introduction to Machine Learning

Machine Learning is a subfield of Artificial Intelligence (AI) that gives computers the ability to learn from data without being explicitly programmed.

There are three types of machine learning:
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

Popular algorithms include:
- Linear Regression
- Decision Trees
- Neural Networks

Applications:
- Image Recognition
- Natural Language Processing
- Autonomous Vehicles
""")
pdf.output("sample.pdf")

# Documentation tools

Run from the repository root with Python and the dependencies in requirements.txt. The report uses Times New Roman 14 pt.

```powershell
python tools/build_visuals.py
python tools/build_docx.py
powershell -ExecutionPolicy Bypass -File tools/export_report.ps1
python tools/build_task_evidence.py
```

build_visuals.py exports editable SVG diagrams and application wireframes, with PNG/PDF copies.

build_docx.py reads docs/report.md and the exported images to create output/docx/SE-2413_Kudashov_ProbPeriod1.docx. It replaces the generated Word file. After making manual edits in Word, export that document directly or run export_report.ps1 without rebuilding the DOCX.

export_report.ps1 uses Microsoft Word on Windows to update the contents and export output/pdf/SE-2413_Kudashov_ProbPeriod1.pdf from the editable report. Close the document before running the script. Exporting PDF from Word's File menu is also supported.

build_task_evidence.py combines the actual YouTrack screenshots into output/pdf/ASTI_YouTrack_Evidence.pdf.

# Documentation tools

The scripts build PDFs, not the ASTI application. The current build uses Python, packages from requirements.txt and Times New Roman fonts installed on Windows. Run from the repository root:

```powershell
python -m pip install -r tools/requirements.txt
python tools/build_report.py
python tools/build_task_evidence.py
```

build_report.py reads docs/report.md, exports diagrams and wireframes, and produces output/pdf/ASTI_Supervisor_Review.pdf. Page images go to ignored tmp/pdfs/report/ for visual inspection.

build_task_evidence.py combines the actual screenshots under docs/task-evidence/ into output/pdf/ASTI_YouTrack_Evidence.pdf. Refresh screenshots when the board changes and inspect the resulting PDF.

Supervisor feedback is pending. The final named submission copy will be generated once the contents and version are fixed.

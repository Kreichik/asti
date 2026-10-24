"""Combine genuine YouTrack screenshots into a PDF for the submission form."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape,A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pypdfium2 as pdfium

root=Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('TimesNewRoman',r'C:/Windows/Fonts/times.ttf'))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Bold',r'C:/Windows/Fonts/timesbd.ttf'))
out=root/'output/pdf/ASTI_YouTrack_Evidence.pdf'
c=canvas.Canvas(str(out),pagesize=landscape(A4));w,h=landscape(A4)
c.setTitle('ASTI YouTrack Board and Task Evidence');c.setAuthor('Yan Kudashov')
shots=[('board.jpg','ASTI Kanban board','Eleven assigned tasks: submission preparation and software development.'),
       ('ASTI-1.jpg','ASTI-1 Completed repository and scope task','Outcome, acceptance criteria, due date, assignee, priority, status and commit.'),
       ('ASTI-5.jpg','ASTI-5 Submission task','Open critical task with deadline, dependencies and explicit submission acceptance criteria.')]
for i,(name,title,caption) in enumerate(shots,1):
 c.setFont('TimesNewRoman-Bold',14);c.drawString(32,h-34,title)
 c.setFont('TimesNewRoman',14);c.drawString(32,h-53,caption)
 c.drawString(32,h-69,'24 October 2026. Later-stage dates are provisional planning targets.')
 img=ImageReader(str(root/'docs/task-evidence'/name));iw,ih=img.getSize()
 scale=min((w-64)/iw,(h-125)/ih);dw,dh=iw*scale,ih*scale
 c.drawImage(img,(w-dw)/2,h-89-dh,dw,dh)
 c.setFont('TimesNewRoman',14);c.setFillColorRGB(0,0,1);c.drawString(32,24,'https://asti-diploma.youtrack.cloud/agiles/204-1/current');c.setFillColorRGB(0,0,0)
 c.linkURL('https://asti-diploma.youtrack.cloud/agiles/204-1/current',(32,20,470,33),relative=0)
 c.drawRightString(w-32,24,str(i));c.showPage()
c.save()
qa=root/'tmp/pdfs/tasks';qa.mkdir(parents=True,exist_ok=True)
p=pdfium.PdfDocument(str(out))
for i in range(len(p)):p[i].render(scale=1.4).to_pil().save(qa/f'page-{i+1}.png')
print(f'Built {out}; pages={len(p)}; bytes={out.stat().st_size}')

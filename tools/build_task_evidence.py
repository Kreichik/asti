"""Combine genuine YouTrack screenshots into a PDF for the submission form."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape,A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pypdfium2 as pdfium

root=Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('Arial',r'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold',r'C:/Windows/Fonts/arialbd.ttf'))
out=root/'output/pdf/ASTI_YouTrack_Evidence.pdf'
c=canvas.Canvas(str(out),pagesize=landscape(A4));w,h=landscape(A4)
c.setTitle('ASTI YouTrack Board and Task Evidence');c.setAuthor('Yan Kudashov')
shots=[('board.jpg','ASTI Kanban board','Six assigned tasks across backlog, development, review and done.'),
       ('ASTI-1.jpg','ASTI-1 Completed repository and scope task','Expected outcome, acceptance criteria, deadline, assignee, priority, status and commit link.'),
       ('ASTI-5.jpg','ASTI-5 Submission task','Open critical task with deadline, dependencies and explicit submission acceptance criteria.')]
for i,(name,title,caption) in enumerate(shots,1):
 c.setFont('Arial-Bold',15);c.drawString(32,h-34,title)
 c.setFont('Arial',9);c.drawString(32,h-53,caption)
 c.drawString(32,h-69,'Captured on 24 October 2026. Deadlines are recorded in the task descriptions.')
 img=ImageReader(str(root/'docs/task-evidence'/name));iw,ih=img.getSize()
 scale=min((w-64)/iw,(h-125)/ih);dw,dh=iw*scale,ih*scale
 c.drawImage(img,(w-dw)/2,h-89-dh,dw,dh)
 c.setFont('Arial',8);c.drawString(32,24,'https://asti-diploma.youtrack.cloud/agiles/204-1/current')
 c.linkURL('https://asti-diploma.youtrack.cloud/agiles/204-1/current',(32,20,470,33),relative=0)
 c.drawRightString(w-32,24,str(i));c.showPage()
c.save()
qa=root/'tmp/pdfs/tasks';qa.mkdir(parents=True,exist_ok=True)
p=pdfium.PdfDocument(str(out))
for i in range(len(p)):p[i].render(scale=1.4).to_pil().save(qa/f'page-{i+1}.png')
print(f'Built {out}; pages={len(p)}; bytes={out.stat().st_size}')

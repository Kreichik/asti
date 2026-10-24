"""Combine genuine YouTrack screenshots into an image-only submission PDF."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
import pypdfium2 as pdfium

root = Path(__file__).resolve().parents[1]
out = root / 'output/pdf/ASTI_YouTrack_Evidence.pdf'
shots = ['board.jpg', 'ASTI-1.jpg', 'ASTI-5.jpg']
c = canvas.Canvas(str(out))
c.setTitle('ASTI YouTrack Evidence')
c.setAuthor('Yan Kudashov')
page_width = landscape(A4)[0]
for name in shots:
    img = ImageReader(str(root / 'docs/task-evidence' / name))
    image_width, image_height = img.getSize()
    page_height = page_width * image_height / image_width
    c.setPageSize((page_width, page_height))
    c.drawImage(img, 0, 0, width=page_width, height=page_height)
    c.showPage()
c.save()
qa = root / 'tmp/pdfs/tasks'
qa.mkdir(parents=True, exist_ok=True)
pdf = pdfium.PdfDocument(str(out))
for i in range(len(pdf)):
    pdf[i].render(scale=1.4).to_pil().save(qa / f'page-{i+1}.png')
print(f'Built {out}; pages={len(pdf)}; bytes={out.stat().st_size}')
pdf.close()

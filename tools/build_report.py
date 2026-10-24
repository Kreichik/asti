"""Build ASTI review PDF and readable diagram exports using bundled Python."""
from pathlib import Path
import re, math, html
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, PageBreak, Table, TableStyle, Image, KeepTogether, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon, Ellipse, Circle
from reportlab.graphics import renderPDF, renderSVG
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parents[1]
FONT=Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('TimesNewRoman',str(FONT/'times.ttf')))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Bold',str(FONT/'timesbd.ttf')))
pdfmetrics.registerFontFamily('TimesNewRoman',normal='TimesNewRoman',bold='TimesNewRoman-Bold',italic='TimesNewRoman',boldItalic='TimesNewRoman-Bold')
INK=colors.black; LINE=colors.black; PALE=colors.white

def text(d,x,y,s,size=12,anchor='middle',bold=False):
    d.add(String(x,y,s,fontName='TimesNewRoman-Bold' if bold else 'TimesNewRoman',fontSize=size,fillColor=INK,textAnchor=anchor))

def box(d,x,y,w,h,lines,fill=PALE):
    d.add(Rect(x,y,w,h,rx=5,fillColor=fill,strokeColor=LINE,strokeWidth=1))
    for i,s in enumerate(lines):text(d,x+w/2,y+h/2+(len(lines)-1)*8-i*16,s,11)

def arrow(d,x1,y1,x2,y2,label=None,lx=None,ly=None):
    d.add(Line(x1,y1,x2,y2,strokeColor=LINE,strokeWidth=1.2))
    a=math.atan2(y2-y1,x2-x1); size=7
    pts=[x2,y2,x2-size*math.cos(a-.42),y2-size*math.sin(a-.42),x2-size*math.cos(a+.42),y2-size*math.sin(a+.42)]
    d.add(Polygon(pts,fillColor=LINE,strokeColor=LINE))
    if label:text(d,lx if lx is not None else (x1+x2)/2,ly if ly is not None else (y1+y2)/2+8,label,9)

def export(d,path):
    path.parent.mkdir(parents=True,exist_ok=True)
    renderPDF.drawToFile(d,str(path.with_suffix('.pdf')))
    renderSVG.drawToFile(d,str(path.with_suffix('.svg')))
    pdf=pdfium.PdfDocument(str(path.with_suffix('.pdf')))
    pdf[0].render(scale=2).to_pil().save(path.with_suffix('.png'))
    pdf.close()

def diagrams():
    d=Drawing(700,420)
    text(d,350,391,'ASTI system context',18,bold=True)
    box(d,20,165,145,90,['User','Account owner'])
    box(d,265,145,190,130,['ASTI assistant software','Backend / mobile / device','Web / integrations'])
    box(d,540,280,140,60,['Google Calendar','Authorized events'])
    box(d,540,170,140,60,['Notion','Selected task data'])
    box(d,540,60,140,60,['Model provider','Grounded briefing'])
    arrow(d,165,225,265,225,'Actions',215,241)
    arrow(d,265,185,165,185,'State and information',215,157)
    arrow(d,455,250,540,310)
    arrow(d,455,210,540,200)
    arrow(d,455,165,540,90)
    text(d,350,20,'External sources remain authoritative; the model does not schedule reminders.',10)
    export(d,ROOT/'docs/diagrams/context')

    d=Drawing(700,530)
    text(d,350,504,'ASTI draft component architecture',18,bold=True)
    box(d,15,400,190,55,['Flutter Android'])
    box(d,255,400,190,55,['Flutter web'])
    box(d,495,400,190,55,['Physical client'])
    box(d,95,300,260,55,['Authenticated application API'])
    box(d,450,300,220,55,['Device gateway','Pairing / protocol / action IDs'])
    arrow(d,110,400,180,355);arrow(d,350,400,275,355);arrow(d,590,400,560,355)
    box(d,175,200,350,55,['Overview / reminder scheduler / focus services'])
    arrow(d,225,300,270,255);arrow(d,560,300,470,255)
    box(d,15,100,195,55,['Synchronization worker','Calendar / Notion adapters'])
    box(d,255,100,190,55,['Relational database'])
    box(d,490,100,195,55,['Briefing service','Model adapter / fallback'])
    arrow(d,310,200,350,155);arrow(d,210,125,255,125);arrow(d,525,225,585,155)
    text(d,350,35,'Scheduler uses stored dates. Clients receive state revisions and source-linked records.',10)
    export(d,ROOT/'docs/diagrams/components')

    d=Drawing(700,610)
    text(d,350,580,'ASTI use cases',18,bold=True)
    d.add(Rect(180,45,345,500,fillColor=colors.white,strokeColor=LINE))
    text(d,352,522,'ASTI software system',12,bold=True)
    d.add(Circle(65,288,13,fillColor=None,strokeColor=INK));d.add(Line(65,275,65,237,strokeColor=INK))
    for xy in [(35,261,95,261),(65,237,40,212),(65,237,90,212)]:d.add(Line(*xy,strokeColor=INK))
    text(d,65,192,'User',12)
    names=['Connect external service','View session-start overview','Receive reminder','Snooze or acknowledge','Run focus session','Pair / revoke device','Configure assistant','Synchronize source records','Generate grounded briefing']
    for i,name in enumerate(names):
        y=480-i*47
        d.add(Ellipse(352,y,132,17,fillColor=PALE,strokeColor=LINE));text(d,352,y-4,name,11)
        if i<7:d.add(Line(95,261,220,y,strokeColor=LINE,strokeWidth=.7))
    box(d,555,130,135,60,['Calendar / Notion','Source services'])
    box(d,555,53,135,50,['Model provider'])
    d.add(Line(485,151,555,160,strokeColor=LINE))
    d.add(Line(485,104,555,78,strokeColor=LINE))
    text(d,350,20,'Viewing an overview includes generating a grounded briefing or its fallback.',9)
    export(d,ROOT/'docs/diagrams/use-cases')

    d=Drawing(900,470)
    text(d,450,440,'ASTI interaction wireframes',19,bold=True)
    headings=['Session overview','Contextual reminder','Focus session']
    for i,h in enumerate(headings):
        x=20+i*295
        d.add(Rect(x,55,270,350,rx=16,fillColor=colors.white,strokeColor=LINE,strokeWidth=1.5))
        text(d,x+135,373,h,15,bold=True)
        text(d,x+135,350,'Android / web / physical client',10)
        d.add(Line(x+20,334,x+250,334,strokeColor=LINE))
    box(d,40,239,230,65,['Next event','Exact source time and title'])
    box(d,40,153,230,65,['Tasks due soon','Source / due date / freshness'])
    text(d,155,108,'Automatic after inactivity',11)
    text(d,155,85,'Rotate to browse; click for detail',10)
    box(d,335,227,230,80,['Upcoming commitment','Title / source / exact time','Optional notification sound'])
    box(d,335,154,108,45,['Snooze']);box(d,455,154,110,45,['Acknowledge'])
    text(d,450,108,'Rotate to select; click to confirm',10)
    text(d,450,85,'Source deadline remains unchanged',10)
    d.add(Circle(745,252,58,fillColor=PALE,strokeColor=LINE))
    text(d,745,248,'Remaining time',12,bold=True)
    text(d,745,170,'Shared focus / break state',11)
    box(d,630,95,108,45,['Pause / resume']);box(d,750,95,110,45,['Stop'])
    text(d,450,22,'Conceptual wireframes. These are interaction designs, not implementation or test evidence.',10)
    export(d,ROOT/'docs/prototype/flows')

    d=Drawing(900,470)
    text(d,450,440,'ASTI Android companion: device onboarding',19,bold=True)
    for i,h in enumerate(['Device ownership','Connectivity','External services']):
        x=20+i*295
        d.add(Rect(x,55,270,350,fillColor=colors.white,strokeColor=LINE,strokeWidth=1))
        text(d,x+135,374,h,15,bold=True)
        text(d,x+135,351,'Android companion',11)
        d.add(Line(x+20,333,x+250,333,strokeColor=LINE))
    box(d,40,243,230,65,['Identify device','Confirm ownership'])
    box(d,40,153,230,65,['Pairing status','Authorize / cancel'])
    text(d,155,100,'Account-bound device access',11)
    box(d,335,243,230,65,['Connection method','BLE / Wi-Fi feasibility pending'])
    box(d,335,153,230,65,['Connection state','Retry / continue'])
    text(d,450,100,'Explain failure and recovery',11)
    box(d,630,243,230,65,['Authorize Google Calendar','Select Notion data source'])
    box(d,630,153,230,65,['Device: online / last seen','Source freshness / errors'])
    text(d,745,100,'Open assistant / manage access',11)
    text(d,450,22,'Conceptual flow. Pairing transport and exact discovery mechanism require real-device validation.',10)
    export(d,ROOT/'docs/prototype/setup')


styles={
    'Body':ParagraphStyle('Body',fontName='TimesNewRoman',fontSize=14,leading=21,spaceAfter=10,textColor=colors.black,splitLongWords=True,allowWidows=0,allowOrphans=0),
    'H1':ParagraphStyle('H1',fontName='TimesNewRoman-Bold',fontSize=14,leading=21,spaceBefore=14,spaceAfter=14,keepWithNext=True,textColor=colors.black),
    'H2':ParagraphStyle('H2',fontName='TimesNewRoman-Bold',fontSize=14,leading=21,spaceBefore=12,spaceAfter=8,keepWithNext=True,textColor=colors.black),
    'Cell':ParagraphStyle('Cell',fontName='TimesNewRoman',fontSize=14,leading=17,spaceAfter=0,textColor=colors.black,splitLongWords=True,allowWidows=0,allowOrphans=0),
    'HeadCell':ParagraphStyle('HeadCell',fontName='TimesNewRoman-Bold',fontSize=14,leading=17,textColor=colors.black,splitLongWords=True,allowWidows=0,allowOrphans=0),
    'Caption':ParagraphStyle('Caption',fontName='TimesNewRoman',fontSize=14,leading=21,spaceAfter=12,textColor=colors.black),
    'Cover':ParagraphStyle('Cover',fontName='TimesNewRoman-Bold',fontSize=14,leading=21,spaceAfter=20,textColor=colors.black),
    'Subtitle':ParagraphStyle('Subtitle',fontName='TimesNewRoman',fontSize=14,leading=21,spaceAfter=23,textColor=colors.black),
}

def rich(s):
    s=html.escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'\1',s)
    s=re.sub(r'(https?://[^\s]+)',lambda m:'<link href="'+m[0].rstrip('.,')+'" color="#0000FF">'+m[0].rstrip('.,')+'</link>'+m[0][len(m[0].rstrip('.,')):],s)
    return s

class ReportDoc(BaseDocTemplate):
    def __init__(self,path):
        super().__init__(str(path),pagesize=A4,leftMargin=54,rightMargin=54,topMargin=55,bottomMargin=49,title='ASTI First Probationary Period Report',author='Yan Kudashov')
        self.addPageTemplates(PageTemplate('normal',[Frame(self.leftMargin,self.bottomMargin,self.width,self.height,id='body')],onPage=self.page_frame))
    def page_frame(self,c,doc):
        c.saveState();c.setFont('TimesNewRoman',14);c.setFillColor(colors.black)
        c.drawRightString(A4[0]-54,27,str(doc.page));c.restoreState()
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name=='H1':
            title=f.getPlainText();key='section-'+str(self.seq.nextf('heading'))
            self.canv.bookmarkPage(key);self.canv.addOutlineEntry(title,key,0)
            self.notify('TOCEntry',(0,title,self.page,key))

def build_report():
    out=ROOT/'output/pdf/ASTI_Supervisor_Review.pdf';out.parent.mkdir(parents=True,exist_ok=True)
    story=[Spacer(1,68),Paragraph('ASTI',styles['Cover']),Paragraph('First Probationary Period Report',styles['Subtitle']),
        Paragraph('Development of an Intelligent System for a Physical Desktop Assistant with a Mobile Application and External Service Integration',styles['Subtitle']),
        Paragraph('Yan Kudashov | SE-2413',styles['Body']),
        Paragraph('Supervisor: Сарсенова Жибек Нуржановна',styles['Body']),
        Paragraph('Astana IT University<br/>Software Engineering<br/>24 October 2026',styles['Body']),
        Spacer(1,18),Paragraph(rich('Repository: https://github.com/Kreichik/asti'),styles['Body']),
        Paragraph(rich('YouTrack: https://asti-diploma.youtrack.cloud/agiles/204-1/current'),styles['Body']),PageBreak(),
        Paragraph('Contents',styles['H2'])]
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName='TimesNewRoman',fontSize=14,leading=23,leftIndent=0,firstLineIndent=0,rightIndent=25)]
    story+=[toc,PageBreak()]
    lines=(ROOT/'docs/report.md').read_text(encoding='utf-8').splitlines()
    i=next(i for i,s in enumerate(lines) if s.startswith('## 1 '))
    first=True
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('## '):
            if not first:story.extend([Spacer(1,15),CondPageBreak(170)])
            first=False;story.append(Paragraph(rich(line[3:]),styles['H1']));i+=1;continue
        if line.startswith('### '):story.extend([CondPageBreak(85),Paragraph(rich(line[4:]),styles['H2'])]);i+=1;continue
        if line.startswith('!['):
            m=re.match(r'!\[(.*?)\]\((.*?)\)',line);p=ROOT/'docs'/m[2]
            from PIL import Image as PILImage
            with PILImage.open(p) as im:w,h=im.size
            width=487; story.append(KeepTogether([Image(str(p),width=width,height=width*h/w),Paragraph(m[1],styles['Caption'])]));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[s.strip() for s in lines[i].strip().strip('|').split('|')]
                if not all(re.match(r'^:?-+:?$',s) for s in cells):rows.append(cells)
                i+=1
            n=len(rows[0]);widths={3:[62,65,360],4:[92,132,132,131],5:[84,101,101,101,100]}.get(n,[487/n]*n)
            # Narrative comparison tables receive more width in their descriptive columns.
            if n==3 and len(rows[0])>0 and rows[0][0] in ['Participants','Area','Milestone','Risk']:widths=[95,196,196]
            if n==3 and rows[0][0]=='Alternative':widths=[100,200,187]
            data=[[Paragraph(rich(c),styles['HeadCell'] if r==0 else styles['Cell']) for c in row] for r,row in enumerate(rows)]
            t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.white),('GRID',(0,0),(-1,-1),.5,colors.black),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
            story.extend([t,Spacer(1,12)]);continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','![')):
            para.append(lines[i].strip());i+=1
        story.append(Paragraph(rich(' '.join(para)),styles['Body']))
    ReportDoc(out).multiBuild(story)
    return out

if __name__=='__main__':
    diagrams();out=build_report()
    qa=ROOT/'tmp/pdfs/report-formatted';qa.mkdir(parents=True,exist_ok=True)
    pdf=pdfium.PdfDocument(str(out))
    for i in range(len(pdf)):
        pdf[i].render(scale=1.3).to_pil().save(qa/f'page-{i+1}.png')
    print(f'Built {out}; pages={len(pdf)}; bytes={out.stat().st_size}')
    pdf.close()

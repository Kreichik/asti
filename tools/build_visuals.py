"""Export ASTI architecture diagrams and application wireframes."""
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
    d=Drawing(900,500)
    text(d,450,470,'ASTI system context',18,bold=True)
    box(d,20,215,150,70,['User'])
    box(d,290,170,260,160,['ASTI platform','Backend API','Android and web applications','Integrations and shared state'])
    box(d,710,350,170,60,['Google Calendar','External events'])
    box(d,710,260,170,60,['Notion','External task source'])
    box(d,710,170,170,60,['Model provider'])
    box(d,710,50,170,70,['Compatible device','External API client'])
    arrow(d,170,265,290,265,'Application actions',230,283)
    arrow(d,290,225,170,225,'Views and settings',230,205)
    arrow(d,550,300,710,380);arrow(d,550,270,710,290)
    arrow(d,550,230,710,200);arrow(d,550,190,710,100,'Authorized messages',635,122)
    text(d,450,20,'The platform boundary excludes device hardware and firmware.',11)
    export(d,ROOT/'docs/diagrams/context')

    d=Drawing(900,600)
    text(d,450,570,'ASTI component architecture',18,bold=True)
    box(d,25,460,220,60,['Flutter Android application'])
    box(d,295,460,220,60,['Flutter web application'])
    box(d,650,460,220,60,['External physical client'])
    box(d,150,345,300,65,['Backend application API','Accounts / integrations / device settings'])
    box(d,605,345,250,65,['Device connection API','Authentication / messages / commands'])
    arrow(d,135,460,250,410);arrow(d,405,460,350,410);arrow(d,760,460,730,410)
    box(d,200,230,500,65,['Domain services','Overview / reminders / focus / connection state'])
    arrow(d,300,345,350,295);arrow(d,730,345,620,295)
    box(d,20,100,255,70,['Integration workers','Calendar / Notion adapters'])
    box(d,335,100,230,70,['PostgreSQL','Accounts / source data / shared state'])
    box(d,625,100,255,70,['Briefing service','Model adapter / fallback'])
    arrow(d,365,230,200,170);arrow(d,450,230,450,170);arrow(d,580,230,745,170)
    arrow(d,275,135,335,135)
    text(d,450,32,'External clients use the connection API; firmware is outside the platform.',11)
    export(d,ROOT/'docs/diagrams/components')

    d=Drawing(900,650)
    text(d,450,620,'ASTI use cases',18,bold=True)
    d.add(Rect(200,45,450,535,fillColor=colors.white,strokeColor=LINE))
    text(d,425,555,'ASTI platform',13,bold=True)
    d.add(Circle(65,330,13,fillColor=None,strokeColor=INK));d.add(Line(65,317,65,279,strokeColor=INK))
    for xy in [(35,303,95,303),(65,279,40,254),(65,279,90,254)]:d.add(Line(*xy,strokeColor=INK))
    text(d,65,235,'User',12)
    names=['Access account','Connect or disconnect services','View overview and reminders','Acknowledge or snooze reminder','Control focus session','Associate or revoke a device','Configure preferences','Synchronize external source','Exchange authorized client state']
    for i,name in enumerate(names):
        y=510-i*49;d.add(Ellipse(425,y,195,19,fillColor=colors.white,strokeColor=LINE));text(d,425,y-4,name,12)
        if i<7:d.add(Line(95,303,230,y,strokeColor=LINE,strokeWidth=.7))
    box(d,705,115,175,65,['External services'])
    box(d,705,30,175,65,['Compatible device'])
    d.add(Line(620,167,705,147,strokeColor=LINE));d.add(Line(620,118,705,64,strokeColor=LINE))
    export(d,ROOT/'docs/diagrams/use-cases')

    d=Drawing(1000,690)
    text(d,500,660,'ASTI Android application',20,bold=True)
    for i,title in enumerate(['Overview','Integrations','Devices']):
        x=20+i*330
        d.add(Rect(x,65,300,550,fillColor=colors.white,strokeColor=LINE,strokeWidth=1.2))
        text(d,x+150,588,'ASTI',18,bold=True);text(d,x+150,556,title,15,bold=True)
        d.add(Line(x+15,535,x+285,535,strokeColor=LINE))
        d.add(Line(x+15,112,x+285,112,strokeColor=LINE))
        text(d,x+150,91,'Overview   Integrations   Devices',11)
    box(d,40,432,260,75,['Upcoming commitments','Event title / time / source'])
    box(d,40,325,260,80,['Active reminders','View details / snooze / acknowledge'])
    box(d,40,210,260,80,['Focus session','Start / pause / stop'])
    text(d,170,155,'Last synchronized / refresh',12)
    box(d,370,432,260,75,['Google Calendar','Connected / choose calendars'])
    box(d,370,325,260,80,['Notion','Connect / select task source'])
    box(d,370,210,260,80,['Connection details','Last sync / retry / disconnect'])
    text(d,500,155,'Available services',12)
    box(d,700,432,260,75,['Connected device','Name / online status / last activity'])
    box(d,700,325,260,80,['Add device','Identify / associate with account'])
    box(d,700,210,260,80,['Access settings','Inspect connection / revoke'])
    text(d,830,155,'Manage account access',12)
    text(d,500,24,'Mobile navigation, integration management and external-device access',12)
    export(d,ROOT/'docs/prototype/mobile')

    d=Drawing(1100,650)
    text(d,550,620,'ASTI web application',20,bold=True)
    d.add(Rect(15,45,1070,530,fillColor=colors.white,strokeColor=LINE))
    d.add(Line(15,520,1085,520,strokeColor=LINE));d.add(Line(205,45,205,520,strokeColor=LINE))
    text(d,65,545,'ASTI',18,bold=True);text(d,975,545,'Account / settings',12)
    for i,label in enumerate(['Overview','Integrations','Devices','Reminders','Focus','Settings']):
        text(d,110,475-i*49,label,14,bold=label=='Integrations')
    text(d,250,480,'Integrations',18,anchor='start',bold=True)
    text(d,250,450,'Connect services and manage the data available to your assistant',12,anchor='start')
    box(d,235,295,360,120,['Google Calendar','Connected','Select calendars / synchronize / disconnect'])
    box(d,625,295,420,120,['Notion','Not connected','Connect and select an authorized task source'])
    d.add(Rect(235,80,810,180,fillColor=colors.white,strokeColor=LINE))
    text(d,260,232,'Connection settings',15,anchor='start',bold=True)
    for i,label in enumerate(['Selected source: authorized calendar or task database','Synchronization: last result and timestamp','Data mapping: title / due date / status','Actions: save settings / synchronize now / revoke access']):
        text(d,260,199-i*30,label,12,anchor='start')
    text(d,550,20,'The web client uses the same account, integrations and API as Android.',12)
    export(d,ROOT/'docs/prototype/web')


if __name__=='__main__':
    diagrams()
    print('Exported architecture diagrams and application wireframes.')

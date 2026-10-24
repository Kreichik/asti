$reportRoot = Split-Path -Parent $PSScriptRoot
$sourceDocx = Join-Path $reportRoot 'output\docx\SE-2413_Kudashov_ProbPeriod1.docx'
$targetPdf = Join-Path $reportRoot 'output\pdf\SE-2413_Kudashov_ProbPeriod1.pdf'
$wordApp = $null
$wordDoc = $null
try {
    $wordApp = New-Object -ComObject Word.Application
    $wordApp.Visible = $false
    $wordApp.DisplayAlerts = 0
    $wordDoc = $wordApp.Documents.Open($sourceDocx, $false, $false)
    $wordDoc.Fields.Update() | Out-Null
    foreach ($reportToc in $wordDoc.TablesOfContents) { $reportToc.Update() }
    $wordDoc.Content.Font.Name = 'Times New Roman'
    $wordDoc.Content.Font.Size = 14
    $wordDoc.Content.Font.Color = 0
    foreach ($reportLink in $wordDoc.Hyperlinks) {
        $reportLink.Range.Font.Color = 16711680
        $reportLink.Range.Font.Underline = 1
    }
    foreach ($reportTable in $wordDoc.Tables) {
        $reportTable.Style = -155
        $reportTable.ApplyStyleHeadingRows = $false
        $reportTable.ApplyStyleRowBands = $false
        $reportTable.ApplyStyleColumnBands = $false
        $reportTable.Borders.Enable = 1
        $reportTable.Borders.InsideLineStyle = 1
        $reportTable.Borders.OutsideLineStyle = 1
        $reportTable.Borders.InsideLineWidth = 4
        $reportTable.Borders.OutsideLineWidth = 4
        $reportTable.Borders.InsideColor = 0
        $reportTable.Borders.OutsideColor = 0
        $reportTable.Rows.AllowBreakAcrossPages = $false
        $reportTable.Rows.Item(1).HeadingFormat = -1
        $reportTable.Rows.HeightRule = 0
        $reportTable.TopPadding = 6
        $reportTable.BottomPadding = 6
        $reportTable.LeftPadding = 6
        $reportTable.RightPadding = 6
        $reportTable.Range.ParagraphFormat.SpaceAfter = 0
        $reportTable.Range.ParagraphFormat.KeepWithNext = 0

    }
    $wordDoc.Repaginate()
    foreach ($reportToc in $wordDoc.TablesOfContents) { $reportToc.UpdatePageNumbers() }
    $wordDoc.Save()
    $wordDoc.ExportAsFixedFormat($targetPdf, 17)
    Write-Output ('Exported report PDF. Pages: ' + $wordDoc.ComputeStatistics(2))
} finally {
    if ($null -ne $wordDoc) { $wordDoc.Close(0) }
    if ($null -ne $wordApp) { $wordApp.Quit() }
}

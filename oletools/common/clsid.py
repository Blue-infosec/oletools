"""
clsid.py

Collection of known CLSIDs and related vulnerabilities, for the oletools.

Author: Philippe Lagadec - http://www.decalage.info
License: BSD, see source code or documentation

clsid is part of the python-oletools package:
http://www.decalage.info/python/oletools
"""

#=== LICENSE ==================================================================

# oletools are copyright (c) 2018 Philippe Lagadec (http://www.decalage.info)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#------------------------------------------------------------------------------
# CHANGELOG:
# 2018-04-11 v0.53 PL: - added collection of CLSIDs
# 2018-04-13       PL: - moved KNOWN_CLSIDS from oledir to common.clsid
#                  SQ: - several additions by Shiao Qu
# 2018-04-18       PL: - added known-bad CLSIDs from Cuckoo sandbox (issue #290)
# 2018-05-08       PL: - added more CLSIDs (issues #299, #304), merged and sorted

__version__ = '0.53dev9'


# REFERENCES:

# Known-bad CLSIDs from Cuckoo Sandbox:
# https://github.com/cuckoosandbox/community/blob/master/modules/signatures/windows/office.py#L314

# https://justhaifei1.blogspot.nl/2017/07/bypassing-microsofts-cve-2017-0199-patch.html
# https://github.com/nccgroup/yaml2yara/blob/master/sample_data/office_exploits/ole.yaml


KNOWN_CLSIDS = {
    '00000300-0000-0000-C000-000000000046': 'StdOleLink (embedded OLE object - Known Related to CVE-2017-0199, CVE-2017-8570 or CVE-2017-8759)',
    '00000303-0000-0000-C000-000000000046': 'File Moniker (may trigger CVE-2017-0199 or CVE-2017-8570)',
    '00000304-0000-0000-C000-000000000046': 'Item Moniker',
    '00000305-0000-0000-C000-000000000046': 'Anti Moniker',
    '00000306-0000-0000-C000-000000000046': 'Pointer Moniker',
    '00000308-0000-0000-C000-000000000046': 'Packager Moniker',
    '00000309-0000-0000-C000-000000000046': 'Composite Moniker (may trigger CVE-2017-8570)',
    '0000031a-0000-0000-C000-000000000046': 'Class Moniker',
    '00000535-0000-0010-8000-00AA006D2EA4': 'ADODB.RecordSet (may trigger CVE-2015-0097)',
    '0002034c-0000-0000-C000-000000000046': 'OutlookAttachMoniker',
    '0002034e-0000-0000-C000-000000000046': 'OutlookMessageMoniker',
    '00020810-0000-0000-C000-000000000046': 'Microsoft Excel.Sheet.5',
    '00020811-0000-0000-C000-000000000046': 'Microsoft Excel.Chart.5',
    '00020820-0000-0000-C000-000000000046': 'Microsoft Microsoft Excel 97-2003 Worksheet (Excel.Sheet.8)',
    '00020821-0000-0000-C000-000000000046': 'Microsoft Excel.Chart.8',
    '00020830-0000-0000-C000-000000000046': 'Microsoft Excel.Sheet.12',
    '00020832-0000-0000-C000-000000000046': 'Microsoft Excel sheet with macro enabled (Excel.SheetMacroEnabled.12)',
    '00020833-0000-0000-C000-000000000046': 'Microsoft Excel binary sheet with macro enabled (Excel.SheetBinaryMacroEnabled.12)',
    '00020900-0000-0000-C000-000000000046': 'Microsoft Word 6.0-7.0 Document (Word.Document.6)',
    '00020906-0000-0000-C000-000000000046': 'Microsoft Word 97-2003 Document (Word.Document.8)',
    '00021700-0000-0000-C000-000000000046': 'Microsoft Equation 2.0 (Known Related to CVE-2017-11882 or CVE-2018-0802)',
    '0002CE02-0000-0000-C000-000000000046': 'Microsoft Equation 3.0 (Known Related to CVE-2017-11882 or CVE-2018-0802)',
    '0002CE03-0000-0000-C000-000000000046': 'MathType Equation Object',
    '0003000C-0000-0000-C000-000000000046': 'OLE Package Object (may contain and run any file)',
    '048EB43E-2059-422F-95E0-557DA96038AF': 'Microsoft Powerpoint.Slide.12',
    '05741520-C4EB-440A-AC3F-9643BBC9F847': 'otkloadr.WRLoader (can be used to bypass ASLR after triggering an exploit)',
    '06290BD2-48AA-11D2-8432-006008C3FBFC': 'Factory bindable using IPersistMoniker (scripletfile)',
    '06290BD3-48AA-11D2-8432-006008C3FBFC': 'Script Moniker, aka Moniker to a Windows Script Component (may trigger CVE-2017-0199)',
    '0CF774D0-F077-11D1-B1BC-00C04F86C324': 'scrrun.dll - HTML File Host Encode Object (ProgID: HTML.HostEncode)',
    '0D43FE01-F093-11CF-8940-00A0C9054228': 'scrrun.dll - FileSystem Object (ProgID: Scripting.FileSystemObject)',
    '0E59F1D5-1FBE-11D0-8FF2-00A0D10038BC': 'MSScriptControl.ScriptControl (may trigger CVE-2015-0097)',
    '1EFB6596-857C-11D1-B16A-00C0F0283628': 'MSCOMCTL.TabStrip (may trigger CVE-2012-1856, CVE-2013-3906 - often used for heap spray)',
    '3050F4D8-98B5-11CF-BB82-00AA00BDCE0B': 'HTML Application (may trigger CVE-2017-0199)',
    '44F9A03B-A3EC-4F3B-9364-08E0007F21DF': 'Control.TaskSymbol (may trigger CVE-2015-2424)',
    '46E31370-3F7A-11CE-BED6-00AA00611080': 'Forms.MultiPage',
    '4C599241-6926-101B-9992-00000B65C6F9': 'Forms.Image (may trigger CVE-2015-2424)',
    '4D3263E4-CAB7-11D2-802A-0080C703929C': 'AutoCAD 2000-2002 Document',
    '5E4405B0-5374-11CE-8E71-0020AF04B1D7': 'AutoCAD R14 Document',
    '64818D10-4F9B-11CF-86EA-00AA00B929E8': 'Microsoft Powerpoint.Show.8',
    '64818D11-4F9B-11CF-86EA-00AA00B929E8': 'Microsoft Powerpoint.Slide.8',
    '66833FE6-8583-11D1-B16A-00C0F0283628': 'MSCOMCTL.Toolbar (may trigger CVE-2012-1856)',
    '6A221957-2D85-42A7-8E19-BE33950D1DEB': 'AutoCAD 2013 Document',
    '6E182020-F460-11CE-9BCD-00AA00608E01': 'Forms.Frame',
    '79EAC9E0-BAF9-11CE-8C82-00AA004BA90B': 'URL Moniker (may trigger CVE-2017-0199 or CVE-2017-8570)',
    '7AABBB95-79BE-4C0F-8024-EB6AF271231C': 'AutoCAD 2007-2009 Document',
    '85131630-480C-11D2-B1F9-00C04F86C324': 'scrrun.dll - JS File Host Encode Object (ProgID: JSFile.HostEncode)',
    '85131631-480C-11D2-B1F9-00C04F86C324': 'scrrun.dll - VBS File Host Encode Object (ProgID: VBSFile.HostEncode)',
    '8E75D913-3D21-11D2-85C4-080009A0C626': 'AutoCAD 2004-2006 Document',
    '9181DC5F-E07D-418A-ACA6-8EEA1ECB8E9E': 'MSCOMCTL.TreeCtrl (may trigger CVE-2012-0158)',
    '996BF5E0-8044-4650-ADEB-0B013914E99C': 'MSCOMCTL.ListViewCtrl (may trigger CVE-2012-0158)',
    'A08A033D-1A75-4AB6-A166-EAD02F547959': 'otkloadr WRAssembly Object (can be used to bypass ASLR after triggering an exploit)',
    'B54F3741-5B07-11CF-A4B0-00AA004A55E8': 'vbscript.dll - VB Script Language (ProgID: VBS, VBScript)',
    'BDD1F04B-858B-11D1-B16A-00C0F0283628': 'MSCOMCTL.ListViewCtrl (may trigger CVE-2012-0158)',
    'C62A69F0-16DC-11CE-9E98-00AA00574A4F': 'Forms.Form',
    'C74190B6-8589-11d1-B16A-00C0F0283628': 'MSCOMCTL.TreeCtrl (may trigger CVE-2012-0158)',
    'C74190B6-8589-11D1-B16A-00C0F0283628': 'MSCOMCTL.TreeCtrl',
    'CF4F55F4-8F87-4D47-80BB-5808164BB3F8': 'Microsoft Powerpoint.Show.12',
    'D27CDB6E-AE6D-11CF-96B8-444553540000': 'Shockwave Flash Object (may trigger many CVEs)',
    'D7053240-CE69-11CD-A777-00DD01143C57': 'Microsoft Forms 2.0 CommandButton',
    'D70E31AD-2614-49F2-B0FC-ACA781D81F3E': 'AutoCAD 2010-2012 Document',
    'DD9DA666-8594-11D1-B16A-00C0F0283628': 'MSCOMCTL.ImageComboCtrl (may trigger CVE-2014-1761)',
    'E5CA59F5-57C4-4DD8-9BD6-1DEEEDD27AF4': 'InkEd.InkEdit',
    'ECABAFC6-7F19-11D2-978E-0000F8757E2A': 'New Moniker',
    'ECABB0C7-7F19-11D2-978E-0000F8757E2A': 'SOAP Moniker (may trigger CVE-2017-8759)',
    'F20DA720-C02F-11CE-927B-0800095AE340': 'OLE Package Object (may contain and run any file)',
    'F414C260-6AC0-11CF-B6D1-00AA00BBBB58': 'jscript.dll - JScript Language (ProgID: ECMAScript, JavaScript, JScript, LiveScript)',
    'F4754C9B-64F5-4B40-8AF4-679732AC0607': 'Microsoft Word Document (Word.Document.12)',
    '1461A561-24E8-4BA3-8D4A-FFEEF980556B': 'BCSAddin.Connect (potential exploit CVE-2016-0042 / MS16-014)',
    '6AD4AE40-2FF1-4D88-B27A-F76FC7B40440': 'BCSAddin.ManageSolutionHelper (potential exploit CVE-2016-0042 / MS16-014)',
    'e8cc4cbe-fdff-11d0-b865-00a0c9081c1d': 'MSDAORA.1 (potential exploit CVE TODO)', # TODO
    '23CE100B-1390-49D6-BA00-F17D3AEE149C': 'UmOutlookAddin.UmEvmCtrl (potential exploit document CVE-2016-0042 / MS16-014)',
    '8627E73B-B5AA-4643-A3B0-570EDA17E3E7': 'UmOutlookAddin.ButtonBar (potential exploit document CVE-2016-0042 / MS16-014)',
    'F959DBBB-3867-41F2-8E5F-3B8BEFAA81B3': 'UmOutlookAddin.FormRegionAddin (potential exploit document CVE-2016-0042 / MS16-014)',
    'ECF44975-786E-462F-B02A-CBCCB1A2C4A2': 'UmOutlookAddin.FormRegionContext (potential exploit document CVE-2016-0042 / MS16-014)',
    'CDF1C8AA-2D25-43C7-8AFE-01F73A3C66DA': 'UmOutlookAddin.InspectorContext (potential exploit document CVE-2016-0042 / MS16-014)',
    'D50FED35-0A08-4B17-B3E0-A8DD0EDE375D': 'UmOutlookAddin.PlayOnPhoneDlg (potential exploit document CVE-2016-0042 / MS16-014)',
    'CCD068CD-1260-4AEA-B040-A87974EB3AEF': 'UmOutlookAddin.RoomsCTP (potential exploit document CVE-2016-0042 / MS16-014)',
    '41B9BE05-B3AF-460C-BF0B-2CDD44A093B1': 'Search.XmlContentFilter (potential exploit document CVE TODO)',
    '3018609E-CDBC-47E8-A255-809D46BAA319': 'SSCE DropTable Listener Object (can be used to bypass ASLR after triggering an exploit)',
}


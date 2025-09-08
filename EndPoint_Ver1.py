import os
import subprocess
import sys

# --- Optional library installs ---
try:
    import wx
    import wx.richtext as rt
except ImportError:
    print("ERROR: wxPython not found!")
    sys.exit(1)

try:
    from mcstatus import JavaServer
except ImportError:
    print("ERROR: mcstatus not found!")
    sys.exit(1)

# --- Redirect GTK errors ---
import io
sys.stderr = io.StringIO()

# --- MOTD default color (grey) ---
MOTD_COLOR = wx.Colour(170, 170, 170)

# --- Event handler ---
def OnSubmit(event):
    user_input = text_box.GetValue().strip()
    if not user_input:
        return

    failed.SetLabel("")
    text_motd.Clear()
    text_version.SetLabel("Fetching...")

    try:
        server = JavaServer.lookup(user_input)
        status = server.status()

        # MOTD
        for part in status.motd.parsed:
            if isinstance(part, str):
                attr = rt.RichTextAttr()
                attr.SetTextColour(MOTD_COLOR)
                attr.SetAlignment(wx.TEXT_ALIGNMENT_LEFT)
                text_motd.BeginStyle(attr)
                text_motd.WriteText(part)
                text_motd.EndStyle()

        # Version
        text_version.SetLabel(f"{status.version.name} (Protocol {status.version.protocol})")

        # Response time
        #try:
            #latency = server.latency()
            #text_response.SetLabel(f"{latency:.2f} ms")
        #except:
            #text_response.SetLabel("Ping failed")

    except Exception as e:
        text_motd.Clear()
        text_version.SetLabel("Unknown")
        #text_response.SetLabel("Ping failed")
        #if "Name or service not known" in str(e):
            #failed.SetLabel("Invalid server address")
        #else:
            #failed.SetLabel(str(e))

# --- GUI Setup ---
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "EndPoint", size=(700, 500))

# Icon (optional)
if os.path.exists("EndPoint.png"):
    bitmap = wx.Bitmap("EndPoint.png", wx.BITMAP_TYPE_PNG)
    icon = wx.Icon()
    icon.CopyFromBitmap(bitmap)
    frame.SetIcon(icon)

notebook = wx.Notebook(frame)

# --- Panel 1: Input ---
panel_input = wx.Panel(notebook)
sizer_input = wx.BoxSizer(wx.VERTICAL)
wx.StaticText(panel_input, label="Input server address:")
text_box = wx.TextCtrl(panel_input, size=(400, 25))
submit_button = wx.Button(panel_input, label="Submit")
submit_button.Bind(wx.EVT_BUTTON, OnSubmit)
failed = wx.StaticText(panel_input, label="")
sizer_input.Add(text_box, 0, wx.ALL, 25)
sizer_input.Add(submit_button, 0, wx.ALL, 10)
sizer_input.Add(failed, 0, wx.ALL, 10)
panel_input.SetSizer(sizer_input)
notebook.AddPage(panel_input, "Input Server")

# --- Panel 2: MOTD ---
panel_motd = wx.Panel(notebook)
sizer_motd = wx.BoxSizer(wx.VERTICAL)
text_motd = rt.RichTextCtrl(panel_motd, style=wx.TE_MULTILINE | wx.TE_READONLY)
text_motd.SetValue("MOTD will appear here")
sizer_motd.Add(text_motd, 1, wx.EXPAND | wx.ALL, 10)
panel_motd.SetSizer(sizer_motd)
notebook.AddPage(panel_motd, "MOTD (Parsed)")

# --- Panel 3: Version ---
panel_version = wx.Panel(notebook)
sizer_version = wx.BoxSizer(wx.VERTICAL)
text_version = wx.StaticText(panel_version, label="Version will appear here")
sizer_version.Add(text_version, 0, wx.ALL, 10)
panel_version.SetSizer(sizer_version)
notebook.AddPage(panel_version, "Version")

# --- Panel 4: Response Time --- Kinda broken, will fix in v2!
#panel_response = wx.Panel(notebook)
#sizer_response = wx.BoxSizer(wx.VERTICAL)
#text_response = wx.StaticText(panel_response, label="Response time will appear here")
#sizer_response.Add(text_response, 0, wx.ALL, 10)
#panel_response.SetSizer(sizer_response)
#notebook.AddPage(panel_response, "Response Time")

# --- Panel 5: Credits ---
panel_credits = wx.Panel(notebook)
sizer_credits = wx.BoxSizer(wx.VERTICAL)
sizer_credits.Add(wx.StaticText(panel_credits, label="Libraries:"), 0, wx.ALL, 10)
sizer_credits.Add(wx.StaticText(panel_credits, label="mcstatus - Fetch server data"), 0, wx.ALL, 10)
sizer_credits.Add(wx.StaticText(panel_credits, label="wxPython - GUI library"), 0, wx.ALL, 10)
panel_credits.SetSizer(sizer_credits)
notebook.AddPage(panel_credits, "Credits")


frame.Show()
app.MainLoop()

import ROOT as root
import math

# Determine the path to the ROOT file 
Input = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
RecoMC_hist = Input.Get("mass/signal;1")

hist = Input.Get("mass/signal_sys_TRIG__1down")
hist2 = Input.Get("mass/signal_sys_TRIG__1up")

bin_contents = []
bin2_contents = []

for bin in range(1, hist.GetNbinsX() + 1):
    content = hist.GetBinContent(bin)
    bin_contents.append(content)

for bin in range(1, hist2.GetNbinsX() + 1):
    content2 = hist2.GetBinContent(bin)
    bin2_contents.append(content2)

s = 0

s1 = 0

for b in range(1, hist.GetNbinsX() + 1):
    for B in range(1, hist.GetNbinsX() + 1):
        s += bin_contents[b-1]*bin_contents[B-1]
        print (s)

for b in range(1, hist2.GetNbinsX() + 1):
    for B in range(1, hist2.GetNbinsX() + 1):
        s1 += bin2_contents[b-1]*bin2_contents[B-1]

down = math.sqrt(s) * 100 / hist.GetNbinsX()

up = math.sqrt(s1) * 100 / hist2.GetNbinsX()

trigger = ( down + up ) / 2

print (down, up, trigger)









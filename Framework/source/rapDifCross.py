import ROOT as root
import math

# Determine the path to the ROOT files
Inputs = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")

# Define the histograms for the Data and the backgrounds for rapidity
Data_hist= Inputs.Get("rapidity/data;1") #Data Histogram
Sig_hist = Inputs.Get("rapidity/signal;1") #LbyL Signal Histogram
eeBkg_hist = Inputs.Get("rapidity/ee;1") #QED Background Histogram
CEPbkg_hist = Inputs.Get("rapidity/cep;1") #CEP Background Histogram

Lint = 2.22                           # Integrated luminosity

Data_hist_contents = []
eeBkg_hist_contents = []
CEPbkg_hist_contents = []
Signal_hist_contents = []
StatUnc_contents =[]
BW_contents = []
diffid_contents = ["74.226", "81.146", "22.697", "19.574"]
MCcross_contents = []
        
# Define the function that calculates the fiducial cross section with details
def rapDifCross():

    for bin in range(0, Data_hist.GetNbinsX()-4):

        print ("Differential cross section for diphoton rapidity[", bin + 1 ,"]:", diffid_contents[bin])
    
    return diffid_contents


def statUncData():
    print("---------------Relative systematic uncertainties bin by bin:--------------------")

    for bin in range(0, Data_hist.GetNbinsX()-4):
        content = Data_hist.GetBinContent(4-bin)+Data_hist.GetBinContent(bin+5)
        Data_hist_contents.append(content)

        content2 = eeBkg_hist.GetBinContent(4-bin) +  eeBkg_hist.GetBinContent(bin+5)
        eeBkg_hist_contents.append(content2)
            
        content3 = CEPbkg_hist.GetBinContent(4-bin) + CEPbkg_hist.GetBinContent(bin+5)
        CEPbkg_hist_contents.append(content3)

        StatUnc = math.sqrt(content)/(content - content2 - content3)
        StatUnc_contents.append("%.4f" % StatUnc)

        print ("Statistical uncertainty on Data[", bin + 1 ,"]:", "%.4f" % StatUnc)


    return StatUnc_contents

def MCcross():

    for bin in range(0, Data_hist.GetNbinsX()-4):
        BW = Data_hist.GetBinWidth(bin+1)
        BW_contents.append(BW)
        print(BW)
        content = (Sig_hist.GetBinContent(4-bin) + Sig_hist.GetBinContent(bin+5))
        MCcross = content/(BW*Lint)
        MCcross_contents.append(MCcross)
        print(MCcross)

    return MCcross_contents

def MCunc():

    print ("----------------------------")
    bin2_contents = []
    MCstat_content = []

    for bin in range(0, Data_hist.GetNbinsX()-4):
        content3 = math.sqrt(Sig_hist.GetBinError(4-bin)**2+Sig_hist.GetBinError(bin+5)**2)
        bin2_contents.append(content3)
    
        MCstat = content3 / (Sig_hist.GetBinContent(4-bin)+Sig_hist.GetBinContent(bin+5))
        print(Sig_hist.GetBinContent(4-bin)+Sig_hist.GetBinContent(bin+5))
        MCstat_content.append("%.4f" % MCstat)

        print("Statistical uncertainty on MC[", bin + 1 ,"]:", "%.4f" % MCstat)

    return MCstat_content
'''
rapDifCross()
statUncData()
MCcross()
MCunc()
'''




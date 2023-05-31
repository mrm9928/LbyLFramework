import ROOT as root
import math

# Determine the path to the ROOT files
Inputs = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")

# Define the histograms for the Data and the backgrounds for rapidity
Data_hist= Inputs.Get("cos_theta_star/data;1") #Data Histogram
Sig_hist = Inputs.Get("cos_theta_star/signal;1") #LbyL Signal Histogram
eeBkg_hist = Inputs.Get("cos_theta_star/ee;1") #QED Background Histogram
CEPbkg_hist = Inputs.Get("cos_theta_star/cep;1") #CEP Background Histogram

Lint = 2.22                           # Integrated luminosity

Data_hist_contents = []
eeBkg_hist_contents = []
CEPbkg_hist_contents = []
Signal_hist_contents = []
StatUnc_contents =[]
BW_contents = []
diffid_contents = ["200.875", "120.153", "81.903", "81.764"]
MCcross_contents = []
        
# Define the function that calculates the fiducial cross section with details
def cosDifCross():

    for bin in range(0, 4):

        print ("Differential cross section for diphoton |cos(\\theta*)|[", bin + 1 ,"]:", diffid_contents[bin])
    
    return diffid_contents


def statUncData():
    print("---------------Relative systematic uncertainties bin by bin:--------------------")

    for bin in range(1, Data_hist.GetNbinsX()+1, 5):
        content1 = Data_hist.GetBinContent(bin)+Data_hist.GetBinContent(bin+1)+(Data_hist.GetBinContent(bin+2)/2)
        Data_hist_contents.append(content1)

        content2 = (Data_hist.GetBinContent(bin+2)/2)+Data_hist.GetBinContent(bin+3)+Data_hist.GetBinContent(bin+4)
        Data_hist_contents.append(content2)

        content3 = eeBkg_hist.GetBinContent(bin)+eeBkg_hist.GetBinContent(bin+1)+(eeBkg_hist.GetBinContent(bin+2)/2)
        eeBkg_hist_contents.append(content3)

        content4 = (eeBkg_hist.GetBinContent(bin+2)/2)+eeBkg_hist.GetBinContent(bin+3)+eeBkg_hist.GetBinContent(bin+4)
        eeBkg_hist_contents.append(content4)

        content5 = CEPbkg_hist.GetBinContent(bin)+CEPbkg_hist.GetBinContent(bin+1)+(CEPbkg_hist.GetBinContent(bin+2)/2)
        CEPbkg_hist_contents.append(content5)

        content6 = (CEPbkg_hist.GetBinContent(bin+2)/2)+CEPbkg_hist.GetBinContent(bin+3)+CEPbkg_hist.GetBinContent(bin+4)
        CEPbkg_hist_contents.append(content6)

        StatUnc1 = math.sqrt(content1)/(content1 - content3 - content5)
        StatUnc_contents.append("%.4f" % StatUnc1)

        StatUnc2 = math.sqrt(content2)/(content2 - content4 - content6)
        StatUnc_contents.append("%.4f" % StatUnc2)

    for bin in range(0,4):

        print ("Statistical uncertainty on Data[", bin + 1 ,"]:", StatUnc_contents[bin])

    return StatUnc_contents

def MCcross():

    for bin in range(1, Data_hist.GetNbinsX()+1, 5):
        BW1 = Data_hist.GetBinWidth(bin)+Data_hist.GetBinWidth(bin+1)+(Data_hist.GetBinWidth(bin+2)/2)
        BW_contents.append(BW1)

        BW2 = (Data_hist.GetBinWidth(bin+2)/2)+Data_hist.GetBinWidth(bin+3)+Data_hist.GetBinWidth(bin+4)
        BW_contents.append(BW2)

        content1 = (Sig_hist.GetBinContent(bin) + Sig_hist.GetBinContent(bin+1) + (Sig_hist.GetBinContent(bin+2)/2))
        MCcross1 = content1/(BW1*Lint)
        MCcross_contents.append(MCcross1)

        content2 = (Sig_hist.GetBinContent(bin+2)/2) + Sig_hist.GetBinContent(bin+3) + Sig_hist.GetBinContent(bin+4)
        MCcross2 = content2/(BW2*Lint)
        MCcross_contents.append(MCcross2)

    return MCcross_contents

def MCunc():

    print ("----------------------------")
    bin_contents = []
    MCstat_content = []

    for bin in range(1, Data_hist.GetNbinsX()+1, 5):
        content1 = math.sqrt(Sig_hist.GetBinError(bin)**2+Sig_hist.GetBinError(bin+1)**2+(Sig_hist.GetBinError(bin+2)/math.sqrt(2))**2)
        bin_contents.append(content1)

        content2 = math.sqrt((Sig_hist.GetBinError(bin+2)/math.sqrt(2))**2+Sig_hist.GetBinError(bin+3)**2+(Sig_hist.GetBinError(bin+4))**2)
        bin_contents.append(content2)
    
        MCstat1 = content1 / (Sig_hist.GetBinContent(bin)+Sig_hist.GetBinContent(bin+1)+(Sig_hist.GetBinContent(bin+2)/2))
        MCstat_content.append("%.4f" % MCstat1)

        MCstat2 = content2 / ((Sig_hist.GetBinContent(bin+2)/2)+Sig_hist.GetBinContent(bin+3)+(Sig_hist.GetBinContent(bin+4)))
        MCstat_content.append("%.4f" % MCstat2)
    for bin in range(0,4):

        print("Statistical uncertainty on MC[", bin + 1 ,"]:", MCstat_content[bin])

    return MCstat_content

'''

cosDifCross()
statUncData()
MCcross()
MCunc()
'''


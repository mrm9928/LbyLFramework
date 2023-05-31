import ROOT as root
import math

# Determine the path to the ROOT files 
D18_Input = root.TFile.Open("~/IAP/Framework/Inputs/data18_all.root")
D15_Input = root.TFile.Open("~/IAP/Framework/Inputs/data15_all.root")
Inputs = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
Truth_Input = root.TFile.Open("~/IAP/Framework/Inputs/histlbylsignal.root")

# Define the histograms for the Data and the backgrounds for rapidity
D18_hist= D18_Input.Get("nominal/06_aco_cut/candidate/mass_unfolding") #2018 Data Histogram
D15_hist = D15_Input.Get("nominal/06_aco_cut/candidate/mass_unfolding") #2015 Data Histogram
Sig_hist = Inputs.Get("mass/signal;1") #LbyL Signal Histogram
eeBkg_hist = Inputs.Get("mass/ee;1") #QED Background Histogram
CEPbkg_hist = Inputs.Get("mass/cep;1") #CEP Background Histogram
Truth_hist = Truth_Input.Get("Truth/Mass")

Lint = 2.22                           # Integrated luminosity

Data_hist_contents = []
eeBkg_hist_contents = []
CEPbkg_hist_contents = []
Signal_hist_contents = []
StatUnc_contents =[]
BW_contents = []
diffid_contents = []
MCcross_contents = []
Truth_hist_contents = []
        
# Define the function that calculates 
def DifFid():

    
    # Define some constants and uncertainties
    Truth = Truth_hist.Integral()
    PredSigma = 78
    Lsig = Truth/PredSigma
    ScaleFactor = Lint/Lsig
    
    # Normalize the signal histograms
    for bin in range(1, Truth_hist.GetNbinsX() + 1):
        bin_content = Truth_hist.GetBinContent(bin)
        scaled_bin_content = bin_content * ScaleFactor
        Truth_hist.SetBinContent(bin, scaled_bin_content)
    
    # Create an empty list to store the bin contents of the mass distribution histograms


    Sig_hist.Rebin(5)

    eeBkg_hist.Rebin(5)
    CEPbkg_hist.Rebin(5)
    Truth_hist.Rebin(50)

    #Plot the rebinned histogram
    canvas = root.TCanvas("canvas", "canvas", 800, 600)
    Truth_hist.Draw()
    canvas.Draw()

    #Save the canvas as a PDF file
    canvas.SaveAs("output.pdf")

    # Loop through the bins of the histograms and retrieve the bin contents
    for bin in range(2, D15_hist.GetNbinsX()):
        BW = D18_hist.GetBinWidth(bin)
        BW_contents.append(BW)
        content = D15_hist.GetBinContent(bin)+D18_hist.GetBinContent(bin)
        Data_hist_contents.append(content)
            
        content2 = eeBkg_hist.GetBinContent(bin)
        eeBkg_hist_contents.append(content2)
            
        content3 = CEPbkg_hist.GetBinContent(bin)
        CEPbkg_hist_contents.append(content3)

        content4 = Truth_hist.GetBinContent(bin)
        Truth_hist_contents.append(content4)

        content5 = Sig_hist.GetBinContent(bin)
        Signal_hist_contents.append(content5)

        diffid = (content - content2 - content3)/ (BW*content5/content4*Lint)
        diffid_contents.append("%.3f" % diffid)

    for bin in range(5, D15_hist.GetNbinsX()+1):
        BW = D18_hist.GetBinWidth(bin)
        BW_contents.append(BW)

        content = D15_hist.GetBinContent(bin)+D18_hist.GetBinContent(bin)
        Data_hist_contents.append(content)
            
        content2 = eeBkg_hist.GetBinContent(bin)+eeBkg_hist.GetBinContent(bin+1)
        eeBkg_hist_contents.append(content2)
            
        content3 = CEPbkg_hist.GetBinContent(bin)+CEPbkg_hist.GetBinContent(bin+1)
        CEPbkg_hist_contents.append(content3)

        content4 = Truth_hist.GetBinContent(bin)+Truth_hist.GetBinContent(bin+1)
        Truth_hist_contents.append(content4)

        content5 = Sig_hist.GetBinContent(bin)+Sig_hist.GetBinContent(bin+1)
        Signal_hist_contents.append(content5)

        diffid = (content - content2 - content3)/ (BW*content5/content4*Lint)
        diffid_contents.append("%.3f" % diffid)

    

    print("---------------Differential cross section bin by bin:--------------------")

    for bin in range(2, D15_hist.GetNbinsX()+1):

        print ("Differential cross section for diphoton invariant mass[",bin-1,"]:",diffid_contents[bin-2])


    return diffid_contents

def statUncData():
    print("---------------Relative systematic uncertainties bin by bin:--------------------")

    for bin in range(2, D15_hist.GetNbinsX()):
        content = D15_hist.GetBinContent(bin)+D18_hist.GetBinContent(bin)
        Data_hist_contents.append(content)

        content2 = eeBkg_hist.GetBinContent(bin)
        eeBkg_hist_contents.append(content2)
            
        content3 = CEPbkg_hist.GetBinContent(bin)
        CEPbkg_hist_contents.append(content3)

        StatUnc = math.sqrt(content)/(content - content2 - content3)
        StatUnc_contents.append("%.4f" % StatUnc)

        #print (content2 + content3)

        print ("Statistical uncertainty on Data[", bin - 1 ,"]:", "%.4f" % StatUnc)

    for bin in range(5, D15_hist.GetNbinsX()+1):
        content = D15_hist.GetBinContent(bin)+D18_hist.GetBinContent(bin)
        Data_hist_contents.append(content)

        content2 = eeBkg_hist.GetBinContent(bin)+eeBkg_hist.GetBinContent(bin+1)
        eeBkg_hist_contents.append(content2)
            
        content3 = CEPbkg_hist.GetBinContent(bin)+CEPbkg_hist.GetBinContent(bin+1)
        CEPbkg_hist_contents.append(content3)

        StatUnc = math.sqrt(content)/(content - content2 - content3)
        StatUnc_contents.append("%.4f" % StatUnc)

        #print (content2 + content3)

        print ("Statistical uncertainty on Data[", bin - 1 ,"]:", "%.4f" % StatUnc)

    return StatUnc_contents


def MCcross():


    for i in [2,3,4,5]:
        BW = D18_hist.GetBinWidth(i)
        BW_contents.append(BW)
        MCcross= Truth_hist_contents[i-2]/(BW*Lint)
        MCcross_contents.append(MCcross)
        

    return MCcross_contents

def MCunc():

    print ("----------------------------")

    bin2_contents = []
    MCstat_content = []

    for bin in [2,3,4]:
        content3 = Truth_hist.GetBinError(bin)
        bin2_contents.append(content3)
    
        MCstat = content3 / Truth_hist.GetBinContent(bin)
        MCstat_content.append("%.4f" % MCstat)

        print("Statistical uncertainty on MC[", bin - 1 ,"]:", "%.4f" % MCstat)


    for bin in range(5,6):
        content3 = math.sqrt(pow(Truth_hist.GetBinError(bin),2)+pow(Truth_hist.GetBinError(bin+1),2))
        bin2_contents.append(content3)

        MCstat = content3 / (Truth_hist.GetBinContent(bin)+Truth_hist.GetBinContent(bin+1))
        MCstat_content.append("%.4f" % MCstat)

        print("Statistical uncertainty on MC[", bin - 1 ,"]:", "%.4f" % MCstat)
    
    return MCstat_content
'''
DifFid()
MCcross()
MCunc()
'''
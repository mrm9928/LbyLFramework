import ROOT as root
import math

# Define the function that calculates the square root of the sum of squared errors

def quadratic_sum(liste):
    s = 0
    for val in liste:
        s += val ** 2
    return math.sqrt(s)
    
# Define the function that calculates the uncorrelated systematic uncertainties
def unc(var, label):
    # Determine the path to the ROOT file 
    Input = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
    
    # Define the histograms for the Data and the backgrounds
    RecoMC_hist = Input.Get("mass/signal;1")
    hist = Input.Get("mass/signal_sys_"+var)
   
    # Create an empty list to store the bin contents of the source of uncertainty histogram
    bin_contents = []

    # Loop through the bins of the histogram and retrieve the bin content
    for bin in range(1, hist.GetNbinsX() + 1):
         content = hist.GetBinContent(bin)
         bin_contents.append(content)
    
    value = quadratic_sum(bin_contents) * 100 / RecoMC_hist.Integral()
    
    print(label, ":", value, "%")
    
    return value

# Define the function that calculates the correlated systematic uncertainties

Input = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
RecoMC_hist = Input.Get("mass/signal;1")

hist = Input.Get("mass/signal_sys_TRIG__1down")

def CorrUnc(var, label):
    # Determine the path to the ROOT file 
    Input = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")

    # Define the histograms for the backgrounds
    hist = Input.Get("mass/signal_sys_"+var)

    # Create an empty list to store the bin contents of the source of uncertainty histogram
    bin_contents = []

    # Loop through the bins of the histogram and retrieve the bin content
    for bin in range(1, hist.GetNbinsX() + 1):
         content = hist.GetBinContent(bin)
         bin_contents.append(content)

    sum = 0

    for b in range(1, hist.GetNbinsX() + 1):
        for B in range(1, hist.GetNbinsX() + 1):
            sum += bin_contents[b-1]*bin_contents[B-1]
    
    corrsysunc = math.sqrt(sum) * 100 / RecoMC_hist.Integral()

    print(label, ":", corrsysunc, "%")
    
    return corrsysunc

def updown(var, label):
    up = CorrUnc(var+"up", "Upper "+label)
    down = CorrUnc(var+"down", "Down "+label)
    average = (up + down)/2
    print (label, ":", average, "%")

    return average

def AltSig():

    AltSigMC_hist = Input.Get("mass/signal_alt_2;1")

    AlterSig = (AltSigMC_hist.Integral() - RecoMC_hist.Integral())* 100 / RecoMC_hist.Integral()
    
    print("Alternative Signal MC:", AlterSig, "%") 

    return AlterSig

def MCstat():
    
    # Create an empty list to store the bin contents of the signal MC statistics histogram
    bin2_contents = []

    # Loop through the bins of the histogram and retrieve the bin content
    for bin in range(1, RecoMC_hist.GetNbinsX() + 1):
         content3 = RecoMC_hist.GetBinError(bin)
         bin2_contents.append(content3)
    
    MCstat = quadratic_sum(bin2_contents) *100 / RecoMC_hist.Integral()
    
    print("Signal MC Statistics:", MCstat, "%")

    return MCstat

def total():

    sysunclist = [updown("TRIG__1", "Trigger Efficiency"), unc("PH_RECOeta", "Photon Reconstruction Efficiency"), unc("PH_PIDeta", "Photon Identification Efficiency"), updown("EG_SCALE_ALL__1", "Photon Energy Scale"), updown("EG_RESOLUTION_ALL__1", "Photon Energy Resolution"), AltSig(), MCstat()]   

    total = quadratic_sum(sysunclist)

    print("Total:", total, "%" )

    return total


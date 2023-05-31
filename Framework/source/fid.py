import ROOT as root
import math

from .sysunc import *

# Define the function that calculates the square root of the sum of squared errors

def quadratic_sum(val, liste):
    s = 0
    for val in liste:
        s += val ** 2
    return math.sqrt(s)
    
# Define the function that calculates the fiducial cross section with details
def fid():
    # Determine the path to the ROOT file 
    Input = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
    Truth_Input = root.TFile.Open("~/IAP/Framework/Inputs/histlbylsignal.root")

    # Define the histograms for the Data and the backgrounds
    Data_hist = Input.Get("mass/data;1")
    RecoMC_hist = Input.Get("mass_large/signal;1")
    eeBkg_hist = Input.Get("mass/ee;1")
    eeBkgsys_hist = Input.Get("mass/ee_sys;1")
    CEPbkg_hist = Input.Get("mass/cep;1")
    CEPbkgsys_hist = Input.Get("mass/cep_sys;1")
    TruthMC_hist = Truth_Input.Get("Truth/Mass")

    # Calculate the number of events in the histograms
    NData = Data_hist.Integral()          # Number of events in the data histogram
    NeeBkg = eeBkg_hist.Integral()         # Number of events in the e+e- background histogram
    NCEPbkg = CEPbkg_hist.Integral()      # Number of events in the CEP background histogram
    Nbkg = NeeBkg + NCEPbkg               # Total number of background events
    Reco = RecoMC_hist.Integral()         # Total number of reconstructed Monte Carlo events
    Truth = TruthMC_hist.Integral()       # Total number of true Monte Carlo events

    # Define some constants and uncertainties
    Lint = 2.22                           # Integrated luminosity
    dL = 0.07                             # Uncertainty on the integrated luminosity
    PredCross = 78
    Lsig = Truth/PredCross
    ScaleFactor = Lint/Lsig
    TruthNorm = Truth * ScaleFactor
    C = Reco/TruthNorm                            # Detector correction factor
    dC = total() * C / 100                    # Uncertainty on the overall correction factor
    

    # Create an empty list to store the bin contents of the e+e- background systematic uncertainty histogram
    eeBkgsysbin_contents = []

    # Loop through the bins of the histogram and retrieve the bin content
    for bin in range(1, eeBkgsys_hist.GetNbinsX() + 1):
         content = eeBkgsys_hist.GetBinContent(bin)
         eeBkgsysbin_contents.append(content)   
    
    # Calculate the uncertainty of the e+e- background events using the quadractic sum function defined earlier
    dNeeBkg = quadratic_sum(content, eeBkgsysbin_contents)
    
    # Create an empty list to store the bin contents of the CEP background systematic uncertainty histogram
    CEPbkgsysbin_contents = []

    # Loop through the bins of the histogram and retrieve the bin content
    for bin in range(1, CEPbkgsys_hist.GetNbinsX() + 1):
         content = CEPbkgsys_hist.GetBinContent(bin)
         CEPbkgsysbin_contents.append(content)   
    
    # Calculate the uncertainty of the CEP background events using the quadractic sum function defined earlier
    dNCEPbkg = quadratic_sum(content, CEPbkgsysbin_contents)
    
    # Calculate the uncertainty of the total background events using the quadractic sum of the two background
    dNbkg = math.sqrt ( dNeeBkg ** 2 + dNCEPbkg ** 2 )
    
    # Calculate some uncertainties
    dNData = math.sqrt(NData)            # Statistical uncertainty on the data
    sigma = (NData - Nbkg) / ( C * Lint ) # Fiducial cross section
    statUnc = sigma * dNData / (NData - Nbkg) # Statistical uncertainty for the data on the fiducial cross section
    LUnc = sigma * dL / Lint              # Luminosity uncertainty on the fiducial cross section
    #eeBkgUnc = sigma * dNeeBkg / (NData - Nbkg) # Systematic uncertainty for the e+e- background on the fiducial cross section
    #CEPbkgUnc = sigma * dNCEPbkg / (NData - Nbkg) # Systematic uncertainty for the CEP background on the fiducial cross section
    BkgUnc = sigma * dNbkg / (NData - Nbkg)
    CUnc = sigma * dC / C                 # Systematic uncertainty for the correction on the fiducial cross section
    sysUnc = math.sqrt(pow(BkgUnc, 2) + pow(CUnc, 2)) # Total systematic uncertainty on the fiducial cross section


    # Print the results
    print("Number of events for the Data: NData = ", NData, "events")
    print("Number of events for the background: Nbkg = ", Nbkg, "events")
    print("Overall detector correction factor: C = ", C)
    print("Uncertainty on the correction factor: dC = ", dC)
    print("Integrated luminosity: Lint = ", Lint, "nb^(-1)")
    print("Uncertainty on the integrated luminosity: dL = ", dL, "nb^(-1)")
    print("Fiducial cross section: sigma = ", sigma, "nb")
    print("Statistical uncertainty on the Data: dNData = ", dNData, "events")
    print("Statistical uncertainty for the data on the fiducial cross section: statUnc = ", statUnc, "nb")
    print("Luminosity uncertainty on the fiducial cross section: LUnc = ", LUnc, "nb")
    print("Uncertainty on the e+e- background: dNeeBkg = ", dNeeBkg, "events")
    print("Uncertainty on the CEP background: dNCEPbkg = ", dNCEPbkg, "events")
    print("Uncertainty on the total background: dNbkg = ", dNbkg, "events")
    print("Systematic uncertainty for the correction factor on the fiducial cross section: CUnc = ", CUnc, "nb")
    print("Total systematic uncertainty on the fiducial cross section: sysUnc = ", sysUnc, "nb")
    print("Fiducial cross section with uncertainties: sigma = ", sigma, "± ", statUnc ,"(stat.) ± ", sysUnc, "(sys.) ± ", LUnc, " (lumi.) nb") 
    
'''
fid()
'''



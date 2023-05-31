#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *

import ROOT
import ROOT as root
import atlasplots as aplt
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1
from array import array
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TLatex, TChain


from source.Plotting import *
from source.fid import *


print("---------------Generating plots:--------------------")

plot("rapidity", -2.4, 2.4, 0, 45, "Events / 0.6", "y_{\gamma\gamma}")
plot("pt", 0, 2, 0, 45, "Events / 0.2 GeV", "p_{T}^{\gamma\gamma} [GeV]")
plot("cos_theta_star", 0, 1, 0, 25, "Events / 0.1", "|cos(\\theta*)|" )
plot("leading_photon_pt", 2, 15, 0, 55, "Photons / GeV", "Leading photon E_{T} [GeV]")
plot("leading_photon_eta", -2.4, 2.4, 0, 35, "Photons / 0.6", "Leading photon \eta")
plot("mass", 5, 30, 0, 25, "Events / GeV", "m_{\gamma\gamma} [GeV]")

print("---------------Calculating Systematic Uncertainties & Fiducial Cross Section:--------------------")

fid()
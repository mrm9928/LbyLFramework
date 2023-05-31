import ROOT as root
import atlasplots as aplt


def plot(var, xlim1, xlim2, ylim1, ylim2, ylabel, xlabel):

    # Set the ATLAS Style
    aplt.set_atlas_style()

    # Create a figure and axes
    fig, (ax1, ax2) = aplt.ratio_plot(name="fig"+var, figsize=(800, 800), hspace=0.05)

    # Determine the path to the ROOT file 
    Input = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
    
    # Define the histograms for the Data, the signal and the backgrounds
    Data_hist = Input.Get(var+"/data;1")

    Sig_hist = Input.Get(var+"/signal;1")
    Sig_hist.SetLineColor(root.kRed+1)
    
    eeBkg_hist = Input.Get(var+"/ee;1")
    sky_blue = root.TColor.GetColor(135, 206, 235)
    eeBkg_hist.SetFillColor(sky_blue)
    
    CEPbkg_hist = Input.Get(var+"/cep;1")
    CEPbkg_hist.SetFillColor(root.kGray+1)
    
    err_hist = Input.Get(var+"/expected_summed_sys;1")
 
    # Stack the signal and the backgrounds
    bkg_and_sig = root.THStack("bkg_and_sig", "")
    bkg_and_sig.Add(eeBkg_hist)
    bkg_and_sig.Add(CEPbkg_hist)
    bkg_and_sig.Add(Sig_hist)
    
    # Set the systematic uncertainties for the MC samples  
    for i in range(0, err_hist.GetNbinsX()):
    	(bkg_and_sig.GetStack().Last()).SetBinError(i+1, err_hist.GetBinContent(i+1))

    # Turn the Data histogram to a graph
    Data_graph = aplt.root_helpers.hist_to_graph(Data_hist)
    
    # Draw the Data as a graph and the MC Samples as histograms on the first axes
    ax1.plot(Data_graph, "P")
    ax1.plot(bkg_and_sig)
    
    # Plot the systematic uncertainties as a hatched band
    err_band = aplt.root_helpers.hist_to_graph(
        bkg_and_sig.GetStack().Last(),
        show_bin_width=True
    )
    ax1.plot(err_band, "2", fillcolor=1, fillstyle=3254, linewidth=0)
    
    #Determine x-range and y-range for the first axes
    ax1.set_xlim(xlim1, xlim2)
    ax1.set_ylim(ylim1, ylim2)
    
    # Draw line at y=1 in ratio panel
    line = root.TLine(ax1.get_xlim()[0], 1, ax1.get_xlim()[1], 1)
    ax2.plot(line)
    
    # Plot the relative error on the ratio axes
    err_band_ratio = aplt.root_helpers.hist_to_graph(
        bkg_and_sig.GetStack().Last(),
        show_bin_width=True,
        norm=True 
    )
    ax2.plot(err_band_ratio, "2", fillcolor=1, fillstyle=3254)

    # Calculate and draw the ratio
    ratio_hist = Data_hist.Clone("ratio_hist")
    ratio_hist.Divide(bkg_and_sig.GetStack().Last())
    ratio_graph = aplt.root_helpers.hist_to_graph(ratio_hist)
    ax2.plot(ratio_graph, "P0")
    
    # Use same x-range in lower axes as upper axes
    ax2.set_xlim(ax1.get_xlim())
    
    #Determine y-range for the second axes
    ax2.set_ylim(0, 2)

    # Add extra space at top of plot to make room for labels
    ax1.add_margins(top=0.16)

    # Set axis titles
    ax1.set_ylabel(ylabel, titleoffset=1.7)
    ax2.set_ylabel("Data / MC", loc="centre", titleoffset=1.7)
    ax2.set_xlabel(xlabel, titleoffset=1)
    
    # Add extra space at top and bottom of ratio panel
    ax2.add_margins(top=0.1, bottom=0.1)

    # Go back to top axes to add labels
    ax1.cd()

    # Add the ATLAS Label
    aplt.atlas_label(text="Internal", loc="upper left")
    ax1.text(0.2, 0.84, "Pb+Pb #sqrt{s_{NN}} = 5.02 TeV", size=22, align=13)

    # Add legend
    legend = ax1.legend(
        loc=(0.5, 0.65, 1 - root.gPad.GetRightMargin() - 0.03, 1 - root.gPad.GetTopMargin() - 0.03),
        textsize=22
    )
    legend.AddEntry(Data_graph, "Data 2015 + 2018 (2.2 nb^{-1})", "EP")
    legend.AddEntry(Sig_hist, "Signal (\gamma\gamma \\rightarrow \gamma\gamma)", "F")
    legend.AddEntry(CEPbkg_hist, "CEP gg \\rightarrow \gamma\gamma", "F")
    legend.AddEntry(eeBkg_hist, "\gamma\gamma \\rightarrow e^{+}e^{-}", "F")
    legend.AddEntry(err_band, "Systematic uncertainty", "F")

    # Save the plot as a PDF
    fig.savefig("Outputs/graph_"+ var +".pdf")

'''
plot("rapidity", -2.4, 2.4, 0, 45, "Events / 0.6", "y_{\gamma\gamma}")
plot("pt", 0, 2, 0, 45, "Events / 0.2 GeV", "p_{T}^{\gamma\gamma} [GeV]")
plot("cos_theta_star", 0, 1, 0, 25, "Events / 0.1", "|cos(\\theta*)|" )
plot("leading_photon_pt", 2, 15, 0, 55, "Photons / GeV", "Leading photon E_{T} [GeV]")
plot("leading_photon_eta", -2.4, 2.4, 0, 35, "Photons / 0.6", "Leading photon \eta")
plot("mass", 5, 30, 0, 25, "Events / GeV", "m_{\gamma\gamma} [GeV]")

'''

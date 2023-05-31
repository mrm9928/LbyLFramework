import ROOT as root
import array
import math
import atlasplots as aplt

import mass_DifCross
import mass_errdif



def mass_plot():
    enreso_contents = []
    enscale_contents = []
    trig_contents = []
    syserr_contents = []

    # Set the ATLAS Style
    aplt.set_atlas_style()

    # Create a figure and axes
    fig, (ax1) = aplt.subplots(1,1, name="fig", figsize=(800, 800))

    difcross_contents=[float(x) for x in mass_DifCross.DifFid()]
    staterr_contents=[float(i) for i in mass_DifCross.statUncData()]
    phreco_contents=[float(i) for i in mass_errdif.Err("PH_RECOeta", "PhReco", "PhReco")]
    phiden_contents=[float(i) for i in mass_errdif.Err("PH_PIDeta", "PhIden", "PhIden")]
    enresodown_contents=[float(i) for i in mass_errdif.Err("EG_RESOLUTION_ALL__1down", "EnResoDown", "EnResoDown")]
    enresoup_contents=[float(i) for i in mass_errdif.Err("EG_RESOLUTION_ALL__1up", "EnResoUp", "EnResoUp")]
    enscaleup_contents=[float(i) for i in mass_errdif.Err("EG_SCALE_ALL__1down", "EnScaleDown", "EnScaleDown")]
    enscaledown_contents=[float(i) for i in mass_errdif.Err("EG_SCALE_ALL__1up", "EnScaleUp", "EnScaleUp")]
    trigdown_contents=[float(i) for i in mass_errdif.Err("TRIG__1down", "TrigDown", "TrigDown")]
    trigup_contents=[float(i) for i in  mass_errdif.Err("TRIG__1up", "TrigUp", "TrigUp")]
    MCerr_contents=[float(i) for i in mass_DifCross.MCunc()]
    MCcross_contents=[float(i) for i in mass_DifCross.MCcross()]

    edges = array.array('d', [5, 10, 15, 20, 30])

    histogram = root.TH1F("histogram", "histogram", len(edges) - 1 , edges)

    histogram3 = root.TH1F("histogram3", "histogram3", len(edges) - 1 , edges)

    histogram4 = root.TH1F("histogram4", "histogram4", len(edges) - 1 , edges)
    
    # Loop through the bins of the histograms and retrieve the bin contents
    for bin in [0,1,2,3]:

        enreso = (enresoup_contents[bin]+enresodown_contents[bin])/2 
        enreso_contents.append(enreso)
        enscale = (enscaleup_contents[bin]+enscaledown_contents[bin])/2 
        enscale_contents.append(enscale)
        trig = (trigup_contents[bin]+trigdown_contents[bin])/2 
        trig_contents.append(trig)
        syserr = difcross_contents[bin] * math.sqrt(pow(phreco_contents[bin],2)+pow(phiden_contents[bin],2)+pow(enreso_contents[bin],2)+pow(enscale_contents[bin],2)+pow(trig_contents[bin],2))
        syserr_contents.append(syserr)


        histogram.SetBinContent(bin+1, difcross_contents[bin])
        histogram.SetBinError(bin+1, difcross_contents[bin]*staterr_contents[bin])
        histogram3.SetBinContent(bin+1, MCcross_contents[bin])
        histogram3.SetBinError(bin+1, MCcross_contents[bin]*MCerr_contents[bin])
        histogram3.SetLineColor(root.kRed+1)
        histogram4.SetBinContent(bin+1, difcross_contents[bin])
        histogram4.SetBinError(bin+1, (difcross_contents[bin]*staterr_contents[bin])+syserr_contents[bin])

        print(bin+1)
        print(histogram.GetBinContent(bin+1))
        print(histogram.GetBinError(bin+1))
        print(histogram3.GetBinContent(bin+1))
        print(histogram3.GetBinError(bin+1))
        print(histogram4.GetBinContent(bin+1))
        print(histogram4.GetBinError(bin+1))

 
    histogram.Add(histogram3)
    hist.append(histogram)


    graph = aplt.root_helpers.hist_to_graph(histogram)

    ax1.plot(graph, "P")

    # ax1.plot(histogram2, "2", fillcolor=1, fillstyle=3254, linewidth=0)

    ax1.plot(histogram3)

    err_band = aplt.root_helpers.hist_to_graph(
        histogram3,
        show_bin_width=True
    )
    ax1.plot(err_band, "2", fillcolor=root.kRed+1, fillstyle=3244, linewidth=0)

    err_band2 = aplt.root_helpers.hist_to_graph(
        histogram4,
        show_bin_width=True
    )
    ax1.plot(err_band2, "2", fillcolor=1, fillstyle=3254, linewidth=0)

    ax1.set_xlim(5, 30)
    ax1.set_ylim(0.1, 60)
    #ax1.set_ylim(0,25)

    ax1.set_yscale("log")

    # Set axis titles
    ax1.set_ylabel("d\sigma/dm_{\gamma\gamma} [nb/GeV]", titleoffset=1.7)
    ax1.set_xlabel("m_{\gamma\gamma} [GeV]")


     # Add the ATLAS Label
    aplt.atlas_label(text="Internal", loc="upper left", size=22)
    ax1.text(0.2, 0.87, "Pb+Pb #sqrt{s_{NN}} = 5.02 TeV", size=15, align=13)

    # Add legend
    legend = ax1.legend(
        loc=(0.6, 0.65, 1 - root.gPad.GetRightMargin() - 0.03, 1 - root.gPad.GetTopMargin() - 0.03),
        textsize=15
    )
    legend.AddEntry(graph, "Data 2015 + 2018 (2.2 nb^{-1})", "EP")
    legend.AddEntry(err_band2, "Syst. + Stat.", "EF")
    legend.AddEntry(histogram3, "SuperChic 3.0", "L")
    legend.AddEntry(err_band, "MC Stat.", "EF")

    fig.savefig("~/IAP/Framework/Outputs/diff_graph.pdf")

    hist = []

    for i in range (0,4):
        histogram.Add(histogram3)
        hist.append(histogram)

    print(hist[1])
        
    

mass_plot()


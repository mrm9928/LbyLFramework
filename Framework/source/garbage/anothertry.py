'''
def FidPlot():

    # Set the ATLAS Style
    aplt.set_atlas_style()

    # Create a figure and axes
    fig, (ax1) = aplt.subplots(1,1, name="fig", figsize=(800, 600))

    staterr_contents = random.sample(range(10,15), 4)
    syserr_contents = random.sample(range(5,10), 4)
    MC_contents = random.sample(range(10,50), 4)
    MCerr_contents = random.sample(range(2,10), 4)

    histogram = root.TH1F("histogram", "histogram", 6, 0, 30)

    histogram2 = root.TH1F("histogram2", "histogram2", 6, 0, 30)

    histogram3 = root.TH1F("histogram3", "histogram3", 6, 0, 30)

    histogram4 = root.TH1F("histogram4", "histogram4", 6, 0, 30)

    diffid_contents2 = [float(i) for i in diffid_contents]

    # Loop through the bins of the histograms and retrieve the bin contents
    for bin in range(1, D18_hist.GetNbinsX()):
        histogram.SetBinContent(bin, diffid_contents2[bin-1])
        histogram.SetBinError(bin, staterr_contents[bin-1])
        histogram2.SetBinContent(bin, staterr_contents[bin-1]+syserr_contents[bin-1])
        histogram3.SetBinContent(bin, MC_contents[bin-1])
        histogram3.SetBinError(bin, MCerr_contents[bin-1])
        histogram3.SetLineColor(root.kRed+1)
        histogram4.SetBinContent(bin, diffid_contents2[bin-1])
        histogram4.SetBinContent(bin, staterr_contents[bin-1]+syserr_contents[bin-1])


    graph = aplt.root_helpers.hist_to_graph(histogram)

    ax1.set_xlim(0, 30)
    ax1.set_ylim(0.1, 10)

    ax1.set_yscale("log")

    ax1.plot(graph, "P")

    # ax1.plot(histogram2, "2", fillcolor=1, fillstyle=3254, linewidth=0)

    ax1.plot(histogram3)

    err_band = aplt.root_helpers.hist_to_graph(
        histogram3,
        show_bin_width=True
    )
    ax1.plot(err_band, "2", fillcolor=root.kRed+1, fillstyle=3254, linewidth=0)

    
    err_band2 = aplt.root_helpers.hist_to_graph(
        histogram4,
        show_bin_width=True
    )
    ax1.plot(err_band2, "2", fillcolor=1, fillstyle=3254, linewidth=0)

    ax1.set_xlim(0, 30)
    ax1.set_ylim(0.1, 50)

     # Add the ATLAS Label
    aplt.atlas_label(text="Internal", loc="upper left")
    ax1.text(0.2, 0.84, "Pb+Pb #sqrt{s_{NN}} = 5.02 TeV", size=22, align=13)

    # Add legend
    legend = ax1.legend(
        loc=(0.5, 0.65, 1 - root.gPad.GetRightMargin() - 0.03, 1 - root.gPad.GetTopMargin() - 0.03),
        textsize=22
    )
    legend.AddEntry(graph, "Data 2015 + 2018 (2.2 nb^{-1})", "EP")
    legend.AddEntry(histogram3, "SuperChic 3.0", "LE23")
    legend.AddEntry(err_band2, "Syst. + Stat.", "EF")

    fig.savefig("Graph2.pdf")
'''

'''
    for bin in range(1, Signal_hist.GetNbinsX()+1):
        Reco_hist.SetBinError(bin, Signal_hist.GetBinContent(bin))

    # Plot the rebinned histogram
    canvas = root.TCanvas("canvas", "canvas", 800, 600)
    Reco_hist.Draw()
    canvas.Draw()

    # Save the canvas as a PDF file
    canvas.SaveAs("output.pdf")

'''



'''
    staterr_contents = random.sample(range(10,15), 4)
    syserr_contents = random.sample(range(5,10), 4)
    MC_contents = random.sample(range(10,50), 4)
    MCerr_contents = random.sample(range(2,10), 4)
    

    histogram = root.TH1F("histogram", "histogram", 4, 0, 2.4)

    histogram2 = root.TH1F("histogram2", "histogram2", 4, 0, 2.4)

    histogram3 = root.TH1F("histogram3", "histogram3", 4, 0, 2.4)

    histogram4 = root.TH1F("histogram4", "histogram4", 4, 0, 2.4)

    # Loop through the bins of the histograms and retrieve the bin contents
    for bin in range(1, Data_hist.GetNbinsX()+1):
         content = Data_hist.GetBinContent(bin)
         Data_hist_contents.append(content)
         
         content2 = eeBkg_hist.GetBinContent(bin)
         eeBkg_hist_contents.append(content2)
         
         content3 = CEPbkg_hist.GetBinContent(bin)
         CEPbkg_hist_contents.append(content3)

         content4 = Truth_hist.GetBinContent(bin)
         Truth_hist_contents.append(content4)

         content5 = Signal_hist.GetBinContent(bin)
         Signal_hist_contents.append(content5)
         
         diffid = (content - content2 - content3)/ (content5/content4*Lint)
         diffid_contents.append(diffid)

         print("Data_hist_contents[", bin, "]=", Data_hist_contents[bin-5])
         print("eeBkg_hist_contents[", bin, "]=", eeBkg_hist_contents[bin-5])
         print("CEPbkg_hist_contents[", bin, "]=", CEPbkg_hist_contents[bin-5])
         print("diffid_contents[", bin, "]=", diffid_contents[bin-5])
         print("Truth_hist_contents[", bin, "]=", Truth_hist_contents[bin-5])
         print("Signal_hist_contents[", bin, "]=", Signal_hist_contents[bin-5])

         histogram.SetBinContent(bin-4, diffid_contents[bin-5])
         histogram.SetBinError(bin-4, staterr_contents[bin-5])
         histogram2.SetBinContent(bin-4, staterr_contents[bin-5]+syserr_contents[bin-5])
         histogram3.SetBinContent(bin-4, MC_contents[bin-5])
         histogram3.SetBinError(bin-4, MCerr_contents[bin-5])
         histogram3.SetLineColor(root.kRed+1)
         histogram4.SetBinContent(bin-4, diffid_contents[bin-5])
         histogram4.SetBinError(bin-4, staterr_contents[bin-5]+syserr_contents[bin-5])

    print(histogram.Integral())

    graph = aplt.root_helpers.hist_to_graph(histogram)

    ax1.plot(graph, "P")

    # ax1.plot(histogram2, "2", fillcolor=1, fillstyle=3254, linewidth=0)

    ax1.plot(histogram3)

    err_band = aplt.root_helpers.hist_to_graph(
        histogram3,
        show_bin_width=True
    )
    ax1.plot(err_band, "2", fillcolor=root.kRed+1, fillstyle=3254, linewidth=0)

    err_band2 = aplt.root_helpers.hist_to_graph(
        histogram4,
        show_bin_width=True
    )
    ax1.plot(err_band2, "2", fillcolor=1, fillstyle=3254, linewidth=0)

    ax1.set_xlim(0, 2.4)
    ax1.set_ylim(0, 160)

     # Add the ATLAS Label
    aplt.atlas_label(text="Internal", loc="upper left")
    ax1.text(0.2, 0.84, "Pb+Pb #sqrt{s_{NN}} = 5.02 TeV", size=22, align=13)

    # Add legend
    legend = ax1.legend(
        loc=(0.5, 0.65, 1 - root.gPad.GetRightMargin() - 0.03, 1 - root.gPad.GetTopMargin() - 0.03),
        textsize=22
    )
    legend.AddEntry(graph, "Data 2015 + 2018 (2.2 nb^{-1})", "EP")
    legend.AddEntry(histogram3, "SuperChic 3.0", "LE23")
    legend.AddEntry(err_band2, "Syst. + Stat.", "EF")

    fig.savefig("graph.pdf")

'''
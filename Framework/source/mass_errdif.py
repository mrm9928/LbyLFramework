import ROOT as root
import math

def Err(var,label, list):
    print ("----------------------------")

    Inputs = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
    err_hist = Inputs.Get("mass/signal_sys_"+var)
    Sig_hist = Inputs.Get("mass/signal;1")

    for bin in range(1, err_hist.GetNbinsX()+1):
        err_hist.SetBinError(bin, err_hist.GetBinContent(bin))

    err_hist.Rebin(5)
    Sig_hist.Rebin(5)

    bin_contents = []
    list = []

    for bin in [2,3,4]:
        x = err_hist.GetBinError(bin)
        bin_contents.append(x)
    
        err = x / Sig_hist.GetBinContent(bin)
        list.append("%.4f" % err)
        print(label+"[", bin - 1 ,"]:", "%.4f" % err)


    for bin in range(5,6):
        x = math.sqrt(pow(err_hist.GetBinError(bin),2)+pow(err_hist.GetBinError(bin+1),2))
        bin_contents.append(x)

        err = x / (Sig_hist.GetBinContent(bin)+Sig_hist.GetBinContent(bin+1))
        list.append("%.4f" % err)
        print(label+"[", bin - 1 ,"]:", "%.4f" % err)
    
    return list

Err("PH_RECOeta", "PhReco", "PhReco")
Err("PH_PIDeta", "PhIden", "PhIden")
Err("EG_RESOLUTION_ALL__1down", "EnResoDown", "EnResoDown")
Err("EG_RESOLUTION_ALL__1up", "EnResoUp", "EnResoUp")
Err("EG_SCALE_ALL__1down", "EnScaleDown", "EnScaleDown")
Err("EG_SCALE_ALL__1up", "EnScaleUp", "EnScaleUp")
Err("TRIG__1down", "TrigDown", "TrigDown")
Err("TRIG__1up", "TrigUp", "TrigUp")

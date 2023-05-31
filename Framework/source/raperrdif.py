import ROOT as root
import math

def Err(var,label, list):
    print ("----------------------------")

    Inputs = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
    err_hist = Inputs.Get("rapidity/signal_sys_"+var)
    Sig_hist = Inputs.Get("rapidity/signal;1")

    bin_contents = []
    list = []

    for bin in range(0, err_hist.GetNbinsX()-4):
        x = math.sqrt(err_hist.GetBinContent(4-bin)**2+err_hist.GetBinContent(bin+5)**2)
        bin_contents.append(x)
    
        err = x / (Sig_hist.GetBinContent(4-bin)+Sig_hist.GetBinContent(bin+5))
        list.append("%.4f" % err)
        print(label+"[", bin + 1 ,"]:", "%.4f" % err)



    return list

'''
Err("PH_RECOeta", "PhReco", "PhReco")
Err("PH_PIDeta", "PhIden", "PhIden")
Err("EG_RESOLUTION_ALL__1down", "EnResoDown", "EnResoDown")
Err("EG_RESOLUTION_ALL__1up", "EnResoUp", "EnResoUp")
Err("EG_SCALE_ALL__1down", "EnScaleDown", "EnScaleDown")
Err("EG_SCALE_ALL__1up", "EnScaleUp", "EnScaleUp")
Err("TRIG__1down", "TrigDown", "TrigDown")
Err("TRIG__1up", "TrigUp", "TrigUp")
'''

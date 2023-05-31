import ROOT as root
import math

def Err(var,label, list):
    print ("----------------------------")

    Inputs = root.TFile.Open("~/IAP/Framework/Inputs/signal_hists.root")
    err_hist = Inputs.Get("rapidity/signal_sys_"+var)
    Sig_hist = Inputs.Get("rapidity/signal;1")

    bin_contents = []
    list = []

    for bin in range(0, err_hist.GetNbinsX()+1, 5):
        x1 = math.sqrt(err_hist.GetBinContent(bin)**2+err_hist.GetBinContent(bin+1)**2+(err_hist.GetBinContent(bin+2)/math.sqrt(2))**2)
        bin_contents.append(x1)
    
        err1 = x1 / (Sig_hist.GetBinContent(bin)+Sig_hist.GetBinContent(bin+1)+(Sig_hist.GetBinContent(bin+2)/2))
        list.append("%.4f" % err1)

        x2 = math.sqrt((err_hist.GetBinContent(bin+2)/math.sqrt(2))**2)+err_hist.GetBinContent(bin+3)**2+(err_hist.GetBinContent(bin+4)**2)
        bin_contents.append(x2)
    
        err2 = x2 / ((Sig_hist.GetBinContent(bin+2)/2)+Sig_hist.GetBinContent(bin+3)+(Sig_hist.GetBinContent(bin+4)))
        list.append("%.4f" % err2)

    for bin in range (0,4):
        print(label+"[", bin + 1 ,"]:", list[bin])



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

#!/usr/bin/env python
# -*-coding:Latin-1 -*
import ROOT as root

import sysunc


def generate_latex_table():
    num_columns = 2
    num_rows = 11

    # Define the contents names
    UncSources = ['Source of Uncertainty','','Trigger efficiency', 'Photon reco. efficiency', 'Photon PID efficiency', 'Photon energy scale', 'Photon energy resolution',
                 'Photon angular resolution', 'Alternative signal MC', 'Signal MC Statistics', 'Total']
    
    values = [sysunc.updown("TRIG__1", "Trigger Efficiency"),
              sysunc.unc("PH_RECOeta", "Photon Reconstruction Efficiency"),
              sysunc.unc("PH_PIDeta", "Photon Identification Efficiency"),
              sysunc.updown("EG_SCALE_ALL__1", "Photon Energy Scale"), 
              sysunc.updown("EG_RESOLUTION_ALL__1", "Photon Energy Resolution"),
              '-', 
              sysunc.AltSig(), 
              sysunc.MCstat(),
              sysunc.total()]

        # Open the LaTeX file
    with open('/home/mrm9928/IAP/Framework/Outputs/sysunctable.tex', 'w') as f:
        # Write the LaTeX table header
        f.write('\\documentclass{article}\n')
        f.write('\\usepackage{adjustbox}\n')
        f.write('\\begin{document}\n')
        f.write('\\begin{table}[H]\n')
        f.write('\\begin{tabular}{|' + '|'.join(['c'] * num_columns) + '|}\n')
        f.write('\\hline\n')

        # Write the table content
        for row in range(num_rows):
            line = ''
            for column in range(num_columns):
                if column == 0:
                    line += UncSources[row]
                if column != num_columns - 1:
                    line += ' & '
                else:
                    line += ' \\\\\n'
            f.write(line)
            f.write('\\hline\n')

        # Write the LaTeX table footer
        f.write('\\end{tabular}\n')
        f.write('\\end{table}\n')
        f.write('\\end{document}\n')

    print('LaTeX table generated successfully.')

generate_latex_table()

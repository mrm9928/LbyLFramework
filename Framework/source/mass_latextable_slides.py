#!/usr/bin/env python
# -*-coding:Latin-1 -*
import ROOT as root

import mass_DifCross 
import mass_errdif 

Bin = [ '5 - 10', '10 - 15', '15 - 20', '20 - 30']

def generate_latex_table():
    num_columns = 8
    num_rows = 5

    # Define the contents names
    variables = ['Bin [GeV]', 'd$\sigma$/dx/bin width', 'Stat. (Data)', 'Stat. (MC)', 'Photon reco.', 'Photon PID', 'Trig. down', 'Trig. up']
    
    values = [Bin,
              mass_DifCross.DifFid(),
              mass_DifCross.statUncData(),
              mass_DifCross.MCunc(),
              mass_errdif.Err("PH_RECOeta", "PhReco", "PhReco"),
              mass_errdif.Err("PH_PIDeta", "PhIden", "PhIden"),
              mass_errdif.Err("TRIG__1down", "TrigDown", "TrigDown"),
              mass_errdif.Err("TRIG__1up", "TrigUp", "TrigUp")]

        # Open the LaTeX file
    with open('/home/mrm9928/IAP/Framework/Outputs/mass_table_slides.tex', 'w') as f:
        # Write the LaTeX table header
        f.write('\\documentclass{article}\n')
        f.write('\\usepackage{adjustbox}\n')
        f.write('\\begin{document}\n')
        f.write('\\begin{table}[H]\n')
        f.write('\\begin{adjustbox}{width=1\\textwidth}\n')
        f.write('\\begin{tabular}{|' + '|'.join(['c'] * num_columns) + '|}\n')
        f.write('\\hline\n')

        # Write the table content
        for row in range(num_rows):
            line = ''
            for column in range(num_columns):
                if row == 0:
                    line += variables[column]
                else :
                    line += values[column][row-1]
                if column != num_columns - 1:
                    line += ' & '
                else:
                    line += ' \\\\\n'
            f.write(line)
            f.write('\\hline\n')

        # Write the LaTeX table footer
        f.write('\\end{tabular}\n')
        f.write('\\end{adjustbox}\n')
        f.write('\\end{table}\n')
        f.write('\\end{document}\n')

    print('LaTeX table generated successfully.')

generate_latex_table()

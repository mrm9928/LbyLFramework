#!/usr/bin/env python
# -*-coding:Latin-1 -*
import ROOT as root

import rapDifCross 
import raperrdif 

Bin = [ "0 - 0.6", "0.6 - 1.2", "1.2 - 1.8", "1.8 - 2.4"]

def generate_latex_table():
    num_columns = 5
    num_rows = 11

    # Define the contents names
    variables = ['Bin', 'd$\sigma$/dx', 'Stat. (Data)', 'Photon reco.', 'Photon PID',
                 'Res. down', 'Res. up', 'Scale down', 'Scale up', 'Trig. down', 'Trig. up']
    
    values = [Bin,
              rapDifCross.rapDifCross(),
              rapDifCross.statUncData(),
              raperrdif.Err("PH_RECOeta", "PhReco", "PhReco"),
              raperrdif.Err("PH_PIDeta", "PhIden", "PhIden"),
              raperrdif.Err("EG_RESOLUTION_ALL__1down", "EnResoDown", "EnResoDown"),
              raperrdif.Err("EG_RESOLUTION_ALL__1up", "EnResoUp", "EnResoUp"),
              raperrdif.Err("EG_SCALE_ALL__1down", "EnScaleDown", "EnScaleDown"),
              raperrdif.Err("EG_SCALE_ALL__1up", "EnScaleUp", "EnScaleUp"),
              raperrdif.Err("TRIG__1down", "TrigDown", "TrigDown"),
              raperrdif.Err("TRIG__1up", "TrigUp", "TrigUp")]

        # Open the LaTeX file
    with open('/home/mrm9928/IAP/Framework/Outputs/raptable.tex', 'w') as f:
        # Write the LaTeX table header
        f.write('\\documentclass{article}\n')
        f.write('\\usepackage{adjustbox}\n')
        f.write('\\begin{document}\n')
        f.write('\\begin{table}[H]\n')
        f.write('\\centering\n')
        f.write('\\begin{tabular}{|' + '|'.join(['c'] * num_columns) + '|}\n')
        f.write('\\hline\n')

        # Write the table content
        for row in range(num_rows):
            line = ''
            for column in range(num_columns):
                if column == 0:
                    line += variables[row]
                else :
                    line += values[row][column-1]
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

'''
generate_latex_table()
'''
from __future__ import print_function
from __future__ import division
import sys, os
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
from getdist import plots, MCSamples
import getdist, IPython
import pylab as plt
#print('GetDist Version: %s, Matplotlib version: %s'%(getdist.__version__, plt.matplotlib.__version__))
#matplotlib 2 doesn't seem to work well without usetex on
plt.rcParams['text.usetex']=True

#----------------------------------------------------------------------------------


g = plots.getSubplotPlotter(chain_dir=[u'./../chains/N1_nierika/bao_jla/nrk_18-12-1_f1-7_conv/', './../chains/N1_nierika/planck_bao_jla/nrk_18-12-1_f1-7/'])
roots = ['2018-12-01_650000_','2018-12-01_800000_',]
params = [u'omega_b', u'omega_cdm', u'Omega_Lambda', u'b0_fld', u'b1_fld', u'H0']

param_3d = None
g.settings.alpha_filled_add=0.5

g.triangle_plot(roots, params, plot_3d_with_param=param_3d, filled=True, shaded=False
               ,legend_labels=[r'$w(N=1)$ BAO + SNe',r'$w(N=1)$ Planck + BAO + SNe']
               ,legend_loc='upper right'
               ,line_args=[{'ls':'--', 'color':'green'},{'lw':1, 'color':'darkblue'}]
               ,contour_colors=['green','darkblue'])

g.export('prueba2_mp.pdf')

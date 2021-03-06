import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import pandas as pd
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

## colormap setting
viridis = cm.get_cmap('viridis', 18)
viridis6 = cm.get_cmap('viridis', 6)
plasma = cm.get_cmap('plasma', 6)
cividis = cm.get_cmap('cividis', 6)

## input variables
alpha_1 = np.arange(0*np.pi, np.pi,  np.pi/1800)
alpha_1 = np.append(alpha_1,np.pi)
alpha_1d = np.rad2deg(alpha_1)
alpha_2 = np.arange(2/3*np.pi , np.pi, np.pi/5400)
alpha_2d = np.rad2deg(alpha_2)
# print(alpha_1.shape)
# print(alpha_2.shape)

R = 25
# print(type(R))

y = np.sin(alpha_1)
theta = 2*np.arcsin(np.sqrt((1/8)*(1-np.cos(alpha_1))))
theta_d = np.rad2deg(theta)
# print(theta.shape)

eta = np.arccos((np.sqrt(2*(1-np.cos(alpha_2)))-np.sin(theta/2))/(np.sqrt(3)*np.cos(theta/2)))
eta_d = np.rad2deg(eta)
# print(eta.shape)

## coordinates of the point 24
X_24 = np.array([])
Y_24 = np.array([])

for i in range(1801):
    if np.sqrt(3)*np.tan(theta[i]/2) > np.cos(eta[i]):
        x_24 = np.sqrt(3)*R*np.cos(eta[i])*np.cos(theta[i]/2)
        X_24 = np.append(X_24, x_24)
    else:
        x_24 = R/2*(np.sqrt(3)*np.cos(eta[i])*np.cos(theta[i]/2)+3*np.sin(theta[i]/2))
        X_24 = np.append(X_24, x_24)

# print(X_24)
# print(X_24.shape)

for i in range(1801):
    if np.sqrt(3)*np.tan(theta[i]/2) > np.cos(eta[i]):
        y_24 = R*np.cos(eta[i])*np.cos(theta[i]/2)
        Y_24 = np.append(Y_24, y_24)
    else:
        y_24 = R/2*(np.cos(eta[i])*np.cos(theta[i]/2)+np.sqrt(3)*np.sin(theta[i]/2))
        Y_24 = np.append(Y_24, y_24)
# print(Y_24)
# print(Y_24.shape)

Z_24 = R*np.cos(theta/2)*np.sin(eta)

P_24 = np.transpose(np.array([X_24, Y_24, Z_24]))
# print(P_24)

## coordinates of the point 14

X_14 = R/2*(np.sqrt(3)*np.cos(eta)*np.cos(theta/2)+np.sin(theta/2))
Y_14 = R/2*np.abs(np.sqrt(3)*np.sin(theta/2)-np.cos(eta)*np.cos(theta/2))
Z_14 = Z_24

P_14 = np.transpose(np.array([X_14, Y_14, Z_14]))

## coordinates of the point 22

X_22 = np.array([])
Y_22 = np.array([])

for i in range(1801):
    if np.sqrt(3)*np.tan(theta[i]/2) > np.cos(eta[i]):
        x_22 = R*np.sin(theta[i]/2)
        X_22 = np.append(X_22, x_22)
    else:
        x_22 = R/2*(np.sqrt(3)*np.cos(eta[i])*np.cos(theta[i]/2)-np.sin(theta[i]/2))
        X_22 = np.append(X_22, x_22)

# print("X_22 shape is", X_22.shape)

for i in range(1801):
    if np.sqrt(3)*np.tan(theta[i]/2) > np.cos(eta[i]):
        y_22 = R*np.cos(eta[i])*np.cos(theta[i]/2)
        Y_22 = np.append(Y_22, y_22)
    else:
        y_22 = R/2*(np.cos(eta[i])*np.cos(theta[i]/2)+np.sqrt(3)*np.sin(theta[i]/2))
        Y_22 = np.append(Y_22, y_22)

# print("Y_22 shape is", Y_22.shape)

Z_22 = Z_24

# print("Z_22 shape is", Z_22.shape)

P_22 = np.transpose(np.array([X_22, Y_22, Z_22]))

## coordinates of the point 13

X_13 = np.zeros([1801,])
# print("X_13 shape is", X_13.shape)

Y_13 = np.zeros([1801,])
Z_13 = np.zeros([1801,])

P_13 = np.transpose(np.array([X_13, Y_13, Z_13]))

## coordinates of the point 15

X_15 = R*(np.sqrt(3)*np.cos(eta)*np.cos(theta/2)+np.sin(theta/2))
Y_15 = np.zeros([1801,])
Z_15 = np.zeros([1801,])

P_15 = np.transpose(np.array([X_15, Y_15, Z_15]))

## coordinates of the point 32

X_32 = X_15/2
Y_32 = np.sqrt(3)/2*X_15
Z_32 = np.zeros([1801,])

P_32 = np.transpose(np.array([X_32, Y_32, Z_32]))

## coordinates of the point 23

X_23 = X_14
Y_23 = np.sqrt(3)/6*X_15
Z_23 = -np.sqrt(np.power(np.sqrt(3)/3*2*R, 2)-np.power(X_23, 2)-np.power(Y_23, 2))

P_23 = np.transpose(np.array([X_23, Y_23, Z_23]))

## distance from point 14 to point 22

d = np.sqrt(np.power(X_14 - X_22, 2) + np.power(Y_14 - Y_22, 2))

## Calculating global curvature

l = np.sqrt(np.power(X_24 - X_13, 2) + np.power(Y_24 - Y_13, 2)) # length between point 13 and point 24 in xy plane
h = Z_24
L = np.sqrt(np.power(l, 2) + np.power(h, 2))
beta = np.arcsin(h/L)
beta_d = np.rad2deg(beta)

lprime = np.sqrt(np.power(X_23 - X_13, 2) + np.power(Y_23 - Y_13, 2)) # length between point 13 and point 23 in xy plane
hprime = Z_23
Lprime = np.sqrt(np.power(lprime, 2) + np.power(hprime, 2))
gamma = np.arcsin(hprime/Lprime)
gamma_d = np.rad2deg(gamma)

mu = np.pi/2. - 2.*eta - gamma
mu_d = np.rad2deg(mu)

muprime = np.pi/2 + eta - mu - gamma
muprime_d = np.rad2deg(muprime)

## In 2 unit module
X_0 = np.zeros(1801,)
Y_0 = np.zeros(1801,)

X_1 = L*np.cos(np.pi+muprime)
Y_1 = L*np.sin(np.pi+muprime)

X_2 = L*np.cos(beta)
Y_2 = L*np.sin(beta)

X_3 = L*np.cos(beta) + L*np.cos(2.*np.pi - (np.pi/2. - mu - gamma - beta))
Y_3 = L*np.sin(beta) + L*np.sin(2.*np.pi - (np.pi/2. - mu - gamma - beta))

X_deg = np.array([])
Y_deg = np.array([])
for i in range(1801):
    X_deg = np.append(X_deg, [X_1[i,], X_0[i,], X_2[i,], X_3[i,]])
    Y_deg = np.append(Y_deg, [Y_1[i,], Y_0[i,], Y_2[i,], Y_3[i,]])

X_deg = np.reshape(X_deg, [1801, 4])
Y_deg = np.reshape(Y_deg, [1801, 4])

zeta = np.pi/2 + eta - mu - gamma - beta
zeta_d = np.rad2deg(zeta)

r = L/(2.*np.sin(zeta/2.))

H = h + L*np.sin(beta + muprime)

## experimental result

alpha_1e = np.array([27.3,
31.4,
40.4,
44.1,
53.05,
61,
67.95,
72.7,
62.4,
47.25,
38.2,
36.1
])


# H_e = np.array([16.05601311,
# 17.99566269,
# 21.09900475,
# 24.94449615,
# 28.75326157,
# 31.20499611,
# 33.04292679,
# 34.65977669,
# 35.75088501,
# 36.99892998,
# 38.19879532])
#
# L_e = np.array([29.68,
# 29.71333333,
# 30.70333333,
# 31.66666667,
# 32.63333333,
# 33.46666667,
# 34.05666667,
# 34.58333333,
# 34.95,
# 35.39,
# 35.84666667
# ])

## Estimating experimental radius of curvature from 3 ponits

def define_circle(p1, p2, p3):
    """
    Returns the center and radius of the circle passing the given 3 points.
    In case the 3 points form a line, returns (None, infinity).
    """
    temp = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2
    cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

    if abs(det) < 1.0e-6:
        return (None, np.inf)

    # Center of circle
    cx = (bc*(p2[1] - p3[1]) - cd*(p1[1] - p2[1])) / det
    cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det

    radius = np.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
    return ((cx, cy))

def define_radius(p1, p2, p3):
    """
    Returns the center and radius of the circle passing the given 3 points.
    In case the 3 points form a line, returns (None, infinity).
    """
    temp = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2
    cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

    if abs(det) < 1.0e-6:
        return (None, np.inf)

    # Center of circle
    cx = (bc*(p2[1] - p3[1]) - cd*(p1[1] - p2[1])) / det
    cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det

    radius = np.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
    return (radius)

p1e = np.array([[36.848, 54.825],
[36.593,	54.311],
[36.421,	53.802],
[36.339,	53.208],
[36.251,	52.705],
[36.164,	52.368],
[36.161,	52.109],
[36.169,	51.857],
[36.243,	52.194],
[36.418,	52.965],
[36.593,	53.553],
[36.76,	53.892]])

p2e = np.array([[60.326,	46.594],
[60.077,	44.988],
[59.998,	42.696],
[59.825,	40.412],
[59.661,	38.202],
[59.574,	36.421],
[59.484,	34.971],
[59.484,	33.962],
[59.489,	35.748],
[59.566,	39.301],
[59.656,	41.848],
[59.741,	43.719]])

p3e = np.array([[85.435,	42.269],
[86.028,	39.98],
[86.791,	36.848],
[87.721,	33.79],
[88.739,	30.994],
[89.672,	28.792],
[90.438,	26.844],
[91.029,	25.482],
[89.924,	27.774],
[88.151,	32.351],
[87.046,	35.83],
[86.365,	38.459]])

p4e = np.array([[109.003,	47.445],
[109.523,	46.239],
[110.45,	44.813],
[111.126,	43.465],
[111.727,	42.108],
[112.316,	41.172],
[112.904,	40.316],
[113.251,	39.725],
[112.567,	40.748],
[111.386,	42.678],
[110.365,	44.138],
[109.952,	45.364]])

CxCy1 = np.array([])
CxCy2 = np.array([])
radius1e = np.array([])
radius2e = np.array([])

for i in range(12):
    CxCy1 = np.append(CxCy1, define_circle(p1e[i,],p2e[i,],p3e[i,]))
    CxCy2 = np.append(CxCy2, define_circle(p2e[i,],p3e[i,],p4e[i,]))
    radius1e = np.append(radius1e, define_radius(p1e[i,],p2e[i,],p3e[i,]))
    radius2e = np.append(radius2e, define_radius(p2e[i,],p3e[i,],p4e[i,]))

#
# CxCy1 = 10.*CxCy1
# CxCy2 = 10.*CxCy2
# radius1e = 10.*radius1e
# radius2e = 10.*radius2e


print(CxCy1)
print(radius1e)

radius_avg = (radius1e + radius2e)/2.
print(radius_avg.shape)

## plot
# fig, axs = plt.subplots(2)
# fig.suptitle(r'$\theta$ and $\eta$ by dihedral angle $\alpha_1$')
# axs[0].plot(alpha_1d, theta_d)
# axs[0].set_ylabel(r'$\theta$ [$\degree$]')
# axs[0].set_xlim(0,180)
# axs[0].grid(color='lightgray',linestyle='--')
# axs[1].plot(alpha_1d, eta_d)
# axs[1].set_xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# axs[1].set_ylabel(r'$\eta$ [$\degree$]')
# axs[1].set_xlim(0,180)
# axs[1].grid(color='lightgray',linestyle='--')
#
# fig, axs = plt.subplots(2)
# fig.suptitle(r'Side lenght (d) and out-of-plane deformation of points')
# axs[0].plot(alpha_1d, d, color='k')
# axs[0].set_ylabel(r'Side length (d) [mm]')
# axs[0].set_xlim(0,180)
# axs[0].grid(color='lightgray',linestyle='--')
# axs[1].plot(alpha_1d, Z_24, color='r', label=r'$A_n$')
# axs[1].plot(alpha_1d, Z_13, color='gold', label=r'$B_n$')
# axs[1].plot(alpha_1d, Z_23, color='yellowgreen', label=r'C')
# axs[1].legend(fancybox=True)
# axs[1].set_xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# axs[1].set_ylabel('Out-of-plane deformation [mm]')
# axs[1].set_xlim(0,180)
# axs[1].grid(color='lightgray',linestyle='--')
#
# fig, axs = plt.subplots(2)
# fig.suptitle('Parameters in cross-section plane for estimating curvature')
# axs[0].plot(alpha_1d, L, color='b')
# axs[0].set_ylabel('L [mm]')
# axs[0].set_xlim(0,180)
# axs[0].grid(color='lightgray',linestyle='--')
# axs[1].plot(alpha_1d, beta, color='k')
# axs[1].set_xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# axs[1].set_ylabel(r'$\beta$ [$\degree$]')
# axs[1].set_xlim(0,180)
# axs[1].grid(color='lightgray',linestyle='--')
#
# fig, axs = plt.subplots(2)
# fig.suptitle('Describing relationship of the each unit module in terms of angle')
# axs[0].plot(alpha_1d, mu_d, color='purple')
# axs[0].set_ylabel(r'$\mu$ [$\degree$]')
# axs[0].set_xlim(0,180)
# axs[0].grid(color='lightgray',linestyle='--')
# axs[1].plot(alpha_1d, muprime_d, color='yellowgreen')
# axs[1].set_xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# axs[1].set_ylabel(r'$\mu^\prime$ [$\degree$]')
# axs[1].set_xlim(0,180)
# axs[1].grid(color='lightgray',linestyle='--')
#
# plt.figure(5)
# plt.plot(X_deg[100,], Y_deg[100,], 'k-o')
# plt.plot(X_deg[330,], Y_deg[330,], 'b-o')
# plt.plot(X_deg[630,], Y_deg[630,], 'r-o')
# # plt.plot(X_deg[1000,], Y_deg[1000,], 'g-o')
# plt.xlim([-40,80])
# plt.ylim([-60,60])
# plt.title(r'In plane position of origami structure composed by 2 unit module')
# plt.legend([r'$\alpha_1$ = 10 $\degree$', r'$\alpha_1$ = 33 $\degree$', r'$\alpha_1$ = 63 $\degree$'])
# plt.xlabel(r'$x^\prime$ position [mm]')
# plt.ylabel(r'$y^\prime$ position [mm]')
# plt.grid(color='lightgray',linestyle='--')
#
# plt.figure(6)
# plt.plot(alpha_1d, zeta_d, color='k')
# plt.xlim([0,180])
# plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# plt.ylabel(r'$\zeta$ [$\degree$]')
# plt.grid(color='lightgray',linestyle='--')
#
# plt.figure(7)
# plt.plot(alpha_1d, r, color='r')
# plt.xlim([0,180])
# plt.ylim([0,300])
# plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# plt.ylabel(r'Radius of curvature, $r$ [mm]')
# plt.grid(color='lightgray',linestyle='--')
#
# plt.figure(8)
# plt.plot(alpha_1d, 1/r, color='r')
# plt.xlim([0,180])
# # plt.ylim([0,300])
# plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# plt.ylabel(r'Curvature, $\kappa$ [1/mm]')
# plt.grid(color='lightgray',linestyle='--')

# plt.figure(9)
# plt.plot(alpha_1d, L, color='b')
# plt.plot(alpha_1e, L_e, 'b--o')
# plt.xlim([0,180])
# plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# plt.ylabel(r'L [mm]')
# plt.legend(['Model', 'Experiment1', 'Experiment2'])
# plt.grid(color='lightgray',linestyle='--')
#
#
# plt.figure(10)
# plt.plot(alpha_1d, H, color='r')
# plt.plot(alpha_1e, H_e, 'r--o')
# plt.xlim([0,180])
# plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# plt.ylabel(r'H [mm]')
# plt.legend(['Model', 'Experiment1', 'Experiment2'])
# plt.grid(color='lightgray',linestyle='--')

plt.figure(11)
plt.plot(alpha_1d, r, color='r')
plt.plot(alpha_1e, radius_avg, 'k--o')
plt.xlim([0,180])
plt.ylim([0,300])
plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
plt.ylabel(r'Radius of curvature, $\kappa$ [mm]')
plt.legend(['Model', 'Experiment1', 'Experiment2'])
plt.grid(color='lightgray',linestyle='--')

plt.show()

## export data
# alpha_1d_data = pd.DataFrame(alpha_1d)
# alpha_1d_data.to_csv("alpha_1d.csv", header=False, index=False, encoding='utf-8')
# d_data = pd.DataFrame(d)
# d_data.to_csv("d.csv", header=False, index=False, encoding='utf-8')
# D_data = pd.DataFrame(X_15)
# D_data.to_csv("D.csv", header=False, index=False, encoding='utf-8')
# Z_24_data = pd.DataFrame(Z_24)
# Z_24_data.to_csv("Z_24.csv", header=False, index=False, encoding='utf-8')

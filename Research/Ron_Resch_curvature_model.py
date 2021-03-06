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

alpha_1e = np.array([31.3,
33.35,
38.65,
45.05,
52.55,
60.1,
67,
73.1,
78.4,
86.15,
87.7,
])

alpha_1e2 = np.array([24.6,
26.25,
31.8,
37.2,
43.65,
49.55,
54.35,
58.6,
62.9,
66.1,
78.25
])

L_e = np.array([29.68,
29.71333333,
30.70333333,
31.66666667,
32.63333333,
33.46666667,
34.05666667,
34.58333333,
34.95,
35.39,
35.84666667
])
H_e = np.array([16.05601311,
17.99566269,
21.09900475,
24.94449615,
28.75326157,
31.20499611,
33.04292679,
34.65977669,
35.75088501,
36.99892998,
38.19879532])

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

p1e = np.array([[3.037999868,	0.495697021],
[2.995604992,	0.527683258],
[2.979025364,	0.631112099],
[2.931902647,	0.733244896],
[2.89221406,	0.836886406],
[2.881969213,	0.897356987],
[2.855140924,	0.943962097],
[2.851706028,	0.987566948],
[2.840724707,	1.006403923],
[2.832406521,	1.024513245],
[2.822229147,	1.076031685]])

p2e = np.array([[5.83714819,	1.341182709],
[5.797153473,	1.529578209],
[5.788204193,	1.848707199],
[5.777799606,	2.214751244],
[5.765233994,	2.553671837],
[5.744220734,	2.823997498],
[5.740748405,	2.992624283],
[5.733437061,	3.138293266],
[5.724719048,	3.236223221],
[5.713824749,	3.359333992],
[5.706037521,	3.490119934]])

p3e = np.array([[8.877485275,	1.610573769],
[8.887722015,	1.801017761],
[8.93182373,	2.113115311],
[9.012430191,	2.502466202],
[9.10067749,	2.86907196],
[9.162157059,	3.120157242],
[9.234647751,	3.319374084],
[9.257892609,	3.474018097],
[9.289382935,	3.574407578],
[9.345821381,	3.699581146],
[9.389957428,	3.830252647]])

p4e = np.array([[11.73315239,	1.000481606],
[11.73799324,	1.096414566],
[11.77360725,	1.277734756],
[11.86175919,	1.476798058],
[11.94824982,	1.669686317],
[12.02696228,	1.811555862],
[12.08072472,	1.891882896],
[12.11910248,	1.974629402],
[12.13714027,	2.00561142],
[12.18409538,	2.080513],
[12.21587563,	2.12437439]])

CxCy1 = np.array([])
CxCy2 = np.array([])
radius1e = np.array([])
radius2e = np.array([])

for i in range(11):
    CxCy1 = np.append(CxCy1, define_circle(p1e[i,],p2e[i,],p3e[i,]))
    CxCy2 = np.append(CxCy2, define_circle(p2e[i,],p3e[i,],p4e[i,]))
    radius1e = np.append(radius1e, define_radius(p1e[i,],p2e[i,],p3e[i,]))
    radius2e = np.append(radius2e, define_radius(p2e[i,],p3e[i,],p4e[i,]))


CxCy1 = 10.*CxCy1
CxCy2 = 10.*CxCy2
radius1e = 10.*radius1e
radius2e = 10.*radius2e


print(CxCy1)
print(radius1e)

radius_avg = (radius1e + radius2e)/2.
print(radius_avg.shape)

## Experiment result (pressure)
pressure = np.array([5,
                     10,
                     15,
                     20,
                     25,
                     30,
                     35,
                     40])
print(pressure)

pressure_p1 = np.array([[36.761,	37.865],
[36.339,	38.971],
[35.746,	40.41],
[35.489,	41.345],
[35.404,	41.851],
[35.237,	42.956],
[35.316,	44.141],
[35.483,	44.989]])
pressure_p2 = np.array([[60,	47.194],
[59.831,	51.095],
[59.746,	56.353],
[59.661,	60.002],
[59.743,	61.184],
[59.828,	64.24],
[60.003,	67.378],
[60,	68.139]])
pressure_p3 = np.array([[85.951,	51.856],
[86.886,	56.353],
[88.241,	61.611],
[89.595,	65.515],
[90.024,	66.872],
[91.039,	69.079],
[92.144,	71.197],
[92.984,	72.551]])
pressure_p4 = np.array([[109.699,	45.498],
[110.884,	48.045],
[112.492,	50.841],
[113.682,	52.537],
[114.191,	53.133],
[115.037,	54.148],
[115.802,	54.911],
[115.845,	54.855]])

pressure_radius1e = np.array([])
pressure_radius2e = np.array([])

for i in range(8):
    pressure_radius1e = np.append(pressure_radius1e, define_radius(pressure_p1[i,],pressure_p2[i,],pressure_p3[i,]))
    pressure_radius2e = np.append(pressure_radius2e, define_radius(pressure_p2[i,],pressure_p3[i,],pressure_p4[i,]))

pressure_radius_avg = (pressure_radius1e + pressure_radius2e)/2.

pressure_delta_h = np.array([1.612,
6.109,
11.367,
15.271,
16.628,
18.835,
20.953,
22.307])

## Experiment result (frequency)

frequency = np.array([0.25,
                      0.5,
                      1,
                      2.5,
                      5])

frequency_p1 = np.array([[35.226,	42.194],
[35.395,	41.521],
[35.568,	40.586],
[35.989,	39.744],
[36.246,	38.89]])
frequency_p2 = np.array([[59.644,	61.952],
[59.732,	59.748],
[59.732,	56.611],
[59.896,	52.965],
[60.073,	50.003]])
frequency_p3 = np.array([[90.421,	67.466],
[89.576,	65.171],
[88.474,	61.613],
[87.2,	57.628],
[86.185,	54.237]])
frequency_p4 = np.array([[114.162,	53.389],
[113.229,	52.287],
[112.132,	50.591],
[111.027,	48.723],
[110.179,	46.775]])

frequency_radius1e = np.array([])
frequency_radius2e = np.array([])

for i in range(5):
    frequency_radius1e = np.append(frequency_radius1e, define_radius(frequency_p1[i,],frequency_p2[i,],frequency_p3[i,]))
    frequency_radius2e = np.append(frequency_radius2e, define_radius(frequency_p2[i,],frequency_p3[i,],frequency_p4[i,]))

frequency_radius_avg = (frequency_radius1e + frequency_radius2e)/2.

frequency_delta_h = np.array([17.299,
12.037,
9.326,
7.376,
3.644])

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
# plt.plot(alpha_1e, L_e, 'k--o')
# plt.plot(alpha_1e2, L_e, 'b--o')
# plt.xlim([0,180])
# plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
# plt.ylabel(r'L [mm]')
# plt.legend(['Model', 'Experiment1', 'Experiment2'])
# plt.grid(color='lightgray',linestyle='--')
#
#
plt.figure(10)
plt.plot(alpha_1d, H, color='r')
plt.plot(alpha_1e, H_e, 'k--o')
plt.plot(alpha_1e2, H_e, 'r--o')
plt.xlim([0,180])
plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
plt.ylabel(r'H [mm]')
plt.legend(['Model', 'Experiment1', 'Experiment2'])
plt.grid(color='lightgray',linestyle='--')

plt.figure(11)
plt.plot(alpha_1d, r, color='r')
# plt.plot(alpha_1e, radius_avg, 'r--o')
plt.plot(alpha_1e2, radius_avg, 'r--o')
plt.xlim([0,180])
plt.ylim([0,300])
plt.xlabel(r'Dihedral angle ($\alpha_1$) [$\degree$]')
plt.ylabel(r'Radius of curvature, $\kappa$ [mm]')
plt.legend(['Model', 'Experiment1', 'Experiment2'])
plt.grid(color='lightgray',linestyle='--')
#
plt.figure(12)
plt.plot(pressure, pressure_radius_avg, 'r--o')
plt.xlim([0,45])
plt.ylim([40,100])
plt.xlabel('Inner pressure [kPa]')
plt.ylabel(r'Radius of curvature, $\kappa$ [mm]')
plt.grid(color='lightgray',linestyle='--')

plt.figure(13)
plt.plot(frequency, frequency_radius_avg, 'r--o')
plt.xlim([0,5])
plt.ylim([40,100])
plt.xlabel('Actuation frequency [Hz]')
plt.ylabel(r'Radius of curvature, $\kappa$ [mm]')
plt.grid(color='lightgray',linestyle='--')

plt.figure(14)
plt.plot(pressure, pressure_delta_h, 'k--o')
plt.xlim([0,45])
plt.ylim([0,30])
plt.xlabel('Inner pressure [kPa]')
plt.ylabel(r'Displacement, $\delta$H [mm]')
plt.grid(color='lightgray',linestyle='--')

plt.figure(15)
plt.plot(frequency, frequency_delta_h, 'k--o')
plt.xlim([0,5])
plt.ylim([0,30])
plt.xlabel('Actuation frequency [Hz]')
plt.ylabel(r'Displacement, $\delta$H [mm]')
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

import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy import units as u
import scipy

df = pd.read_csv('Clusters.csv')

num1 = (df.Cluster == 1).sum()
num2 = (df.Cluster == 2).sum()

avgra1 = ((df.loc[df['Cluster'] == 1, 'RA'].sum())/num1)*u.degree
avgra1 = ((df.loc[df['Cluster'] == 2, 'RA'].sum())/num2)*u.degree
avgdec1 = ((df.loc[df['Cluster'] == 1, 'DEC'].sum())/num1)*u.degree
avgdec2 = ((df.loc[df['Cluster'] == 2, 'DEC'].sum())/num2)*u.degree

Mra = np.array(SkyCoord.from_name('M1').ra.degree)
for i in range(2,111):
    raval = np.array(SkyCoord.from_name('M{}'.format(i)).ra.degree)
    Mra = np.append(Mra, raval)

Mdec = np.array(SkyCoord.from_name('M1').dec.degree)
for i in range(2,111):
    decval = np.array(SkyCoord.from_name('M{}'.format(i)).dec.degree)
    Mdec = np.append(Mdec, decval)

names = np.array('Messier 1')
for i in range(2,111):
    name = np.array('Messier {}'.format(i))
    names = np.append(names, name)

df1 = pd.DataFrame()
df1['Name'] = names.tolist()
df1['Ra'] = Mra.tolist()
df1['Dec'] = Mdec.tolist()
df1.index += 1
df1.to_csv('Messier.csv',index = False)

ra1 = np.asarray(df['RA'])
dec1 = np.asarray(df['DEC'])
c1 = SkyCoord(ra = ra1*u.degree, dec = dec1*u.degree, frame = 'icrs')
c2 = SkyCoord(ra = Mra*u.degree, dec = Mdec*u.degree, frame = 'icrs')
idx, d2d, d3d = (c1).match_to_catalog_sky(c2)

df['Astrosat_Flag'] = np.zeros(len(df))

matches = []
max_radius = 30./3600

for id1, (closest_id2, dist) in enumerate(zip(idx, d2d)):
    closest_dist = dist.value
    if closest_dist < max_radius:
        matches.append([id1, closest_id2, closest_dist])
        df['Astrosat_Flag'][id1] = 1
print(len(matches))
print(df[df['Astrosat_Flag']==1])

idx1, d2d1, d3d1 = (c2).match_to_catalog_sky(c1)

df1['Astrosat_Flag'] = np.zeros(len(df1))

matches1 = []
max_radius = 30./3600

for id1, (closest_id2, dist) in enumerate(zip(idx1, d2d1)):
    closest_dist = dist.value
    if closest_dist < max_radius:
        matches1.append([id1, closest_id2, closest_dist])
        df1['Astrosat_Flag'][id1] = 1
print(len(matches1))
print(df1[df1['Astrosat_Flag']==1])

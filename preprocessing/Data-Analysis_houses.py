### Data-Analysis project ###
### Pauwel De Wilde ###
### BeCode.org - Bouman 3.31 ###

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import re

url = "https://raw.githubusercontent.com/jejobueno/challenge-collecting-data/main/assets/housing-data.csv"
df = pd.read_csv(url)


# GET THE DATAFRAME READY
# sort by location & type
df = df.sort_values(["postalCode"], ascending = False).reset_index()
df = df.iloc[:, 2:]

# reorganize gardens and terraces under "outsideSpace"
df.terraceSurface.fillna(0, inplace = True)
df.gardenSurface.fillna(0, inplace = True)
df["outsideSpace"] = df["terraceSurface"] + df["gardenSurface"]

# column per province
df["province"] = df["postalCode"]
df["province"] = df["province"].astype(str).replace(to_replace = r"(1[0-3]\d{2})", value = "BRU", regex = True)	
df["province"] = df["province"].astype(str).replace(to_replace = r"(1[5-9]\d{2})", value = "VLB", regex = True)	
df["province"] = df["province"].astype(str).replace(to_replace = r"(3[0-4]\d{2})", value = "VLB", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(1[3-4]\d{2})", value = "WAB", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(2\d{3})", value = "ANT", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(3[5-9]\d{2})", value = "LIM", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(4\d{3})", value = "LUI", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(5\d{3})", value = "NAM", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(6[0-5]\d{2})", value = "HEN", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(7\d{3})", value = "HEN", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(6[6-9]\d{2})", value = "LUX", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(8\d{3})", value = "WVL", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(9\d{3})", value = "OVL", regex = True)

# dataframe per region
df_fla = df[((df["province"] == "VLB") | (df["province"] == "ANT") | (df["province"] == "WVL") | (df["province"] == "OVL") | (df["province"] == "LIM"))]
df_wal = df[((df["province"] == "WAB") | (df["province"] == "LUI") | (df["province"] == "NAM") | (df["province"] == "HEN") | (df["province"] == "LUX"))]

# CUT THE DATAFRAME
# reduntant colums
df = df.drop(["typeSale", "hasFullyEquippedKitchen", "gardenSurface", "terraceSurface", "facadeCount"], axis = 1)

# redundant rows
annuity_index = df[df["subtypeSale"] == "LIFE_ANNUITY"].index
df = df.drop(annuity_index, axis = 0).reset_index()

housegroup_index = df[df["typeProperty"] == "HOUSE_GROUP"].index
df = df.drop(housegroup_index, axis = 0).reset_index()
df = df.iloc[:, 2:]

df.drop_duplicates(["postalCode", "price"], keep = "last")

###############################

# CREATE SEPERATE DATAFRAMES
# per property type
df_houses = df[df["typeProperty"] == "HOUSE"]
df_apartments = df[df["typeProperty"] == "APARTMENT"]

df_fla_h = df_fla[df_fla["typeProperty"] == "HOUSE"]
df_fla_a = df_fla[df_fla["typeProperty"] == "APARTMENT"]

df_wal_h = df_wal[df_wal["typeProperty"] == "HOUSE"]
df_wal_a = df_wal[df_wal["typeProperty"] == "APARTMENT"]

###############################

# VISUALIZATION
# with python and Matplotlib
# mean per province
houses = df_houses.groupby("province").price.mean().plot(kind = "bar")
plt.title("Mean house price per province (Belgium)")
plt.xlabel("Province")
plt.ylabel("Price")
plt.ylim(0, 1200000)
plt.savefig("housePerProvince")

df_apartments.groupby("province").price.mean().plot(kind = "bar")
plt.title("Mean apartment price per province (Belgium)")
plt.xlabel("Province")
plt.ylabel("Price")
plt.ylim(0, 1200000)
plt.savefig("apartmentPerProvince")

# mean per region
df_fla_h.groupby("province").price.mean().plot(kind = "bar")
plt.title("Mean house price in Flanders")
plt.xlabel("Province")
plt.ylabel("Price")
plt.ylim(0, 1200000)
plt.savefig("houseFlanders")

df_fla_a.groupby("province").price.mean().plot(kind = "bar")
plt.title("Mean apartment price in Flanders")
plt.xlabel("Province")
plt.ylabel("Price")
plt.ylim(0, 1200000)
plt.savefig("apartmentFlanders")

df_wal_h.groupby("province").price.mean().plot(kind = "bar")
plt.title("Mean house price in Walonia")
plt.xlabel("Province")
plt.ylabel("Price")
plt.ylim(0, 1200000)
plt.savefig("houseWallonia")

df_wal_a.groupby("province").price.mean().plot(kind = "bar")
plt.title("Mean apartment price in Walonia")
plt.xlabel("Province")
plt.ylabel("Price")
plt.ylim(0, 1200000)
plt.savefig("apartmentWallonia")

# mean in Belgium
df.groupby("province").price.mean().plot(kind = "bar")
plt.title("Mean property price in Belgium")
plt.xlabel("Province")
plt.ylabel("Price")
plt.ylim(0, 1200000)
plt.savefig("meanBelgium")

# # per municipality
# df.groupby("postalCode").price.mean().head(10).plot(kind = "bar")
# plt.show()

# df_fla.groupby("postalCode").price.mean().head(10).plot(kind = "bar")
# plt.figure(figsize= (10, 20))
# ax = plt.subplot()
# ax.ticklabel_format(useOffset = False)
# plt.title("Mean property price in Belgium")
# plt.xlabel("Province")
# plt.ylabel("Price")
# plt.ylim(0, 1200000)
# plt.show()

# with Seaborn
# ppr = df_houses.groupby("province")["price"].mean()
# ppr.reset_index()
# print(ppr)
# sns.barplot(x = "province", y = ppr, data = df_houses)
# plt.ylim(0, None)
# plt.show()
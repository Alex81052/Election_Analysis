counties = ["Araphoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
counties = ["Araphoe","Denver","Jefferson"] 
if "Araphoe" in counties  or "El Paso" in counties: 
    print("Araphoe or El Paso is in the list of counties")
else: 
    print("Araphoe and El Paso is not in the list of counties.")
for county in counties:
    print("county")
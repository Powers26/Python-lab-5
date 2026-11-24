#Lium Powers, Python, 11/19/2026
import urllib.request
import json
import statistics

#takes url and acesses it to create a list of the signatures of earthquakes, which it returns
def sigList():
    slist = []
    handle = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson")
    
    data = handle.read()
    edata = json.loads(data)
    siglist = edata.get('features')

    for i in range(len(siglist)):
        dat = siglist[i]
        properties = dat.get('properties')
        sig = properties.get('sig')
        slist.append(sig)


    return(slist)

#stores return of siglist function as elist
elist = sigList()

#formatting for 3 digits after decimal
print("The min is ", "{0:2.3f}".format(min(elist)))
print("The max is ", "{0:2.3f}".format(max(elist)))
print("The mean is ", "{0:2.3f}".format(statistics.mean(elist)))
print("The median is ", "{0:2.3f}".format(statistics.median(elist)))
print("The standard deviation is ", "{0:2.3f}".format(statistics.stdev(elist)))
print("The mode is ", "{0:2.3f}".format(statistics.mode(elist)))


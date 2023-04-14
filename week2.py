import matplotlib.pyplot as plot

# set up your lists
numlist = [8, 7, 4, 2]
namelist = ['blue', 'orange', 'pink', 'yellow']
colorlist = ['blue', 'orange', 'pink', 'yellow']
explodelist = [0.05, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist, explode=explodelist,
         startangle=120, shadow=True, wedgeprops={"edgecolor": 'black'})
plot.axis('equal')
plot.savefig('piechart.png')
plot.show()

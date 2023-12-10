import matplotlib.pyplot as plt
state = ["Oyo","Osun","Ogun","Lagos","Ondo"]
#Portion covered by each state
angle = [3, 7,8,6, 10]
#Color for each state
colors = ["red","orange","green","pink", "blue"]
plt.pie(angle, colors = colors, labels = state, startangle = 180, shadow = True,
        explode = (0,0,0,0,0), radius = 0.8, autopct = "%1.2f%%" )
#Legend

plt.ylabel("Girls axis")
plt.title("Graph of boys versus girls")
plt.legend()
#function to show the plot
plt.show()

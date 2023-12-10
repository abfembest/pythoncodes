import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,3,4,5]
x2 = [1,2,3,4,5]
tick_label = ["One", "Two","Three", "Four", "Five"]
plt.bar(y,x2, label = "line 1", width = 0.8, tick_label= tick_label,color = ["blue","red","black"])
#plt.scatter(y,x2, marker = "*") 
#Giving x- axis name
plt.xlabel("Boys axis")
#Giving y- axis name
plt.ylabel("Girls axis")
plt.title("Graph of boys versus girls")
plt.legend()
#function to show the plot
plt.show()

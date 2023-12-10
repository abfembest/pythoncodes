import matplotlib.pyplot as plt
fine_babes =[2,3,5,7,9]
wowo_babes= [1,3,5,6,8]
runs_babes= [3,4,5,7,7]

plt.plot(fine_babes, wowo_babes, runs_babes , marker="*", label = "Line 1")
plt.xlabel("fine_babes")
plt.ylabel("wowo_babes")
plt.title("officer David's choice of babes")
plt.legend()


plt.show()


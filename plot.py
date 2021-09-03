import matplotlib.pyplot as plt

REPORT_DIR = "./reports"
if __name__ == "__main__":
    file_name = input("Enter file name: ")
    bests = []
    worsts = []
    avgs = []
    with open(REPORT_DIR+"/"+file_name+".txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            infos = line.strip("\n").split(",")
            gen_num, best, worst, avg = int(infos[0]) , int(infos[1]), int(infos[2]), float(infos[3])
            bests.append(best)
            worsts.append(worst)
            avgs.append(avg)
            
    
    plt.plot(range(len(bests)), bests, label="best")
    plt.plot(range(len(bests)), worsts, label="worst")
    plt.plot(range(len(bests)), avgs, label="average")
    plt.legend()
    plt.show()
            
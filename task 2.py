time_sek = int(input("Enter time sek: "))
time_chas = time_sek//3600
time_min_sek = time_sek - time_chas*3600
time_min = time_min_sek//60
time_sek = time_min_sek - time_min*60

print("время в формате ч:м:с = {0}:{1}:{2}".format(time_chas,time_min,time_sek))
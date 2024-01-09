import main
import time


start_vanilla = time.time()
main.prime_finder_vanilla(4000)
end_vanilla = time.time()

vanilla_time = end_vanilla - start_vanilla
# print(end_vanilla-start_vanilla)

start_optimized= time.time()
main.prime_finder_optimized(4000)
end_optimized = time.time()
optTiem = end_optimized - start_optimized


print(vanilla_time)
print(optTiem)
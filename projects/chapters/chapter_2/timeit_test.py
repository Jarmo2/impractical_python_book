import time
import palingrams


start = time.time()
print(palingrams.find_palingrams())
end = time.time()
print(f"Runtime of this program was {end - start} seconds.")
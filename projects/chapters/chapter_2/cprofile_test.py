import cProfile
import palingrams
import palingrams_speed_up

cProfile.run('palingrams.find_palingrams()')
cProfile.run('palingrams_speed_up.find_palingrams()')
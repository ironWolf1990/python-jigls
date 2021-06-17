import cProfile
import pstats
from typing import Callable


class Profile:
    def __init__(self) -> None:
        self.profiler = cProfile.Profile()

    def __call__(self, toProfle: Callable):
        self.profiler.enable()
        toProfle()
        self.profiler.disable()
        print(f"\n    {40*'='}\n         PROFILER\n    {40*'='}\n")
        pstats.Stats(self.profiler).sort_stats("ncalls").print_stats()


# def ProfileDecorator(toProfile):
#     def profileWrapper():
#         profiler = cProfile.Profile()
#         profiler.enable()

#         toProfile()

#         print(f"\n    {40*'='}\n         PROFILER\n    {40*'='}\n")
#         profiler.disable()
#         stats = pstats.Stats(profiler).sort_stats("ncalls")
#         stats.print_stats()

#     return profileWrapper
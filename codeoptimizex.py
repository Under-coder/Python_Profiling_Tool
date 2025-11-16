import cProfile
import pstats
import io

"""
    Profiles a given function with arguments and prints results sorted by cumulative time.
    Returns the function's result and the profiling stats as a string.
"""

def profile_function(func, *args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()                # Start profiling
    result = func(*args, **kwargs)   # Execute the user's function
    profiler.disable()               # Stop profiling

    s = io.StringIO()
    stats = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    stats.print_stats()
    print(s.getvalue())              # Print stats to console
    return result, s.getvalue()      # Return both function result and stats text

def slow_function():
    # Example slow function for demonstration
    for _ in range(1000000):
        _ = 1 + 1

def main():
    # Entry point for standalone run or testing
    profile_function(slow_function)

if __name__ == "__main__":
    main()

def save_profile(func, filename="profile_output.prof", *args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()
    profiler.dump_stats(filename)
    print(f"Profile saved into {filename}")
    return result

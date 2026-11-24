"""Independent illustrative dependency scheduler; no AI or network calls."""
def ready(tasks, completed):
    """Return unfinished tasks whose prerequisites have completed."""
    return sorted(name for name, deps in tasks.items()
                  if name not in completed and set(deps) <= set(completed))

if __name__ == "__main__":
    tasks = {"plan": [], "review": ["plan"], "report": ["review"]}
    done = set()
    while len(done) < len(tasks):
        wave = ready(tasks, done)
        if not wave:
            raise RuntimeError("Unresolved dependencies")
        print("Simulated wave:", wave)
        done.update(wave)

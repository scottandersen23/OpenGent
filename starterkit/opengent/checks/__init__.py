from . import freshness, duplicates, nulls, revenue

DEFAULT_CHECKS = [
    freshness.run,
    duplicates.run,
    nulls.run,
    revenue.run,
]

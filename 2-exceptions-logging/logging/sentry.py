import sentry_sdk

sentry_sdk.init(
    dsn="https://006662c900f90d003891d249d07be797@o4507508488273920.ingest.us.sentry.io/4507508494893056",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
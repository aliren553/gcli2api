# Render scheduled keepalive

The GitHub Actions workflow sends a HEAD request to /keepalive approximately
every 10 minutes, only during 12:00–02:00 Asia/Shanghai by default.
This is a provisional window, not a guarantee of uptime. Scheduled Actions can
be delayed or disabled for inactive repositories; fork workflows may require
enabling in GitHub Actions. Manual runs respect the same time window.

Repository Actions variables:
- RENDER_KEEPALIVE_ENABLED=false disables probing.
- RENDER_KEEPALIVE_START_HOUR (0–23, default 12)
- RENDER_KEEPALIVE_END_HOUR (0–23, default 2, exclusive)
Equal start/end disables probes, rather than enabling 24-hour operation.

Do not enable the app's internal KEEPALIVE_URL self-ping at the same time:
it defeats the inactive window. Ensure KEEPALIVE_URL is empty in Render and
the application's persisted configuration. No model requests or API credentials
are used. HEAD responses have no body, but still use bandwidth and running hours.
Render limits, restarts, and cold starts still apply. GitHub Actions usage limits
also apply. Pause this workflow to stop scheduled keepalive.

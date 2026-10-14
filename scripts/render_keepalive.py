"""Lightweight scheduled HEAD probe. No API keys or model requests."""
import os
from datetime import datetime
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo


def should_probe(now, enabled, start, end):
    if enabled.lower() not in ('true', '1', 'yes'):
        return False
    if not (0 <= start <= 23 and 0 <= end <= 23) or start == end:
        return False
    hour = now.hour
    return start <= hour < end if start < end else hour >= start or hour < end


def main():
    now = datetime.now(ZoneInfo('Asia/Shanghai'))
    enabled = os.getenv('KEEPALIVE_ENABLED', 'true')
    start = int(os.getenv('KEEPALIVE_START_HOUR', '12'))
    end = int(os.getenv('KEEPALIVE_END_HOUR', '2'))
    if not should_probe(now, enabled, start, end):
        print('Outside active window or disabled; no request sent.')
        return
    url = 'https://zaoligcli2api.onrender.com/keepalive'
    request = Request(url, method='HEAD', headers={'User-Agent': 'gcli2api-scheduled-healthcheck/1.0'})
    with urlopen(request, timeout=120) as response:
        print(f'HEAD probe status: {response.status}')


if __name__ == '__main__':
    main()

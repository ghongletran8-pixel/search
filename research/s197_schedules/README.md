# s197 official release schedules: fetch result

**Result: nothing fetched.** The cloud environment could not reach any of the requested publishers. **No raw files are in this folder**, and none were substituted from other sources.

## What happened (2026-10-02, UTC)
- Every requested host was refused by this environment's **egress proxy** with `403 to CONNECT (policy denial)`. That happens **before** any connection to the publisher, so there is no publisher HTTP status, header or byte to save.
- Per the proxy's own rules, policy denials were **not retried** and **not routed around**.
- Per-host denial timestamps and the mapping from each requested URL to its host are in `manifest.json` (`attempts`, `hosts_denied`). `files` is empty.

## Blocked even from the cloud (all 15 hosts tried)
| Target | Host(s) | Requested |
|---|---|---|
| 1 BLS | www.bls.gov | schedule/news_release/empsit.htm, cpi.htm, ppi.htm, jolts.htm, bls.ics; yearly calendar xls/ics |
| 2 S&P Global PMI | www.pmi.spglobal.com, www.spglobal.com | Public/Home/PressRelease; release-calendar page |
| 3 ISM | www.ismworld.org | Report on Business release dates |
| 4 Conference Board | www.conference-board.org | Consumer Confidence release schedule |
| 5 BEA | www.bea.gov, apps.bea.gov | news/schedule and any json/ics feed |
| 6 Federal Reserve | www.federalreserve.gov | monetarypolicy/fomccalendars.htm |
| 7 US Treasury | www.treasurydirect.gov, fiscaldata.treasury.gov, api.fiscaldata.treasury.gov, home.treasury.gov | auctions/upcoming and official announced-auction csv/json |
| 8 NAR / Census / EIA | www.nar.realtor, www.census.gov, www.eia.gov | existing-home-sales schedule; economic-indicators/calendar-listview.html; petroleum/supply/weekly/schedule.php |

## Not used, by design
- **WebFetch tool:** it returns model-processed text, not raw bytes, so it cannot meet "save each response unmodified".
- **Search snippets and third-party calendars:** excluded by the task rules.
- **Archive or mirror copies:** these would substitute another source and route around the egress policy.

## How to get the files
- **From this cloud environment:** the environment owner must allow these hosts in the environment's Network access settings (cloud environment menu → Edit; see https://code.claude.com/docs/en/claude-code-on-the-web). Then re-run the fetch.
- **From the laptop:** the laptop's 403s come from the publishers themselves. This environment never reached them, so it gives no information about publisher-side blocking.

Coverage fields (`covers_from`, `covers_to`, `has_explicit_time_zone`) are not filled because no file exists. No times were inferred.

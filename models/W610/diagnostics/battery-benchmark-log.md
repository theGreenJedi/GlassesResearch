# W610 normalized battery benchmark log

Use one copy of this form per run. Do not overwrite earlier runs. The purpose is reproducibility, not producing the largest runtime number.

## Run identity

| Field | Record |
|---|---|
| Run ID | |
| Date / start time / timezone | |
| Tester | |
| Device seller / label / revision | |
| Firmware | |
| Companion app or SDK version | |
| Host phone / OS | |
| Ambient temperature | |
| Device age / known cycle history | |
| Workload class | idle connected / fixed-volume audio / periodic stills / continuous video / Wi-Fi transfer / mixed |
| Network state | |
| Vendor endpoints blocked? | yes / no / not tested |

## Charge baseline

| Field | Record |
|---|---|
| Charge source and rated output | |
| Cable / magnetic adapter | |
| Starting device-reported charge | |
| Charge start / reported 100% time | |
| Defined taper duration | |
| Input Wh, if safely metered | |
| Temperature / abnormal behavior | |

Input Wh includes charging losses and must not be reported as cell capacity.

## Fixed workload definition

Record every variable needed to reproduce the workload:

- phone and glasses volume;
- audio source/file and loop behavior;
- capture interval, resolution and count;
- video resolution and duration;
- Wi-Fi transfer batch size and media bytes;
- screen/app state;
- Bluetooth/Wi-Fi connection state;
- AI or network activity;
- interruptions or deviations.

## Interval log

Use a fixed interval selected before the run.

| Elapsed | Reported % | Charging state | Work completed | Connection state | Temperature / observations |
|---:|---:|---|---|---|---|
| 00:00 | 100 | | | | |
| | | | | | |

## Cutoff behavior

| Check | Result |
|---|---|
| Below 15%: photo available? | |
| Below 15%: video available? | |
| Below 15%: audio recording available? | |
| Below 10%: music/multimedia available? | |
| Shutdown percentage and behavior | |
| Unsaved-media or transfer loss | |

Do not deep-cycle repeatedly merely to observe a cutoff. Stop immediately for swelling, unusual heat, odor, unstable charging, or enclosure deformation.

## Result

| Field | Record |
|---|---|
| Starting / ending reported charge | |
| Elapsed runtime | |
| Completed workload | |
| Mean reported drain per hour | |
| Endpoint/cutoff reached | |
| Invalidating deviations | |
| Evidence files / captures | |

## Replication summary

Do not publish a normalized runtime until at least three comparable valid runs exist.

| Run | Runtime | Work completed | Valid? | Notes |
|---|---:|---:|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| Median | | | | |
| Spread | | | | |

Report the median and spread. Keep claimed 270 mAh capacity and “up to” runtime separate from measured results.

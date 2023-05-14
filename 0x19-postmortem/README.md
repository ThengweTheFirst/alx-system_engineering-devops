# Server Outage Incident report
> By Mzwandile Aaron Sithebe


10th May 2023, we experienced server outage on all our server infrastructure which resulted in our clients inability to use our services and we sincerely apologize for the financial loss our clients have incurred during this period.

## Issue Summary
On 10th May 2023 (02:00 UTC + 2h), we experienced a server outage (downtime) on all of our server infrastructure which lasted for 3 hours. As a result of this, our clients experienced a http `500 error` which had a __90% impact__ on their business as they were unable to access our services. The root cause was not properly testing out all implemented upgrades before pushing to production servers.

## Timeline (all time in UTC + 2h)

| Time (UTC + 2h)     | Actions 	   |
| ------------------- | ------------------ |
| 02:00PM | Upgrades implementation begins |
| 02:05PM | Server Outage begins 	   |
| 02:15PM | Pagers alerted on-call team    |
| 02:30PM | On-call team acknowledgement   |
| 03:00PM | Rollback initiation begins	   |
| 04:00PM | Successful rollback		   |
| 05:00PM | Server restart initiated	   |
| 05:30PM | 100% of traffic back online    |

## Root cause
At 02:00PM (UTC + 2h) server upgrade was initiated across all our production servers without first releasing on our test environments and performing all necessary unit testing. Part of the upgrade been shipped to production server required an authentication from a 3rd party software, this new implementation is not supported on the current version present on our servers which resulted in the downtime experienced. We were able to resolve this quickly by first performing a rollback the severs previous state thereafter upgrading the current version on our servers.

## Preventive measures
- Pushing all intended changes 1st to our test environments before shipping to life server.
- Increase the performance metrics threshold to alert on-call engineers on the event of possible server crash 

